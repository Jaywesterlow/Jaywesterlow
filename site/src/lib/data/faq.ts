export type Faq = { q: string; a: string };

/** Question-shaped headings, answer in the first sentence: the format answer engines extract first. */
export const faq: Faq[] = [
	{
		q: 'Hoe ver is het appartement van de lift?',
		a: '250 tot 400 meter lopen naar de Reiterkogelbahn, afhankelijk van het appartement. Met ski’s op de schouder is dat drie tot vijf minuten. Er rijdt geen skibus tussen ons huis en de lift, omdat het niet hoeft.'
	},
	{
		q: 'Wat kost een week in de voorjaarsvakantie?',
		a: 'Hoogseizoen: Kohlmais € 1.500, Reiterkogel € 2.000, Zwölferkogel € 2.600 en Schattberg € 1.050 per week. Alles is inbegrepen behalve de toeristenbelasting. De volledige seizoenstabel staat op elke appartementpagina.'
	},
	{
		q: 'Is beddengoed inbegrepen?',
		a: 'Ja. Beddengoed, handdoeken, eindschoonmaak, wifi en een parkeerplaats zitten in de weekprijs. Je hoeft niets mee te nemen behalve je skispullen.'
	},
	{
		q: 'Kunnen we met acht personen?',
		a: 'Ja, in Zwölferkogel: vier slaapkamers, twee badkamers en een eettafel voor tien. Voor grotere groepen kun je Zwölferkogel en Reiterkogel samen huren; dan slaap je met veertien onder één dak.'
	},
	{
		q: 'Hoe werkt het boeken en betalen?',
		a: 'Je stuurt een aanvraag met je data en het aantal personen. Binnen 24 uur bevestigen we of het appartement vrij is en sturen we een voorstel. Je betaalt [x]% aanbetaling via iDEAL, de rest [x] weken voor aankomst.'
	},
	{
		q: 'Zijn huisdieren welkom?',
		a: '[Ja/nee]. [Voorwaarden, bijvoorbeeld: één hond, op aanvraag, € [x] extra schoonmaak.]'
	},
	{
		q: 'Is er parkeergelegenheid?',
		a: 'Ja, elk appartement heeft een eigen parkeerplaats bij het huis. Winterbanden zijn in Oostenrijk verplicht van 1 november tot 15 april; sneeuwkettingen zijn op onze weg zelden nodig, maar handig om bij je te hebben.'
	}
];
