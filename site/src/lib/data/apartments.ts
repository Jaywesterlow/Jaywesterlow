export type Slug = 'kohlmais' | 'reiterkogel' | 'zwoelferkogel' | 'schattberg';

export type Apartment = {
	slug: Slug;
	name: string;
	index: number;
	sleeps: string;
	sleepsMax: number;
	area: number;
	bedrooms: number;
	bathrooms: number;
	liftMeters: number;
	lift: string;
	summary: string;
	layout: string;
	included: string[];
	amenities: string[];
	price: { low: number; mid: number; high: number };
	photos: { key: string; alt: string; cap: string }[];
	/** placeholder booked ranges (ISO dates, inclusive) until iCal feeds are wired */
	booked: [string, string][];
};

const included = [
	'beddengoed',
	'handdoeken',
	'eindschoonmaak',
	'wifi',
	'parkeerplaats',
	'ski- en droogruimte'
];

export const apartments: Apartment[] = [
	{
		slug: 'kohlmais',
		name: 'Kohlmais',
		index: 1,
		sleeps: '4',
		sleepsMax: 4,
		area: 55,
		bedrooms: 2,
		bathrooms: 1,
		liftMeters: 250,
		lift: 'Reiterkogelbahn',
		summary:
			'Vier personen, twee slaapkamers en een balkon op het zuiden. Het appartement voor een gezin dat vooral buiten wil zijn.',
		layout:
			'[Woonkamer met open keuken en eettafel voor vier. Slaapkamer 1 met tweepersoonsbed, slaapkamer 2 met twee eenpersoonsbedden. Badkamer met douche. Balkon op het zuiden.]',
		included,
		amenities: ['vaatwasser', 'balkon zuid', 'skiberging'],
		price: { low: 850, mid: 1150, high: 1500 },
		photos: [
			{
				key: 'slaapkamer',
				alt: 'Slaapkamer van Kohlmais met uitzicht op de bergen',
				cap: 'slaapkamer'
			},
			{ key: 'woonkamer', alt: 'Woonkamer van Kohlmais', cap: 'woonkamer' },
			{ key: 'balkon', alt: 'Balkon met uitzicht over Hinterglemm', cap: 'balkon' }
		],
		booked: [
			['2026-12-19', '2027-01-02'],
			['2027-02-13', '2027-02-27']
		]
	},
	{
		slug: 'reiterkogel',
		name: 'Reiterkogel',
		index: 2,
		sleeps: '6',
		sleepsMax: 6,
		area: 80,
		bedrooms: 3,
		bathrooms: 2,
		liftMeters: 300,
		lift: 'Reiterkogelbahn',
		summary:
			'Zes personen, drie slaapkamers, sauna, en 300 meter lopen naar de Reiterkogelbahn. Het appartement voor twee gezinnen of een vriendengroep die één grote tafel wil.',
		layout:
			'[Woonkamer met open keuken en eettafel voor acht. Slaapkamer 1 en 2 met tweepersoonsbed, slaapkamer 3 met stapelbed. Twee badkamers, sauna, ski- en droogruimte beneden. Balkon op het zuiden.]',
		included,
		amenities: ['sauna', 'vaatwasser', 'twee badkamers', 'balkon zuid'],
		price: { low: 1100, mid: 1500, high: 2000 },
		photos: [
			{
				key: 'woonkamer',
				alt: 'Woonkamer van Reiterkogel met eettafel en uitzicht op de piste',
				cap: 'woonkamer'
			},
			{ key: 'slaapkamer', alt: 'Slaapkamer van Reiterkogel', cap: 'slaapkamer' },
			{ key: 'sauna', alt: 'Sauna van Reiterkogel', cap: 'sauna' },
			{ key: 'balkon', alt: 'Balkon van Reiterkogel', cap: 'balkon' }
		],
		booked: [
			['2026-12-19', '2027-01-09'],
			['2027-02-06', '2027-02-20']
		]
	},
	{
		slug: 'zwoelferkogel',
		name: 'Zwölferkogel',
		index: 3,
		sleeps: '8',
		sleepsMax: 8,
		area: 105,
		bedrooms: 4,
		bathrooms: 2,
		liftMeters: 400,
		lift: 'Reiterkogelbahn',
		summary:
			'Acht personen, vier slaapkamers, sauna en een open haard. Het grootste appartement, voor een groep die samen wil koken en eten.',
		layout:
			'[Grote woonkamer met open haard, keuken en eettafel voor tien. Vier slaapkamers, twee badkamers, sauna, droogruimte. Twee balkons.]',
		included,
		amenities: ['sauna', 'open haard', 'vaatwasser', 'twee badkamers', 'twee balkons'],
		price: { low: 1400, mid: 1900, high: 2600 },
		photos: [
			{ key: 'balkon', alt: 'Balkon van Zwölferkogel met uitzicht over het dal', cap: 'balkon' },
			{ key: 'woonkamer', alt: 'Woonkamer van Zwölferkogel', cap: 'woonkamer' },
			{ key: 'sauna', alt: 'Sauna van Zwölferkogel', cap: 'sauna' }
		],
		booked: [['2026-12-26', '2027-01-09']]
	},
	{
		slug: 'schattberg',
		name: 'Schattberg',
		index: 4,
		sleeps: '2–3',
		sleepsMax: 3,
		area: 40,
		bedrooms: 1,
		bathrooms: 1,
		liftMeters: 250,
		lift: 'Reiterkogelbahn',
		summary:
			'Studio voor twee, met een slaapbank voor een derde. Klein, licht en het dichtst bij de lift.',
		layout: '[Studio met kitchenette, tweepersoonsbed, slaapbank, badkamer met douche, balkon.]',
		included,
		amenities: ['kitchenette', 'balkon'],
		price: { low: 600, mid: 800, high: 1050 },
		photos: [
			{ key: 'sauna', alt: 'Badkamer en sauna-ruimte van Schattberg', cap: 'badkamer' },
			{ key: 'slaapkamer', alt: 'Slaapkamer van Schattberg', cap: 'slaapkamer' }
		],
		booked: [['2027-02-13', '2027-02-27']]
	}
];

export const bySlug = (slug: string) => apartments.find((a) => a.slug === slug);
export const euro = (n: number) => '€ ' + n.toLocaleString('nl-NL');
