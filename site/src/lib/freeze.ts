/**
 * While a modal is open the page behind it is invisible anyway, but the browser keeps
 * painting and compositing it: a sticky hero, blurred panels and a clipped photo, every
 * frame, next to a decoding video. Hiding it costs nothing and gives those frames back.
 * Layout is preserved (visibility, not display), so the scroll position survives.
 */
let depth = 0;

export function freezePage(on: boolean) {
	if (typeof document === 'undefined') return;
	depth = Math.max(0, depth + (on ? 1 : -1));
	document.documentElement.classList.toggle('page-frozen', depth > 0);
}
