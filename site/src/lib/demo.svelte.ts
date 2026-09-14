/** Demo overlay state. Any link that is not built yet opens it; the form does too. */
export type DemoKind = 'link' | 'form' | 'nav';

export const demo = $state({ open: false, kind: 'link' as DemoKind });

export function openDemo(kind: DemoKind = 'link') {
	demo.kind = kind;
	demo.open = true;
}

export function closeDemo() {
	demo.open = false;
}
