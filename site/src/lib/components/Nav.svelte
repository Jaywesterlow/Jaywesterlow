<script lang="ts">
	import { nav, DEMO } from '$lib/site';
	import Icon from './Icon.svelte';
	import { fade } from 'svelte/transition';

	let open = $state(false);
</script>

<header class="nav">
	<a href="#top" class="logo" aria-label="Huis Hinterglemm, naar boven">
		<img src="/brand/lockup.svg" alt="Huis Hinterglemm" width="569" height="112" />
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
		position: absolute;
		inset: 0 0 auto 0;
		z-index: 10;
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: var(--s-5);
		padding: 22px var(--inset);
		color: var(--ink);
	}
	.logo img {
		height: 40px;
		width: auto;
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
		:global(.hero.mobile-dark) .nav {
			color: var(--snow);
		}
	}
</style>
