/**
 * Scroll progress as a CSS variable. Sets `--p` (0..1) on the node.
 *
 * mode 'enter': 0 when the top of the node reaches the bottom of the viewport, 1 when it reaches the top.
 * mode 'leave': 0 when the bottom of the node is at the bottom of the viewport, 1 when it leaves at the top.
 * mode 'pin':   for tall sections with a sticky child: 0 when the top hits the viewport top,
 *               1 when the bottom hits the viewport bottom.
 * mode 'page':  0 at scrollY 0, 1 at scrollY = distance (fraction of viewport height).
 *
 * With reduced motion, `--p` is fixed at `rest` and nothing listens to scroll.
 */
export type ProgressOptions = {
	mode?: 'enter' | 'leave' | 'pin' | 'page';
	distance?: number;
	rest?: number;
};

const reduced = () =>
	typeof matchMedia !== 'undefined' && matchMedia('(prefers-reduced-motion: reduce)').matches;

export function progress(node: HTMLElement | SVGElement, opts: ProgressOptions = {}) {
	const mode = opts.mode ?? 'enter';
	if (reduced()) {
		node.style.setProperty('--p', String(opts.rest ?? 1));
		return {};
	}
	let raf = 0;
	const clamp = (v: number) => (v < 0 ? 0 : v > 1 ? 1 : v);
	const compute = () => {
		raf = 0;
		const vh = window.innerHeight;
		let p: number;
		if (mode === 'page') {
			p = window.scrollY / (vh * (opts.distance ?? 0.7));
		} else {
			const r = node.getBoundingClientRect();
			if (mode === 'enter') p = (vh - r.top) / vh;
			else if (mode === 'leave') p = (vh - r.bottom) / vh;
			else p = -r.top / Math.max(1, r.height - vh);
		}
		node.style.setProperty('--p', clamp(p).toFixed(4));
	};
	const schedule = () => {
		if (!raf) raf = requestAnimationFrame(compute);
	};
	compute();
	addEventListener('scroll', schedule, { passive: true });
	addEventListener('resize', schedule);
	return {
		destroy() {
			removeEventListener('scroll', schedule);
			removeEventListener('resize', schedule);
			if (raf) cancelAnimationFrame(raf);
		}
	};
}

/** Adds class `in` once the node is 20% visible. Used for one-shot reveals (line drawing, fades). */
export function reveal(node: HTMLElement | SVGElement, threshold = 0.2) {
	if (reduced() || typeof IntersectionObserver === 'undefined') {
		node.classList.add('in');
		return {};
	}
	const io = new IntersectionObserver(
		(entries) => {
			for (const e of entries) {
				if (e.isIntersecting) {
					node.classList.add('in');
					io.disconnect();
				}
			}
		},
		{ threshold }
	);
	io.observe(node);
	return { destroy: () => io.disconnect() };
}
