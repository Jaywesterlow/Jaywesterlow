<script lang="ts">
	import { reveal } from '$lib/scroll';

	/** Drive from the Netherlands. Utrecht is the example start; swap for the client's own reference town. */
	const stops: [number, string, string][] = [
		[30, 'Utrecht', '0 km'],
		[160, 'Keulen', '230 km'],
		[290, 'Frankfurt', '420 km'],
		[440, 'München', '830 km'],
		[560, 'Kufstein', '920 km'],
		[670, 'Hinterglemm', '1.000 km']
	];
	const anchor = (i: number) => (i === 0 ? 'start' : i === stops.length - 1 ? 'end' : 'middle');
	const end = (i: number) => i === 0 || i === stops.length - 1;
</script>

<svg
	viewBox="0 0 700 124"
	class="route"
	role="img"
	aria-label="Route van Utrecht naar Hinterglemm"
	use:reveal
>
	<line x1="30" y1="70" x2="670" y2="70" class="base" />
	<line x1="30" y1="70" x2="670" y2="70" class="dash" pathLength="1" />
	{#each stops as [x, name, dist], i (name)}
		<circle cx={x} cy="70" r={end(i) ? 7 : 5} class:end={end(i)} class="stop" style:--i={i} />
		<text {x} y={i % 2 === 0 ? 50 : 100} text-anchor={anchor(i)} class="name" class:strong={end(i)}
			>{name}</text
		>
		<text {x} y={i % 2 === 0 ? 36 : 114} text-anchor={anchor(i)} class="dist">{dist}</text>
	{/each}
</svg>

<style>
	.route {
		width: 100%;
		height: auto;
		overflow: visible;
	}
	.base {
		stroke: var(--stone);
		stroke-width: 2;
	}
	.dash {
		stroke: var(--piste);
		stroke-width: 3;
		stroke-dasharray: 0.009 0.012;
		stroke-dashoffset: 0;
		opacity: 0;
		transition: opacity 400ms var(--ease-out);
	}
	.route:global(.in) .dash {
		opacity: 1;
		animation: ride 1400ms var(--ease-out);
	}
	@keyframes ride {
		from {
			stroke-dasharray: 0 1;
		}
		to {
			stroke-dasharray: 0.009 0.012;
		}
	}
	.stop {
		fill: var(--snow);
		stroke: var(--ink);
		stroke-width: 2;
	}
	.stop.end {
		fill: var(--ink);
	}
	.name {
		font-family: var(--font-body);
		font-size: 13px;
		font-weight: 500;
		fill: var(--ink);
	}
	.name.strong {
		font-weight: 700;
	}
	.dist {
		font-family: var(--font-label);
		font-weight: 500;
		font-size: 11px;
		fill: var(--stone-2);
	}
	@media (max-width: 700px) {
		.name {
			font-size: 16px;
		}
		.dist {
			font-size: 13px;
		}
	}
</style>
