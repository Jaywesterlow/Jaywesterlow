/** In-memory limiter: N hits per window per key. Per function instance, which is enough to stop a script hammering the form. */
const hits = new Map<string, { count: number; reset: number }>();

export function limited(key: string, max = 5, windowMs = 10 * 60 * 1000) {
	const now = Date.now();
	const entry = hits.get(key);
	if (!entry || entry.reset < now) {
		hits.set(key, { count: 1, reset: now + windowMs });
		return false;
	}
	entry.count += 1;
	return entry.count > max;
}
