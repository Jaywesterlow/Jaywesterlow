<script lang="ts">
	import '../app.css';
	import DemoOverlay from '$lib/components/DemoOverlay.svelte';
	import Cursor from '$lib/components/Cursor.svelte';
	import { openDemo } from '$lib/demo.svelte';
	import { DEMO } from '$lib/site';

	let { children } = $props();

	/** Every link to a page that is not built yet opens the demo overlay instead of jumping. */
	function onclick(e: MouseEvent) {
		const a = (e.target as Element | null)?.closest('a');
		if (!a) return;
		if (a.getAttribute('href') === DEMO) {
			e.preventDefault();
			openDemo('link');
		}
	}
</script>

<svelte:document {onclick} />

{@render children()}
<DemoOverlay />
<Cursor />
