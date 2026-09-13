/**
 * Lens tilt: the element rotates a few degrees toward the pointer and a soft
 * highlight follows it (`--mx`, `--my` in %). Off for coarse pointers and reduced motion.
 */
export function tilt(node: HTMLElement, opts: { max?: number; scale?: number } = {}) {
	const max = opts.max ?? 6;
	const scale = opts.scale ?? 1.015;
	if (
		typeof matchMedia === 'undefined' ||
		!matchMedia('(pointer: fine)').matches ||
		matchMedia('(prefers-reduced-motion: reduce)').matches
	)
		return {};
	node.style.transformStyle = 'preserve-3d';
	let raf = 0;
	let target = { rx: 0, ry: 0, s: 1, mx: 50, my: 50 };
	const cur = { ...target };
	const paint = () => {
		raf = 0;
		let moving = false;
		for (const k of Object.keys(cur) as (keyof typeof cur)[]) {
			const d = target[k] - cur[k];
			if (Math.abs(d) > 0.01) moving = true;
			cur[k] += d * 0.16;
		}
		node.style.transform = `perspective(900px) rotateX(${cur.rx.toFixed(2)}deg) rotateY(${cur.ry.toFixed(2)}deg) scale(${cur.s.toFixed(3)})`;
		node.style.setProperty('--mx', `${cur.mx.toFixed(1)}%`);
		node.style.setProperty('--my', `${cur.my.toFixed(1)}%`);
		if (moving) raf = requestAnimationFrame(paint);
	};
	const schedule = () => {
		if (!raf) raf = requestAnimationFrame(paint);
	};
	const move = (e: PointerEvent) => {
		const r = node.getBoundingClientRect();
		const px = (e.clientX - r.left) / r.width;
		const py = (e.clientY - r.top) / r.height;
		target = {
			rx: (0.5 - py) * max * 2,
			ry: (px - 0.5) * max * 2,
			s: scale,
			mx: px * 100,
			my: py * 100
		};
		schedule();
	};
	const leave = () => {
		target = { rx: 0, ry: 0, s: 1, mx: 50, my: 50 };
		schedule();
	};
	node.addEventListener('pointermove', move);
	node.addEventListener('pointerleave', leave);
	return {
		destroy() {
			node.removeEventListener('pointermove', move);
			node.removeEventListener('pointerleave', leave);
			if (raf) cancelAnimationFrame(raf);
		}
	};
}
