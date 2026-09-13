/** Jagged mountain ridge as an SVG path, closed at the bottom. Shared by the footer and the section edge. */
export function ridge(w: number, base: number, amp: number, seed: number, depth = 400) {
	const pts: string[] = [];
	let first = '';
	for (let x = 0; x <= w + 24; x += 24) {
		const t = x / w;
		const v =
			Math.sin(t * 9 * Math.PI + seed) * 0.5 +
			Math.sin(t * 23 * Math.PI + seed * 1.7) * 0.3 +
			Math.sin(t * 51 * Math.PI + seed * 2.3) * 0.2;
		const jag = ((x * 7919 + seed * 104729) % 97) / 97 - 0.5;
		const y = base - amp * (0.55 + 0.45 * v) - jag * amp * 0.18;
		if (!first) first = y.toFixed(1);
		pts.push(`L${x},${y.toFixed(1)}`);
	}
	return `M0,${w + depth} L0,${first} ${pts.join(' ')} L${w},${w + depth} Z`;
}
