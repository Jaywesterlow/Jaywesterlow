/** Season table 2026/27, Saturday to Saturday. Placeholder until the client's price list arrives. */
export type SeasonKey = 'low' | 'mid' | 'high';

export const seasons: { key: SeasonKey; name: string; ranges: string }[] = [
	{ key: 'low', name: 'Laagseizoen', ranges: '9 jan – 6 feb · 13 mrt – sluiting' },
	{ key: 'mid', name: 'Middenseizoen', ranges: 'opening – 19 dec · 6–13 feb · 27 feb – 13 mrt' },
	{ key: 'high', name: 'Hoogseizoen', ranges: '19 dec – 9 jan · 13–27 feb' }
];

export const seasonNote =
	'Per week, alles inbegrepen. Toeristenbelasting € [x] per persoon per nacht apart. Aankomst en vertrek op zaterdag in het hoogseizoen; daarbuiten ook kortere periodes op aanvraag.';
