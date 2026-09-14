<script lang="ts">
	const paths: Record<string, string> = {
		temp: '<path d="M10 4a2 2 0 0 1 4 0v9.5a4 4 0 1 1-4 0z"/><path d="M12 9v6"/>',
		snow: '<path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9M12 3l-2.5 2.5M12 3l2.5 2.5M12 21l-2.5-2.5M12 21l2.5-2.5"/>',
		lift: '<path d="M3 5l18 4"/><path d="M12 7v5"/><rect x="8" y="12" width="8" height="7" rx="1.5"/><path d="M8 15.5h8"/>',
		sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
		car: '<path d="M3 13l2-5a2 2 0 0 1 1.9-1.3h10.2A2 2 0 0 1 19 8l2 5v5H3z"/><circle cx="7.5" cy="16.5" r="1.5"/><circle cx="16.5" cy="16.5" r="1.5"/><path d="M3 13h18"/>',
		key: '<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3M15 12v2"/>',
		ticket:
			'<path d="M3 8a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v2a2 2 0 0 0 0 4v2a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-2a2 2 0 0 0 0-4z"/><path d="M13 6v12"/>',
		ski: '<path d="M4 20l16-6M6 4l4 3-1 5 4 3 1 5"/><circle cx="14" cy="5" r="1.5"/>',
		cart: '<path d="M3 4h2l2.4 11h11.2L21 8H7"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
		bag: '<path d="M5 8h14l-1 12H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
		play: '<path d="M7 4l12 8-12 8z"/>',
		wa: '<path d="M4 20l1.5-4.2A8 8 0 1 1 8.6 19z"/><path d="M9 9.5c.3 2.5 2.4 4.6 5 5l1.4-1.4-1.9-.9-.9.7c-.8-.4-1.5-1.1-1.9-1.9l.7-.9-.9-1.9z"/>',
		mail: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
		plus: '<path d="M12 5v14M5 12h14"/>',
		arrow: '<path d="M5 12h14M13 6l6 6-6 6"/>',
		space:
			'<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/><rect x="9" y="9" width="6" height="6" rx="1"/>',
		check: '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.5 2.5L16 9.5"/>',
		menu: '<path d="M4 7h16M4 12h16M4 17h16"/>',
		close: '<path d="M6 6l12 12M18 6L6 18"/>'
	};

	let { name, size = 22 }: { name: keyof typeof paths | string; size?: number } = $props();
</script>

<!-- eslint-disable svelte/no-at-html-tags -- static path data from the map above -->
<svg
	class="ico"
	viewBox="0 0 24 24"
	style:width="{size}px"
	style:height="{size}px"
	aria-hidden="true">{@html paths[name] ?? ''}</svg
>
