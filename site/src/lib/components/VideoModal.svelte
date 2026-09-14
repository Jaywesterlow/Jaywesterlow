<script lang="ts">
	import Icon from './Icon.svelte';
	import { freezePage } from '$lib/freeze';

	let { open = $bindable(false) }: { open?: boolean } = $props();
	let dialog: HTMLDialogElement | undefined = $state();
	let video: HTMLVideoElement | undefined = $state();
	/** The file is only requested once someone opens the modal. */
	let src = $state('');

	$effect(() => {
		if (!dialog) return;
		if (open && !dialog.open) {
			src = '/video/huis-hinterglemm-720.mp4';
			dialog.showModal();
			freezePage(true);
			video?.play().catch(() => {});
		}
		if (!open && dialog.open) dialog.close();
	});

	function close() {
		video?.pause();
		if (video) video.currentTime = 0;
		if (open) freezePage(false);
		open = false;
	}
</script>

<dialog bind:this={dialog} class="modal" onclose={close} aria-label="Video: Hinterglemm van boven">
	<button type="button" class="x" onclick={close} aria-label="Sluiten"
		><Icon name="close" size={24} /></button
	>
	<video
		bind:this={video}
		controls
		playsinline
		preload="none"
		poster="/video/poster.webp"
		width="1280"
		height="720"
	>
		{#if src}<source {src} type="video/mp4" />{/if}
	</video>
	<p class="meta">Beelden en muziek zijn AI-voorbeelden tot er echte opnames zijn.</p>
</dialog>

<style>
	.modal {
		border: 0;
		padding: 0;
		background: var(--ink);
		color: var(--snow);
		border-radius: var(--r-card);
		width: min(92vw, 1120px);
		max-width: none;
		overflow: hidden;
	}
	/* a flat wash, not a blur: blurring the whole page behind the dialog costs more
	   than decoding the video and drops playback to a slideshow */
	.modal::backdrop {
		background: oklch(0.18 0.04 255 / 0.92);
	}
	video {
		display: block;
		width: 100%;
		height: auto;
		background: #000;
	}
	.x {
		position: absolute;
		top: 10px;
		right: 10px;
		z-index: 2;
		border: 0;
		border-radius: 999px;
		width: 40px;
		height: 40px;
		display: inline-flex;
		align-items: center;
		justify-content: center;
		background: oklch(0.24 0.05 255 / 0.7);
		color: var(--snow);
		cursor: pointer;
	}
	.meta {
		padding: 10px 14px;
		font-size: 0.6875rem;
		color: var(--ink-3);
	}
</style>
