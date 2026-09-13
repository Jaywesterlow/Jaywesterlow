<script lang="ts">
	import { ridge } from '$lib/ridge';

	/** Two ridges that carry the page from a light section into a dark one: ice in front of ink. */
	const back = ridge(1440, 150, 110, 4);
	const front = ridge(1440, 175, 70, 7);
</script>

<div class="edge" aria-hidden="true">
	<svg viewBox="0 0 1440 180" preserveAspectRatio="none">
		<path d={back} fill="oklch(0.36 0.06 252)" />
		<path d={front} fill="var(--ink)" />
	</svg>
</div>

<style>
	.edge {
		background: var(--snow);
		line-height: 0;
	}
	svg {
		display: block;
		width: 100%;
		height: clamp(80px, 12vw, 180px);
	}
</style>
