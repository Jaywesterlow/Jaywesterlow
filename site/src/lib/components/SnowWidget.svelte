<script lang="ts">
	import Icon from './Icon.svelte';

	/** Static example. On the real site this reads the daily snow report. */
	const items = [
		{ icon: 'temp', value: '−6 °C', sub: 'dal, 08:00' },
		{ icon: 'snow', value: '85 cm', sub: 'sneeuw op de berg' },
		{ icon: 'lift', value: '68 / 70', sub: 'liften open' },
		{ icon: 'sun', value: 'zon', sub: 'tot 15:00' }
	];
</script>

<div class="widget">
	<div class="head">
		<span class="label">Vandaag in Hinterglemm</span>
		<span class="src">bron: saalbach.com · voorbeeld</span>
	</div>
	<div class="cells">
		{#each items as it (it.icon)}
			<div class="cell">
				<Icon name={it.icon} />
				<b>{it.value}</b>
				<span class="sub">{it.sub}</span>
			</div>
		{/each}
	</div>
</div>

<style>
	.widget {
		display: flex;
		flex-direction: column;
		gap: 14px;
		padding: 18px 20px;
		border-radius: var(--r-card);
		background: oklch(0.24 0.05 255 / 0.45);
		border: 1px solid oklch(1 0 0 / 0.2);
		backdrop-filter: blur(12px);
		-webkit-backdrop-filter: blur(12px);
		color: var(--snow);
	}
	.head {
		display: flex;
		justify-content: space-between;
		gap: 24px;
	}
	.head .label {
		color: var(--snow);
	}
	.src,
	.sub {
		font-family: var(--font-mono);
		font-size: 0.6875rem;
		color: var(--ice);
	}
	.cells {
		display: flex;
		gap: 28px;
	}
	.cell {
		display: flex;
		flex-direction: column;
		gap: 6px;
		min-width: 96px;
	}
	.cell b {
		font-family: var(--font-display);
		font-size: 1.75rem;
		letter-spacing: -0.02em;
		line-height: 1;
	}
	@media (max-width: 900px) {
		.widget {
			padding: 12px 14px;
			gap: 10px;
		}
		.head {
			display: none;
		}
		.cells {
			gap: 16px;
		}
		.cell {
			min-width: 0;
			flex-direction: row;
			align-items: center;
			gap: 8px;
		}
		.cell b {
			font-size: 1.125rem;
		}
		.cell .sub,
		.cell:nth-child(4) {
			display: none;
		}
	}
</style>
