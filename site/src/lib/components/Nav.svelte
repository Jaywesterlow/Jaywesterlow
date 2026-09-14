<script lang="ts">
	import { nav, DEMO } from '$lib/site';
	import Icon from './Icon.svelte';
	import { fade } from 'svelte/transition';

	let open = $state(false);
	let y = $state(0);
	let last = 0;
	let hidden = $state(false);
	const scrolled = $derived(y > 40);

	/* hide while scrolling down, show again on the first scroll up; always visible near the top */
	$effect(() => {
		const dy = y - last;
		if (y < 120) hidden = false;
		else if (dy > 4) hidden = true;
		else if (dy < -4) hidden = false;
		last = y;
	});
</script>

<svelte:window bind:scrollY={y} />

<header class="nav" class:scrolled class:hidden={hidden && !open} class:open>
	<a href="#top" class="logo" aria-label="Huis Hinterglemm, naar boven">
		<img class="ink" src="/brand/lockup.svg" alt="Huis Hinterglemm" width="569" height="112" />
		<img class="white" src="/brand/lockup-white.svg" alt="" width="569" height="112" />
	</a>
	<nav class="links" aria-label="Hoofdmenu">
		{#each nav as item (item.href)}
			<a href={item.href}>{item.label}</a>
		{/each}
	</nav>
	<a href={DEMO} class="btn primary sm cta">Beschikbaarheid</a>
	<button
		class="burger"
		type="button"
		aria-expanded={open}
		aria-controls="menu"
		onclick={() => (open = !open)}
	>
		<span class="sr">Menu</span>
		<Icon name={open ? 'close' : 'menu'} size={26} />
	</button>
</header>

{#if open}
	<div id="menu" class="menu dark" transition:fade={{ duration: 220 }}>
		<nav aria-label="Menu">
			{#each nav as item (item.href)}
				<a href={item.href} onclick={() => (open = false)}>{item.label}</a>
			{/each}
		</nav>
		<a href={DEMO} class="btn primary" onclick={() => (open = false)}>Bekijk beschikbaarheid</a>
	</div>
{/if}

<style>
	.nav {
		position: fixed;
		inset: 0 0 auto 0;
		z-index: 40;
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: var(--s-5);
		padding: 22px var(--inset);
		color: var(--ink);
		background: transparent;
		border-bottom: 1px solid transparent;
		transition:
			transform 480ms var(--ease-out),
			background var(--t-base) var(--ease-out),
			padding var(--t-base) var(--ease-out),
			border-color var(--t-base) var(--ease-out),
			color var(--t-base) var(--ease-out);
	}
	.nav.scrolled {
		background: oklch(0.985 0.004 240 / 0.94);
		backdrop-filter: blur(10px);
		-webkit-backdrop-filter: blur(10px);
		border-bottom-color: var(--stone);
		padding-block: 14px;
	}
	.nav.hidden {
		transform: translateY(-100%);
	}
	.logo {
		display: inline-flex;
	}
	.logo img {
		height: 40px;
		width: auto;
	}
	.logo .white {
		display: none;
	}
	.links {
		display: flex;
		gap: 32px;
		font-weight: 500;
	}
	.links a:hover {
		color: var(--piste);
	}
	.menu nav a,
	.links a {
		transition: color var(--t-fast) var(--ease-out);
	}
	.burger {
		display: none;
		background: none;
		border: 0;
		padding: 6px;
		color: inherit;
		cursor: pointer;
	}
	.sr {
		position: absolute;
		width: 1px;
		height: 1px;
		overflow: hidden;
		clip: rect(0 0 0 0);
	}
	.menu {
		position: fixed;
		inset: 0;
		z-index: 9;
		display: flex;
		flex-direction: column;
		justify-content: flex-end;
		gap: var(--s-6);
		padding: 96px var(--inset) 48px;
	}
	.menu nav {
		display: flex;
		flex-direction: column;
		gap: var(--s-4);
		font-family: var(--font-display);
		font-size: 2.25rem;
		font-weight: 700;
		letter-spacing: -0.03em;
	}
	@media (max-width: 900px) {
		.links,
		.cta {
			display: none;
		}
		.burger {
			display: inline-flex;
			position: relative;
			z-index: 11;
		}
		.nav {
			padding: 18px var(--inset);
		}
		.logo img {
			height: 34px;
		}
	}
	@media (max-width: 900px) {
		/* over the dark mobile hero the bar is white on the photo; on the white bar it goes back to ink */
		.nav:not(.scrolled):not(.open) {
			color: var(--snow);
		}
		.nav:not(.scrolled):not(.open) .logo .ink {
			display: none;
		}
		.nav:not(.scrolled):not(.open) .logo .white {
			display: block;
		}
		.nav.open {
			color: var(--snow);
		}
		.nav.open .logo .ink {
			display: none;
		}
		.nav.open .logo .white {
			display: block;
		}
	}
</style>
