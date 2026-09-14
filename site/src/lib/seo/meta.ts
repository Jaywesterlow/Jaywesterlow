import { site } from '$lib/site';
import { apartments, type Apartment } from '$lib/data/apartments';
import type { Faq } from '$lib/data/faq';

export type Meta = {
	title: string;
	description: string;
	path: string;
	image?: string;
	type?: 'website' | 'article';
	/** extra JSON-LD nodes for this page; the shared Organization/WebSite nodes are always added */
	graph?: Record<string, unknown>[];
	noindex?: boolean;
};

const ORG = `${site.url}/#organization`;
const WEBSITE = `${site.url}/#website`;

export function organizationNode() {
	return {
		'@type': ['Organization', 'LodgingBusiness'],
		'@id': ORG,
		name: site.name,
		url: site.url,
		logo: `${site.url}/icon-512.png`,
		image: `${site.url}/og.png`,
		email: site.email,
		telephone: site.phoneE164,
		address: {
			'@type': 'PostalAddress',
			streetAddress: site.address.street,
			postalCode: site.address.postalCode,
			addressLocality: site.address.city,
			addressRegion: site.address.region,
			addressCountry: site.address.country
		},
		geo: { '@type': 'GeoCoordinates', latitude: site.geo.lat, longitude: site.geo.lng },
		sameAs: [site.instagram],
		checkinTime: '16:00',
		checkoutTime: '10:00',
		numberOfRooms: apartments.length,
		areaServed: 'Hinterglemm, Salzburgerland'
	};
}

export function websiteNode() {
	return {
		'@type': 'WebSite',
		'@id': WEBSITE,
		url: site.url,
		name: site.name,
		inLanguage: site.lang,
		publisher: { '@id': ORG }
	};
}

export function webPageNode(m: Meta) {
	return {
		'@type': 'WebPage',
		'@id': `${site.url}${m.path}#webpage`,
		url: `${site.url}${m.path}`,
		name: m.title,
		description: m.description,
		inLanguage: site.lang,
		isPartOf: { '@id': WEBSITE },
		about: { '@id': ORG },
		dateModified: site.buildDate
	};
}

export function breadcrumbNode(items: { name: string; path: string }[]) {
	return {
		'@type': 'BreadcrumbList',
		itemListElement: items.map((it, i) => ({
			'@type': 'ListItem',
			position: i + 1,
			name: it.name,
			item: `${site.url}${it.path}`
		}))
	};
}

export function faqNode(items: Faq[]) {
	return {
		'@type': 'FAQPage',
		mainEntity: items.map((f) => ({
			'@type': 'Question',
			name: f.q,
			acceptedAnswer: { '@type': 'Answer', text: f.a }
		}))
	};
}

export function apartmentNode(a: Apartment) {
	const path = `/appartementen/${a.slug}`;
	return {
		'@type': 'VacationRental',
		'@id': `${site.url}${path}#rental`,
		name: `${site.name} · ${a.name}`,
		url: `${site.url}${path}`,
		description: a.summary,
		image: a.photos.map((p) => `${site.url}/img/${p.key}-1600.webp`),
		containedInPlace: { '@id': ORG },
		occupancy: { '@type': 'QuantitativeValue', maxValue: a.sleepsMax, unitCode: 'C62' },
		floorSize: { '@type': 'QuantitativeValue', value: a.area, unitCode: 'MTK' },
		numberOfBedrooms: a.bedrooms,
		numberOfBathroomsTotal: a.bathrooms,
		amenityFeature: [...a.included, ...a.amenities].map((name) => ({
			'@type': 'LocationFeatureSpecification',
			name,
			value: true
		})),
		offers: {
			'@type': 'Offer',
			priceCurrency: 'EUR',
			price: a.price.low,
			priceSpecification: {
				'@type': 'UnitPriceSpecification',
				priceCurrency: 'EUR',
				minPrice: a.price.low,
				maxPrice: a.price.high,
				unitText: 'week'
			},
			availability: 'https://schema.org/InStock',
			url: `${site.url}${path}`
		}
	};
}

export function buildGraph(m: Meta) {
	return {
		'@context': 'https://schema.org',
		'@graph': [organizationNode(), websiteNode(), webPageNode(m), ...(m.graph ?? [])]
	};
}
