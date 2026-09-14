<script lang="ts">
	import { demo, closeDemo } from '$lib/demo.svelte';
	import Icon from './Icon.svelte';
	import { DEMO_CONTACT } from '$lib/site';
	import { freezePage } from '$lib/freeze';

	let dialog: HTMLDialogElement | undefined = $state();

	let frozen = false;
	$effect(() => {
		if (!dialog) return;
		if (demo.open && !dialog.open) {
			dialog.showModal();
			freezePage(true);
			frozen = true;
		}
		if (!demo.open && dialog.open) dialog.close();
	});

	function onclose() {
		if (frozen) freezePage(false);
		frozen = false;
		closeDemo();
	}

	const text = $derived(
		demo.kind === 'form'
			? 'In de demo wordt het formulier niet verstuurd. Op de echte site komt de aanvraag binnen per e-mail en WhatsApp, met een bevestiging voor de gast.'
			: 'Deze pagina is een voorstel voor Huis Hinterglemm: logo, website en content, gemaakt door Jaymar Westerlow. De links werken nog niet. Klik hieronder om verder te kijken.'
	);
</script>

<dialog bind:this={dialog} class="demo" {onclose} aria-labelledby="demo-title">
	<img class="bg" src="/img/hero-piste-800.webp" alt="" loading="lazy" />
	<div class="scrim"></div>
	<div class="inner">
		<img src="/brand/mark-white.svg" alt="" width="72" height="72" class="mark" />
		<h2 id="demo-title">Dit is een demo.</h2>
		<p>{text}</p>
		<div class="actions">
			<button type="button" class="btn primary" onclick={closeDemo}
				>Verder kijken <Icon name="arrow" size={18} /></button
			>
			{#if DEMO_CONTACT}<a href={DEMO_CONTACT} class="btn secondary">Neem contact op met Jaymar</a
				>{/if}
		</div>
	</div>
</dialog>

<style>
	.demo {
		border: 0;
		padding: 0;
		width: 100vw;
		height: 100vh;
		max-width: none;
		max-height: none;
		background: var(--ink);
		color: var(--snow);
		overflow: hidden;
	}
	.demo::backdrop {
		background: transparent;
	}
	.demo[open] {
		animation: fade 320ms var(--ease-out);
	}
	@keyframes fade {
		from {
			opacity: 0;
		}
	}
	.bg {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		object-fit: cover;
		/* a small source scaled up is already soft, so a 3px blur is enough and costs a third */
		filter: blur(3px) brightness(0.6);
		transform: scale(1.04);
	}
	.scrim {
		position: absolute;
		inset: 0;
		background: oklch(0.24 0.05 255 / 0.55);
	}
	.inner {
		position: absolute;
		inset: 0;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: flex-start;
		gap: 22px;
		max-width: 640px;
		margin: 0 auto;
		padding: var(--gutter);
	}
	.mark {
		width: 72px;
		height: 72px;
	}
	h2 {
		font-size: clamp(2.5rem, 2rem + 3vw, 4rem);
	}
	p {
		font-size: 1.125rem;
		color: var(--ice);
		max-width: 44ch;
	}
	.actions {
		display: flex;
		gap: 12px;
		flex-wrap: wrap;
	}
	.actions .secondary {
		color: var(--snow);
		border-color: var(--snow);
	}
	.actions .secondary:hover {
		color: var(--ice);
		border-color: var(--ice);
	}
</style>
