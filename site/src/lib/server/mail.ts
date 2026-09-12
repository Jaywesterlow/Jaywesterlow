import { env } from '$env/dynamic/private';

export type Inquiry = {
	apartment: string;
	arrival: string;
	departure: string;
	adults: number;
	children: number;
	name: string;
	email: string;
	phone: string;
	message: string;
};

/** Sends the inquiry through Resend (EU) when RESEND_API_KEY is set; otherwise logs it so the form works in preview. */
export async function sendInquiry(i: Inquiry): Promise<'sent' | 'logged'> {
	const key = env.RESEND_API_KEY;
	const to = env.INQUIRY_TO;
	const from = env.INQUIRY_FROM ?? 'Huis Hinterglemm <aanvraag@huishinterglemm.nl>';
	const text = [
		`Appartement: ${i.apartment}`,
		`Aankomst: ${i.arrival}  Vertrek: ${i.departure}`,
		`Volwassenen: ${i.adults}  Kinderen: ${i.children}`,
		`Naam: ${i.name}`,
		`E-mail: ${i.email}`,
		`Telefoon: ${i.phone || '-'}`,
		'',
		i.message || '(geen bericht)'
	].join('\n');
	if (!key || !to) {
		console.log('[inquiry:logged]\n' + text);
		return 'logged';
	}
	const res = await fetch('https://api.resend.com/emails', {
		method: 'POST',
		headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
		body: JSON.stringify({
			from,
			to: [to],
			reply_to: i.email,
			subject: `Aanvraag ${i.apartment} · ${i.arrival} – ${i.departure}`,
			text
		})
	});
	if (!res.ok) throw new Error(`Resend ${res.status}`);
	return 'sent';
}
