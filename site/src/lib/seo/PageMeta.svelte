<script lang="ts">
	import { site } from '$lib/site';
	import { buildGraph, type Meta } from './meta';

	let { meta }: { meta: Meta } = $props();

	const url = $derived(`${site.url}${meta.path}`);
	const image = $derived(`${site.url}${meta.image ?? '/og.png'}`);
	const jsonld = $derived(
		'<script type="application/ld+json">' +
			JSON.stringify(buildGraph(meta)).replace(/</g, '\\u003c') +
			'</' +
			'script>'
	);
</script>

<svelte:head>
	<title>{meta.title}</title>
	<meta name="description" content={meta.description} />
	<link rel="canonical" href={url} />
	<link rel="alternate" hreflang="nl" href={url} />
	<link rel="alternate" hreflang="x-default" href={url} />
	{#if meta.noindex}<meta name="robots" content="noindex, nofollow" />{/if}
	<meta property="og:type" content={meta.type ?? 'website'} />
	<meta property="og:site_name" content={site.name} />
	<meta property="og:locale" content={site.locale} />
	<meta property="og:title" content={meta.title} />
	<meta property="og:description" content={meta.description} />
	<meta property="og:url" content={url} />
	<meta property="og:image" content={image} />
	<meta name="twitter:card" content="summary_large_image" />
	<!-- eslint-disable-next-line svelte/no-at-html-tags -- JSON-LD is serialised with < escaped -->
	{@html jsonld}
</svelte:head>
