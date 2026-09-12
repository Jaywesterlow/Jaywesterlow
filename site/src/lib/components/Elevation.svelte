<script lang="ts">
	import { reveal } from '$lib/scroll';

	/** Height profile from the front door to the top station. Heights marked [verifiëren] in the copy. */
	const W = 700;
	const H = 340;
	const pts: [number, number][] = [
		[0, 1060],
		[300, 1070],
		[600, 1140],
		[900, 1240],
		[1200, 1360],
		[1500, 1470],
		[1800, 1580],
		[2100, 1690],
		[2400, 1780],
		[2600, 1820]
	];
	const pl = 60,
		pr = 24,
		pt = 36,
		pb = 48;
	const X = (d: number) => pl + (d / 2600) * (W - pl - pr);
	const Y = (a: number) => pt + (1 - (a - 1000) / 900) * (H - pt - pb);
	const f = (n: number) => n.toFixed(1);
	const line = 'M' + pts.map(([d, a]) => `${f(X(d))},${f(Y(a))}`).join(' L');
	const area = line + ` L${f(X(2600))},${f(Y(1000))} L${f(X(0))},${f(Y(1000))} Z`;
	const walk = `M${f(X(0))},${f(Y(1060))} L${f(X(300))},${f(Y(1070))}`;
	const grid = [1000, 1300, 1600, 1900];
	const xt: [number, string][] = [
		[0, '0 m'],
		[300, '300 m'],
		[1300, '1,3 km'],
		[2600, '2,6 km']
	];

	let hover: { d: number; a: number } | null = $state(null);
	const minutes = (d: number) =>
		d <= 300 ? Math.round(d / 75) : 4 + Math.round(((d - 300) / 2300) * 12);

	function move(e: MouseEvent) {
		const svg = e.currentTarget as SVGSVGElement;
		const r = svg.getBoundingClientRect();
		const x = ((e.clientX - r.left) / r.width) * W;
		const d = Math.max(0, Math.min(2600, ((x - pl) / (W - pl - pr)) * 2600));
		let a = 1060;
		for (let i = 1; i < pts.length; i++) {
			const [d0, a0] = pts[i - 1];
			const [d1, a1] = pts[i];
			if (d <= d1) {
				a = a0 + ((d - d0) / (d1 - d0)) * (a1 - a0);
				break;
			}
		}
		hover = { d: Math.round(d / 10) * 10, a: Math.round(a / 10) * 10 };
	}
</script>

<svg
	viewBox="0 0 {W} {H}"
	class="chart"
	role="img"
	aria-label="Hoogteprofiel van de voordeur tot het bergstation"
	use:reveal
	onmousemove={move}
	onmouseleave={() => (hover = null)}
>
	{#each grid as a (a)}
		<line x1={pl} x2={W - pr} y1={f(Y(a))} y2={f(Y(a))} class="grid" />
		<text x={pl - 8} y={f(Y(a) + 4)} text-anchor="end" class="tick">{a}</text>
	{/each}
	<path d={area} class="area" />
	<path d={line} class="line" pathLength="1" />
	<path d={walk} class="walk" pathLength="1" />
	<circle cx={f(X(0))} cy={f(Y(1060))} r="5" class="dot" />
	<text x={f(X(0) + 8)} y={f(Y(1060) - 40)} class="mark">Huis Hinterglemm · ± 1.060 m</text>
	<circle cx={f(X(300))} cy={f(Y(1070))} r="5" class="dot" />
	<text x={f(X(300) + 14)} y={f(Y(1070) + 26)} class="mark">Reiterkogelbahn · 300 m lopen</text>
	<circle cx={f(X(2600))} cy={f(Y(1820))} r="5" class="dot" />
	<text x={f(X(2600) - 8)} y={f(Y(1820) - 16)} text-anchor="end" class="mark"
		>Bergstation · ± 1.820 m</text
	>
	{#each xt as [d, lbl] (d)}
		<text x={f(X(d))} y={H - pb + 18} text-anchor="middle" class="tick">{lbl}</text>
	{/each}
	{#if hover}
		<line x1={f(X(hover.d))} x2={f(X(hover.d))} y1={pt} y2={H - pb} class="cursor" />
		<circle cx={f(X(hover.d))} cy={f(Y(hover.a))} r="6" class="dot hot" />
		<g transform="translate({f(Math.min(X(hover.d) + 12, W - 170))},{pt + 4})">
			<rect width="160" height="44" rx="4" class="tip" />
			<text x="10" y="18" class="tipa">{hover.a} m</text>
			<text x="10" y="35" class="tipb">
				{hover.d < 1000 ? `${hover.d} m` : `${(hover.d / 1000).toFixed(1).replace('.', ',')} km`} · {hover.d <=
				300
					? `${minutes(hover.d)} min lopen`
					: `${minutes(hover.d)} min in de gondel`}
			</text>
		</g>
	{/if}
</svg>

<style>
	.chart {
		width: 100%;
		height: auto;
		overflow: visible;
	}
	.grid {
		stroke: var(--stone);
		stroke-width: 1;
	}
	.tick {
		font-family: var(--font-label);
		font-weight: 500;
		font-size: 12px;
		fill: var(--stone-2);
	}
	.area {
		fill: var(--glacier);
		opacity: 0;
		transition: opacity var(--t-reveal, 700ms) var(--ease-out) 900ms;
	}
	.line {
		fill: none;
		stroke: var(--piste);
		stroke-width: 2;
		stroke-linejoin: round;
		stroke-dasharray: 1;
		stroke-dashoffset: 1;
		transition: stroke-dashoffset var(--t-draw) var(--ease-out) 300ms;
	}
	.walk {
		fill: none;
		stroke: var(--ink);
		stroke-width: 4;
		stroke-linecap: round;
		stroke-dasharray: 1;
		stroke-dashoffset: 1;
		transition: stroke-dashoffset 500ms var(--ease-out);
	}
	.chart:global(.in) .line,
	.chart:global(.in) .walk {
		stroke-dashoffset: 0;
	}
	.chart:global(.in) .area {
		opacity: 1;
	}
	.dot {
		fill: var(--snow);
		stroke: var(--piste);
		stroke-width: 2;
	}
	.dot.hot {
		fill: var(--piste);
	}
	.mark {
		font-family: var(--font-body);
		font-size: 14px;
		font-weight: 600;
		fill: var(--ink);
	}
	.cursor {
		stroke: var(--ink);
		stroke-width: 1;
		stroke-dasharray: 3 4;
	}
	.tip {
		fill: var(--ink);
	}
	.tipa {
		font-family: var(--font-display);
		font-size: 15px;
		font-weight: 700;
		fill: var(--snow);
	}
	.tipb {
		font-family: var(--font-label);
		font-weight: 500;
		font-size: 11px;
		fill: var(--ice);
	}
	@media (max-width: 700px) {
		.mark {
			font-size: 17px;
		}
		.tick {
			font-size: 14px;
		}
	}
</style>
