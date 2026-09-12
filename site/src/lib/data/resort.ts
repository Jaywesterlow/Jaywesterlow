/** Resort facts. Marked [verifiëren] where the number must be checked against the official Skicircus site before launch. */
export const resort = {
	name: 'Skicircus Saalbach Hinterglemm Leogang Fieberbrunn',
	facts: [
		{ label: 'Pistekilometers', value: '270' },
		{ label: 'Liften', value: '70' },
		{ label: 'Hoogte', value: '830–2096 m' },
		{ label: 'Seizoen', value: 'dec – apr' }
	],
	verify: 'Cijfers verifiëren op saalbach.com vóór livegang.',
	levels: [
		{
			name: 'Blauw',
			text: 'De Reiterkogel is de kant voor kinderen en beginners: brede, rustige pistes en een skischool die op 200 meter van de deur start.'
		},
		{
			name: 'Rood',
			text: 'Richting Zwölferkogel en over de kam naar Saalbach: lange rode afdalingen waar je een hele dag op kunt variëren.'
		},
		{
			name: 'Zwart',
			text: 'De Zwölfer Nordabfahrt en de afdalingen bij Leogang voor wie ’s ochtends als eerste in de gondel wil zitten.'
		}
	],
	kids: 'Skischool en kinderland bij het dalstation van de Reiterkogelbahn. Skipas voor kinderen tot [x] jaar [gratis/korting] in [periode].',
	apres:
		'Hinterglemm heeft de rustige kant van het dal: een paar goede hutten aan de piste, twee bars in het dorp, en om tien uur is het stil. Saalbach ligt vijf minuten verderop met de bus als je meer wilt.',
	nonSkiers:
		'Winterwandelpaden vanaf het dorp, rodelbaan bij de [naam] hut, langlaufloipe in het dal, en het zwembad van Saalbach.'
};

export const practical = [
	{
		title: 'Reis vanuit Nederland',
		text: 'Ongeveer 1.000 kilometer via Keulen, Frankfurt, München en Kufstein; met pauzes reken je op tien uur. Vignet voor Oostenrijk online kopen vóór vertrek. Winterbanden zijn verplicht van 1 november tot 15 april.'
	},
	{
		title: 'Aankomst en sleutel',
		text: 'Inchecken vanaf 16:00, uitchecken tot 10:00. De sleutel [ligt in een sleutelkluis / geven we persoonlijk]. Parkeerplaats bij het huis.'
	},
	{
		title: 'Skipas',
		text: 'De skipas voor de Skicircus koop je online of bij het dalstation op 250 meter. Prijzen 2026/27: [x] per volwassene per 6 dagen, kinderen [x]. Wij [regelen/regelen niet] de skipas.'
	},
	{
		title: 'Materiaal huren',
		text: 'Twee verhuurwinkels binnen 300 meter. Reserveer online vóór de kerstvakantie en de voorjaarsvakantie; dan staat je materiaal klaar.'
	},
	{
		title: 'Boodschappen',
		text: 'Supermarkt op [x] minuten lopen, open tot [x] uur. Bakker in het dorp vanaf 07:00. Op zondag is bijna alles dicht; koop op zaterdag in.'
	},
	{
		title: 'Inpaklijst',
		text: 'Skipas-hoesje, zonnebrand, lippenbalsem, handschoenen voor de kinderen in tweevoud, pantoffels, een goed boek. Beddengoed en handdoeken liggen klaar.'
	}
];
