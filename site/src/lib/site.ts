/** One place for every fact about the business. Values in [brackets] must come from the client. */
export const site = {
	name: 'Huis Hinterglemm',
	tagline: 'Vier appartementen aan de piste in Hinterglemm',
	url: 'https://huishinterglemm.nl',
	locale: 'nl_NL',
	lang: 'nl',
	phoneDisplay: '06 [nummer]',
	phoneE164: '+316[nummer]',
	email: 'info@huishinterglemm.nl',
	instagram: 'https://www.instagram.com/huishinterglemm',
	kvk: '[KVK-nummer]',
	address: {
		street: '[straat en nummer]',
		postalCode: '5754',
		city: 'Hinterglemm',
		region: 'Salzburg',
		country: 'AT'
	},
	geo: { lat: 47.377, lng: 12.586 }, // Hinterglemm village centre; replace with the building's coordinates
	hosts: '[voornamen]',
	hostsFrom: '[plaats]',
	replyWithin: '24 uur',
	buildDate: new Date().toISOString().slice(0, 10)
} as const;

/** Anchors on the one-page demo. */
export const nav = [
	{ href: '#appartementen', label: 'Appartementen' },
	{ href: '#skigebied', label: 'Skigebied' },
	{ href: '#praktisch', label: 'Praktisch' },
	{ href: '#prijzen', label: 'Prijzen' },
	{ href: '#over-ons', label: 'Over ons' }
] as const;

/** Every link that does not exist yet in the demo points here; the layout opens the demo overlay for it. */
export const DEMO = '#demo';

/** Link for the 'contact Jaymar' button in the demo overlay (mailto: or wa.me). Empty hides the button. */
export const DEMO_CONTACT = '';

/** Resort facts, verified on saalbach.com on 2026-09-12. */
export const facts = {
	pistes: 270,
	blue: 140,
	red: 112,
	black: 18,
	lifts: 70,
	huts: 60,
	low: 830,
	high: 2096,
	season: '27 nov 2026 – 4 apr 2027',
	pass6Adult: 440,
	pass6Youth: 330,
	pass6Child: 220,
	peakDates: '19 dec – 12 mrt',
	alpinKm: 408,
	alpinLifts: 121,
	checked: '12 sep 2026'
} as const;
