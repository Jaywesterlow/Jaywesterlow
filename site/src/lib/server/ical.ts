import { env } from '$env/dynamic/private';
import { bySlug } from '$lib/data/apartments';

export type Range = [string, string];

/**
 * Booked ranges for an apartment. Reads an iCal feed (Airbnb / Booking.com export) from
 * ICAL_URL_<SLUG> when set, otherwise the placeholder ranges in the data file.
 * Pages are prerendered, so this runs at build time; redeploy (or move to ISR) to refresh.
 */
export async function bookedRanges(slug: string): Promise<Range[]> {
	const url = env[`ICAL_URL_${slug.toUpperCase()}`];
	const fallback = bySlug(slug)?.booked ?? [];
	if (!url) return fallback;
	try {
		const res = await fetch(url, { headers: { accept: 'text/calendar' } });
		if (!res.ok) return fallback;
		return parseIcal(await res.text());
	} catch {
		return fallback;
	}
}

/** Minimal VEVENT parser: DTSTART/DTEND (date or date-time, DTEND exclusive) -> inclusive ISO date ranges. */
export function parseIcal(text: string): Range[] {
	const lines = text.replace(/\r\n[ \t]/g, '').split(/\r?\n/);
	const out: Range[] = [];
	let start = '';
	let end = '';
	for (const line of lines) {
		if (line === 'BEGIN:VEVENT') {
			start = '';
			end = '';
		} else if (line.startsWith('DTSTART')) start = toIso(line);
		else if (line.startsWith('DTEND')) end = toIso(line);
		else if (line === 'END:VEVENT' && start) {
			const last = end ? addDays(end, -1) : start;
			out.push([start, last]);
		}
	}
	return out;
}

function toIso(line: string) {
	const v = line.split(':').pop() ?? '';
	return `${v.slice(0, 4)}-${v.slice(4, 6)}-${v.slice(6, 8)}`;
}

export function addDays(iso: string, n: number) {
	const d = new Date(iso + 'T00:00:00Z');
	d.setUTCDate(d.getUTCDate() + n);
	return d.toISOString().slice(0, 10);
}
