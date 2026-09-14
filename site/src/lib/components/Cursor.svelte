<script lang="ts">
	import { onMount } from 'svelte';

	/**
	 * Themed cursor: a small dot with a ring that eases after the pointer.
	 * Elements can set data-cursor="play" | "view" | "drag" for a labelled state;
	 * links and buttons grow the ring. Only on fine pointers without reduced motion.
	 */
	let el: HTMLDivElement | undefined = $state();
	/* a modal <dialog> paints in the top layer, above any z-index; the cursor joins it as a popover */
	let topLayer = $state(false);
	let active = $state(false);
	let mode = $state<'default' | 'link' | 'label' | 'hidden'>('hidden');
	let label = $state('');

	const labels: Record<string, string> = { play: 'Afspelen', view: 'Bekijk', chart: 'Hoogte' };

	onMount(() => {
		const fine = matchMedia('(pointer: fine)').matches;
		const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
		if (!fine || reduced) return;
		active = true;
		document.documentElement.classList.add('custom-cursor');

		const supported = typeof HTMLElement !== 'undefined' && 'showPopover' in HTMLElement.prototype;
		const anyDialog = () => !!document.querySelector('dialog[open]');
		/** Re-enter the top layer so the cursor sits above a dialog that just opened. */
		const raise = () => {
			if (!el) return;
			if (!supported) {
				/* no popover support: fall back to the native cursor while a dialog is open */
				document.documentElement.classList.toggle('custom-cursor', !anyDialog());
				return;
			}
			try {
				if (topLayer) el.hidePopover();
				el.showPopover();
				topLayer = true;
			} catch {
				topLayer = false;
			}
		};
		const dialogs = new MutationObserver(raise);
		dialogs.observe(document.body, { attributes: true, attributeFilter: ['open'], subtree: true });
		queueMicrotask(raise);

		let x = innerWidth / 2,
			y = innerHeight / 2,
			rx = x,
			ry = y,
			raf = 0;
		const tick = () => {
			rx += (x - rx) * 0.22;
			ry += (y - ry) * 0.22;
			if (el) {
				el.style.setProperty('--x', `${x}px`);
				el.style.setProperty('--y', `${y}px`);
				el.style.setProperty('--rx', `${rx}px`);
				el.style.setProperty('--ry', `${ry}px`);
			}
			raf = requestAnimationFrame(tick);
		};
		raf = requestAnimationFrame(tick);

		const classify = (t: Element | null) => {
			const tagged = t?.closest<HTMLElement>('[data-cursor]');
			if (tagged) {
				label = labels[tagged.dataset.cursor ?? ''] ?? tagged.dataset.cursor ?? '';
				mode = 'label';
				return;
			}
			mode = t?.closest('a, button, [role="button"], input, select, textarea, label')
				? 'link'
				: 'default';
		};
		const move = (e: PointerEvent) => {
			x = e.clientX;
			y = e.clientY;
			classify(e.target as Element | null);
		};
		/* the page can scroll under a resting pointer; re-read what is beneath it */
		const scroll = () => {
			if (mode !== 'hidden') classify(document.elementFromPoint(x, y));
		};
		const leave = () => (mode = 'hidden');
		const enter = () => (mode = 'default');
		addEventListener('pointermove', move, { passive: true });
		addEventListener('scroll', scroll, { passive: true });
		document.documentElement.addEventListener('mouseleave', leave);
		document.documentElement.addEventListener('mouseenter', enter);
		return () => {
			dialogs.disconnect();
			cancelAnimationFrame(raf);
			removeEventListener('pointermove', move);
			removeEventListener('scroll', scroll);
			document.documentElement.removeEventListener('mouseleave', leave);
			document.documentElement.removeEventListener('mouseenter', enter);
			document.documentElement.classList.remove('custom-cursor');
		};
	});
</script>

{#if active}
	<div
		bind:this={el}
		class="cursor {mode}"
		class:top={topLayer}
		popover="manual"
		aria-hidden="true"
	>
		<span class="dot"></span>
		<span class="ring"
			>{#if mode === 'label'}<span class="text">{label}</span>{/if}</span
		>
	</div>
{/if}

<style>
	.cursor {
		position: fixed;
		inset: 0;
		z-index: 1000;
		pointer-events: none;
		/* reset the popover defaults so the layer stays a transparent full-screen overlay */
		margin: 0;
		padding: 0;
		border: 0;
		width: 100%;
		height: 100%;
		max-width: none;
		max-height: none;
		background: transparent;
		overflow: visible;
	}
	.cursor:not(.top) {
		display: block;
	}
	.cursor::backdrop {
		background: transparent;
	}
	.dot,
	.ring {
		position: absolute;
		top: 0;
		left: 0;
		border-radius: 999px;
		will-change: transform;
	}
	.dot {
		width: 7px;
		height: 7px;
		background: var(--ink);
		box-shadow: 0 0 0 1.5px oklch(1 0 0 / 0.9);
		transform: translate(calc(var(--x, -100px) - 50%), calc(var(--y, -100px) - 50%));
		transition: opacity var(--t-fast) var(--ease-out);
	}
	.ring {
		width: 36px;
		height: 36px;
		border: 1.5px solid var(--ink);
		/* white halo outside and inside the navy ring: visible on white, glacier and ink alike */
		box-shadow:
			0 0 0 1.5px oklch(1 0 0 / 0.85),
			inset 0 0 0 1.5px oklch(1 0 0 / 0.85);
		display: inline-flex;
		align-items: center;
		justify-content: center;
		transform: translate(calc(var(--rx, -100px) - 50%), calc(var(--ry, -100px) - 50%)) scale(1);
		transition:
			width 320ms var(--ease-out),
			height 320ms var(--ease-out),
			background 320ms var(--ease-out),
			border-color 320ms var(--ease-out),
			opacity var(--t-fast) var(--ease-out);
	}
	.hidden .dot,
	.hidden .ring {
		opacity: 0;
	}
	.link .ring {
		width: 52px;
		height: 52px;
		background: oklch(0.56 0.16 250 / 0.18);
	}
	.link .dot {
		opacity: 0;
	}
	.label .dot {
		opacity: 0;
	}
	.label .ring {
		width: 84px;
		height: 84px;
		background: var(--piste);
		border-color: var(--piste);
		box-shadow: 0 0 0 1.5px oklch(1 0 0 / 0.85);
	}
	.text {
		color: #fff;
		font-family: var(--font-label);
		font-weight: 700;
		font-size: 0.75rem;
		letter-spacing: 0.08em;
		text-transform: uppercase;
	}
</style>
