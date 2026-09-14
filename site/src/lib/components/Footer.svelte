<script lang="ts">
	import { site, DEMO } from '$lib/site';
	import { apartments } from '$lib/data/apartments';
	import { ridge } from '$lib/ridge';

	/** Seven layered ridges; the last one is the footer colour so the content sits on ink. */
	const layers: [number, number, string][] = [
		[300, 150, 'oklch(0.90 0.045 228)'],
		[330, 140, 'oklch(0.82 0.07 225)'],
		[365, 130, 'oklch(0.68 0.08 235)'],
		[400, 120, 'oklch(0.52 0.08 245)'],
		[440, 105, 'oklch(0.38 0.06 252)'],
		[480, 90, 'oklch(0.30 0.05 255)'],
		[520, 80, 'oklch(0.24 0.05 255)']
	];
	const desktop = layers.map(([b, a, c], i) => ({ d: ridge(1440, b, a, i * 3 + 1), c }));
	const mobile = layers.map(([b, a, c], i) => ({
		d: ridge(390, b * 0.9 + 40, a * 0.75, i * 3 + 1),
		c
	}));
	const year = new Date().getFullYear();
</script>

<footer class="footer" id="contact-footer">
	<svg viewBox="0 0 1440 760" preserveAspectRatio="none" class="ridges desktop" aria-hidden="true">
		<defs
			><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"
				><stop offset="0" stop-color="oklch(0.93 0.035 228)" /><stop
					offset="0.28"
					stop-color="oklch(0.985 0.004 240)"
				/></linearGradient
			></defs
		>
		<rect width="1440" height="760" fill="url(#sky)" />
		{#each desktop as l, i (i)}<path d={l.d} fill={l.c} />{/each}
	</svg>
	<svg viewBox="0 0 390 900" preserveAspectRatio="none" class="ridges mobile" aria-hidden="true">
		<defs
			><linearGradient id="sky-m" x1="0" y1="0" x2="0" y2="1"
				><stop offset="0" stop-color="oklch(0.93 0.035 228)" /><stop
					offset="0.22"
					stop-color="oklch(0.985 0.004 240)"
				/></linearGradient
			></defs
		>
		<rect width="390" height="900" fill="url(#sky-m)" />
		{#each mobile as l, i (i)}<path d={l.d} fill={l.c} />{/each}
	</svg>

	<div class="top">
		<span class="label">Nog vragen?</span>
		<h2>Stuur een WhatsApp. Je hoort binnen 24 uur van ons.</h2>
	</div>

	<div class="content dark">
		<div class="cols">
			<div class="brand">
				<img src="/brand/lockup-white.svg" alt="Huis Hinterglemm" width="569" height="112" />
				<p>
					Vier appartementen in Hinterglemm, verhuurd door Nederlandse eigenaren. Vragen? Stuur een
					WhatsApp, je hoort binnen 24 uur van ons.
				</p>
			</div>
			<div class="col">
				<span class="label">Appartementen</span>
				{#each apartments as a (a.slug)}<a href={DEMO}>{a.name} · {a.sleeps} pers.</a>{/each}
			</div>
			<div class="col">
				<span class="label">Info</span>
				<a href="#skigebied">Skigebied</a><a href="#praktisch">Praktisch</a><a href="#prijzen"
					>Prijzen</a
				><a href="#over-ons">Over ons</a>
			</div>
			<div class="col">
				<span class="label">Contact</span>
				<a href={DEMO}>{site.phoneDisplay}</a><a href={DEMO}>{site.email}</a><a href={DEMO}
					>Instagram</a
				>
			</div>
		</div>
		<div class="legal meta">
			<span>© {year} {site.name} · {site.kvk}</span>
			<span
				><a href={DEMO}>Privacy</a> · <a href={DEMO}>Huisregels</a> ·
				<a href={DEMO}>Voorwaarden</a></span
			>
		</div>
	</div>
</footer>

<style>
	.footer {
		position: relative;
		overflow: hidden;
		min-height: 880px;
		display: flex;
		flex-direction: column;
		justify-content: space-between;
	}
	.ridges {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
	}
	.ridges.mobile {
		display: none;
	}
	.top {
		position: relative;
		display: flex;
		flex-direction: column;
		gap: 12px;
		padding: 40px var(--inset) 0;
	}
	.top h2 {
		font-size: clamp(2rem, 1.5rem + 2vw, 3rem);
		max-width: 16ch;
	}
	.content {
		position: relative;
		background: transparent;
		display: flex;
		flex-direction: column;
		gap: 28px;
		padding: 300px var(--inset) 32px;
	}
	.cols {
		display: grid;
		grid-template-columns: 2fr 1fr 1fr 1fr;
		gap: 32px;
	}
	.brand {
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		gap: 12px;
	}
	.brand img {
		height: 40px;
		width: auto;
	}
	.brand p {
		max-width: 38ch;
		font-size: var(--fs-small);
		color: var(--ink-3);
	}
	.col {
		display: flex;
		flex-direction: column;
		gap: 8px;
		font-size: var(--fs-small);
	}
	.col .label {
		color: var(--ink-3);
	}
	.col a:hover {
		color: var(--ice);
	}
	.legal {
		border-top: 1px solid oklch(0.36 0.05 255);
		padding-top: 16px;
		display: flex;
		justify-content: space-between;
		gap: 16px;
		flex-wrap: wrap;
		font-size: 0.6875rem;
		color: var(--ink-3);
	}
	@media (max-width: 900px) {
		.footer {
			min-height: 1000px;
		}
		.ridges.desktop {
			display: none;
		}
		.ridges.mobile {
			display: block;
		}
		.top {
			padding-top: 48px;
		}
		.content {
			padding-top: 200px;
		}
		.cols {
			grid-template-columns: 1fr 1fr;
			gap: 24px;
		}
		.brand {
			grid-column: 1 / -1;
		}
		.brand img {
			height: 34px;
		}
	}
</style>
