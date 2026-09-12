<script lang="ts">
	import PageMeta from '$lib/seo/PageMeta.svelte';
	import { faqNode, apartmentNode } from '$lib/seo/meta';
	import { site, facts, DEMO } from '$lib/site';
	import { apartments, euro } from '$lib/data/apartments';
	import { faq } from '$lib/data/faq';
	import Nav from '$lib/components/Nav.svelte';
	import Icon from '$lib/components/Icon.svelte';
	import SnowWidget from '$lib/components/SnowWidget.svelte';
	import Elevation from '$lib/components/Elevation.svelte';
	import RouteMap from '$lib/components/RouteMap.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import VideoModal from '$lib/components/VideoModal.svelte';
	import { progress, reveal } from '$lib/scroll';
	import { openDemo } from '$lib/demo.svelte';

	const meta = {
		title: 'Huis Hinterglemm · Vier appartementen aan de piste in Hinterglemm',
		description:
			'Ski-in, bijna ski-out: vier ruime appartementen in Hinterglemm, 250 tot 400 meter van de Reiterkogelbahn. Eén prijs per week, alles inbegrepen. Nederlandse eigenaren.',
		path: '/',
		noindex: true, // demo on a preview domain; drop this on the real domain
		graph: [faqNode(faq.slice(0, 5)), ...apartments.map(apartmentNode)]
	};

	const rooms: Record<string, string> = {
		kohlmais: 'slaapkamer',
		reiterkogel: 'woonkamer',
		zwoelferkogel: 'balkon',
		schattberg: 'sauna'
	};

	const three = [
		['Ruim', 'Twee tot acht personen, één grote tafel, een droogruimte voor de skischoenen.'],
		['Dichtbij', 'Lopen naar de gondel. Om negen uur sta je boven.'],
		['Eerlijk', 'Eén prijs per week, alles inbegrepen. Vrij of bezet staat op de site.']
	];

	const levels = [
		[
			'Blauw · voor de kinderen',
			'De Reiterkogel, recht boven ons huis, is de rustige kant: brede blauwe pistes en een skischool die op 200 meter van de deur begint.'
		],
		[
			'Rood · de hele dag variëren',
			'Over de kam naar Saalbach en door naar Leogang: lange rode afdalingen en meer dan 60 hutten onderweg.'
		],
		[
			'Zwart · als eerste in de gondel',
			'De Zwölfer Nordabfahrt begint in Hinterglemm. Sommige liften draaien vanaf 8 uur; om 9 uur sta je boven, wij ook.'
		]
	];
	const total = facts.blue + facts.red + facts.black;
	const pct = (n: number) => ((n / total) * 100).toFixed(1) + '%';

	const practical: [string, string, string][] = [
		[
			'car',
			'Reis vanuit Nederland',
			'± 1.000 km via Keulen, Frankfurt, München en Kufstein; met pauzes tien uur. Vignet online kopen vóór vertrek; winterbanden verplicht 1 nov – 15 apr.'
		],
		[
			'key',
			'Aankomst en sleutel',
			'Inchecken vanaf 16:00, uitchecken tot 10:00. [Sleutelkluis of persoonlijk.] Eigen parkeerplaats bij het huis.'
		],
		[
			'ticket',
			'Skipas 2026/27',
			`6 dagen hoogseizoen (${facts.peakDates}): volwassenen € ${facts.pass6Adult}, jongeren (2008–2010) € ${facts.pass6Youth}, kinderen (2011–2020) € ${facts.pass6Child}. Online of bij het dalstation op 300 m.`
		],
		[
			'ski',
			'Materiaal huren',
			'Twee verhuurwinkels binnen 300 meter. Reserveer online vóór de kerst- en voorjaarsvakantie; dan staat alles klaar.'
		],
		[
			'cart',
			'Boodschappen',
			'Supermarkt op [x] minuten lopen. Bakker vanaf 07:00. Zondag is bijna alles dicht: koop zaterdag in.'
		],
		[
			'bag',
			'Inpaklijst',
			'Skipas-hoesje, zonnebrand, handschoenen voor de kinderen in tweevoud, pantoffels. Beddengoed en handdoeken liggen klaar.'
		]
	];

	const seasons: [string, string, 'low' | 'mid' | 'high'][] = [
		['Laagseizoen', '9 jan – 6 feb · 13 mrt – 4 apr', 'low'],
		['Middenseizoen', '27 nov – 19 dec · 6–13 feb · 27 feb – 13 mrt', 'mid'],
		['Hoogseizoen', '19 dec – 9 jan · 13–27 feb', 'high']
	];

	let video = $state(false);
	let openFaq = $state(0);

	function submit(e: SubmitEvent) {
		e.preventDefault();
		openDemo('form');
	}
</script>

<PageMeta {meta} />

<div id="top" class="page">
	<!-- 1 · hero, pinned; content fades as the sheet slides over it -->
	<section class="hero mobile-dark" use:progress={{ mode: 'page', distance: 0.7 }}>
		<picture class="bg">
			<source
				media="(max-width: 700px)"
				srcset="/img/piste-ochtend-800.jpg 800w, /img/piste-ochtend-1600.jpg 1600w"
			/>
			<img
				src="/img/hero-piste-1600.jpg"
				srcset="/img/hero-piste-800.jpg 800w, /img/hero-piste-1600.jpg 1600w, /img/hero-piste-2400.jpg 2400w"
				sizes="100vw"
				alt="Versgeprepareerde piste boven Hinterglemm in de vroege ochtend, met het dorp en de gondel"
				fetchpriority="high"
				width="2400"
				height="1340"
			/>
		</picture>
		<div class="scrim"></div>
		<Nav />
		<div class="hero-copy">
			<span class="kicker">Hinterglemm · Salzburgerland · Oostenrijk</span>
			<h1>Wakker worden aan de piste.</h1>
			<div class="actions">
				<a href={DEMO} class="btn primary">Bekijk beschikbaarheid <Icon name="arrow" size={18} /></a
				>
				<a href="#appartementen" class="textlink">De vier appartementen</a>
			</div>
			<div class="widget-m"><SnowWidget /></div>
		</div>
		<div class="widget-d"><SnowWidget /></div>
	</section>

	<div class="over">
		<!-- 2 · sheet -->
		<section class="sheet" use:progress={{ mode: 'leave', rest: 0 }}>
			<div class="head">
				<div class="head-text">
					<span class="label">De appartementen</span>
					<h2>Vier huizen onder één dak.</h2>
					<p class="sub">
						Ski-in, bijna ski-out: vier ruime appartementen in Hinterglemm, 250 tot 400 meter van de
						gondel. Nederlandse eigenaren die er zelf elke winter skiën.
					</p>
				</div>
			</div>
			<div class="three">
				{#each three as [t, d] (t)}
					<div class="item">
						<h3>{t}</h3>
						<p>{d}</p>
					</div>
				{/each}
			</div>
		</section>

		<!-- 3 · mask: the village grows inside the house shape until it fills the screen -->
		<section class="mask" use:progress={{ mode: 'pin' }}>
			<div class="pin">
				<div class="house">
					<img
						src="/img/dorp-blauwuur-1600.jpg"
						srcset="/img/dorp-blauwuur-800.jpg 800w, /img/dorp-blauwuur-1600.jpg 1600w"
						sizes="100vw"
						alt="Hinterglemm in het blauwe uur, sneeuw op de daken"
						loading="lazy"
					/>
				</div>
				<div class="mask-copy">
					<span class="label">Hinterglemm om half zes</span>
					<h2>De rustige kant van het dal.</h2>
				</div>
			</div>
		</section>

		<!-- 4 · apartments -->
		<section id="appartementen" class="section glacier apts">
			<div class="head">
				<div class="head-text">
					<span class="label">Kies je huis</span>
					<h2>Van studio voor twee tot acht onder één dak.</h2>
				</div>
				<a href={DEMO} class="btn ghost">Vergelijk alle vier <Icon name="arrow" size={18} /></a>
			</div>
			<div class="grid4">
				{#each apartments as a (a.slug)}
					<a href={DEMO} class="card apt">
						<div class="photo">
							<img
								src="/img/{rooms[a.slug]}-800.jpg"
								srcset="/img/{rooms[a.slug]}-800.jpg 800w, /img/{rooms[a.slug]}-1600.jpg 1600w"
								sizes="(max-width: 900px) 100vw, 25vw"
								alt={a.photos[0].alt}
								loading="lazy"
								width="1264"
								height="848"
							/>
							<span class="cap">voorbeeld (ai)</span>
						</div>
						<div class="body">
							<div class="row">
								<h3>{a.name}</h3>
								<span class="meta">{a.liftMeters} m → lift</span>
							</div>
							<ul class="pills">
								<li class="pill">{a.sleeps} pers.</li>
								<li class="pill">{a.area} m²</li>
								<li class="pill">{a.bedrooms} slaapk.</li>
							</ul>
							<div class="row price">
								<span class="muted">vanaf</span>
								<b>{euro(a.price.low)} <small>/ week</small></b>
							</div>
						</div>
					</a>
				{/each}
			</div>
			<p class="meta muted note">
				Prijzen per week, alles inbegrepen behalve toeristenbelasting. Seizoenstabel onder
				“Prijzen”.
			</p>
		</section>

		<!-- 5 · elevation -->
		<section class="section climb">
			<div class="split">
				<div class="head-text">
					<span class="label">Van de deur tot boven</span>
					<h2>300 meter lopen, dan 750 meter omhoog.</h2>
					<p class="sub">
						Geen skibus, geen parkeerplaats zoeken. Om negen uur sta je op ruim 1.800 meter.
						<span class="meta">[hoogtes verifiëren]</span>
					</p>
				</div>
				<div class="chart">
					<div class="row">
						<span class="label">Hoogteprofiel · afstand vanaf de voordeur</span>
						<span class="meta muted">hover: hoogte + looptijd</span>
					</div>
					<Elevation />
				</div>
			</div>
			<ul class="facts four">
				<li class="fact"><span class="label">Tot de lift</span><b>250–400 m</b></li>
				<li class="fact"><span class="label">Personen</span><b>2–8</b></li>
				<li class="fact"><span class="label">Prijs</span><b>per week, alles-in</b></li>
				<li class="fact"><span class="label">Antwoord</span><b>binnen 24 u</b></li>
			</ul>
		</section>

		<!-- 6 · resort -->
		<section id="skigebied" class="section dark resort">
			<div class="head">
				<div class="head-text">
					<span class="label">Skicircus Saalbach Hinterglemm Leogang Fieberbrunn</span>
					<h2>Een van de grootste skigebieden van Oostenrijk, en je stapt de deur uit.</h2>
					<p class="sub">
						Seizoen {facts.season}. Met de ALPIN CARD ook Zell am See-Kaprun en de
						Kitzsteinhorn-gletsjer:
						{facts.alpinKm} km piste, {facts.alpinLifts} liften.
					</p>
				</div>
			</div>
			<div class="bigs" use:reveal>
				<div><b>{facts.pistes} km</b><span class="label">piste</span></div>
				<div><b>{facts.lifts}</b><span class="label">liften</span></div>
				<div>
					<b>{facts.low}–{facts.high.toLocaleString('nl-NL')} m</b><span class="label">hoogte</span>
				</div>
				<div><b>{facts.huts}+</b><span class="label">hutten</span></div>
			</div>
			<div class="split wide">
				<div class="photo tall">
					<img
						src="/img/skischool-800.jpg"
						srcset="/img/skischool-800.jpg 800w, /img/skischool-1600.jpg 1600w"
						sizes="(max-width: 900px) 100vw, 55vw"
						alt="Skischool op de Reiterkogel, kinderen op een brede blauwe piste"
						loading="lazy"
					/>
					<span class="cap">skischool reiterkogel · voorbeeld (ai)</span>
				</div>
				<div class="bar-wrap" use:reveal>
					<div class="row">
						<span class="label">Pistekilometers per kleur</span>
						<span class="meta muted">{facts.pistes} km totaal</span>
					</div>
					<div class="bar">
						<div class="b" style:width={pct(facts.blue)}></div>
						<div class="r" style:width={pct(facts.red)}></div>
						<div class="k" style:width={pct(facts.black)}></div>
					</div>
					<div class="legend meta">
						<span><i class="b"></i>blauw {facts.blue} km</span>
						<span><i class="r"></i>rood {facts.red} km</span>
						<span><i class="k"></i>zwart {facts.black} km</span>
					</div>
					<p class="meta src">Cijfers: saalbach.com, {facts.checked}.</p>
				</div>
			</div>
			<div class="three">
				{#each levels as [t, d] (t)}
					<div class="item">
						<h3>{t}</h3>
						<p>{d}</p>
					</div>
				{/each}
			</div>
		</section>

		<!-- 7 · practical -->
		<section id="praktisch" class="section practical">
			<div class="head">
				<div class="head-text">
					<span class="label">Praktisch</span>
					<h2>Alles wat je wilt weten voordat je de auto inlaadt.</h2>
				</div>
			</div>
			<div class="route">
				<span class="label">Rijden vanuit Nederland · ± 10 uur</span>
				<RouteMap />
			</div>
			<div class="three items">
				{#each practical as [i, t, d] (t)}
					<div class="item">
						<Icon name={i} />
						<h3>{t}</h3>
						<p>{d}</p>
					</div>
				{/each}
			</div>
		</section>

		<!-- 8 · prices -->
		<section id="prijzen" class="section glacier prices">
			<div class="head">
				<div class="head-text">
					<span class="label">Prijzen</span>
					<h2>Eén prijs per week. Geen verrassingen.</h2>
					<p class="sub">
						Beddengoed, handdoeken, eindschoonmaak, wifi en parkeren zitten erin. Alleen de
						toeristenbelasting (€ [x] p.p. per nacht) komt erbij. [x]% aanbetaling via iDEAL.
					</p>
				</div>
			</div>
			<div class="table" role="table" aria-label="Weekprijzen per seizoen">
				<div class="tr th" role="row">
					<span role="columnheader">Seizoen</span>
					<span role="columnheader">Weken 2026/27 (za–za)</span>
					{#each apartments as a (a.slug)}<span role="columnheader" class="num"
							>{a.name} · {a.sleeps} p.</span
						>{/each}
				</div>
				{#each seasons as [name, dates, key] (key)}
					<div class="tr" role="row">
						<b role="cell">{name}</b>
						<span role="cell" class="meta muted dates">{dates}</span>
						{#each apartments as a (a.slug)}
							<b role="cell" class="num amount"
								><span class="apt-m">{a.name} </span>{euro(a.price[key])}</b
							>
						{/each}
					</div>
				{/each}
			</div>
			<div class="actions">
				<a href={DEMO} class="btn primary">Bekijk beschikbaarheid <Icon name="arrow" size={18} /></a
				>
				<a href={DEMO} class="btn secondary"><Icon name="wa" size={18} /> Vraag het via WhatsApp</a>
			</div>
		</section>

		<!-- 9 · hosts + video card -->
		<section id="over-ons" class="section hosts">
			<div class="card host">
				<div class="photo">
					<img
						src="/img/gondel-800.jpg"
						srcset="/img/gondel-800.jpg 800w, /img/gondel-1600.jpg 1600w"
						sizes="(max-width: 900px) 100vw, 30vw"
						alt="Gondel van de Reiterkogelbahn boven Hinterglemm"
						loading="lazy"
					/>
					<span class="cap">[host] · voorbeeld (ai)</span>
				</div>
				<div class="body">
					<span class="label">Over ons</span>
					<h2>Wij zijn {site.hosts}, uit {site.hostsFrom}.</h2>
					<p>
						[Waarom dit huis, sinds wanneer, hoe vaak jullie er zelf zijn. Twee zinnen, in jullie
						eigen woorden.]
					</p>
					<div class="links">
						<a href={DEMO}><Icon name="wa" size={18} /> WhatsApp</a>
						<a href={DEMO}><Icon name="mail" size={18} /> {site.email}</a>
					</div>
				</div>
			</div>
			<button type="button" class="card story" onclick={() => (video = true)}>
				<img
					src="/img/aerial-dorp-800.jpg"
					srcset="/img/aerial-dorp-800.jpg 800w, /img/aerial-dorp-1600.jpg 1600w"
					sizes="(max-width: 900px) 100vw, 35vw"
					alt=""
					loading="lazy"
				/>
				<div class="story-copy">
					<span class="label">Video · 0:26</span>
					<h3>Hinterglemm van boven, op een ochtend in januari.</h3>
					<span class="play"><Icon name="play" size={18} /> Bekijk de video</span>
				</div>
			</button>
		</section>

		<!-- 10 · faq -->
		<section class="section faq">
			<div class="head-text">
				<span class="label">Veelgestelde vragen</span>
				<h2>Wat mensen ons eerst vragen.</h2>
			</div>
			<div class="qs">
				{#each faq.slice(0, 5) as f, i (f.q)}
					<div class="q" class:open={openFaq === i}>
						<h3>
							<button
								type="button"
								aria-expanded={openFaq === i}
								onclick={() => (openFaq = openFaq === i ? -1 : i)}
							>
								{f.q}
								<Icon name="plus" size={18} />
							</button>
						</h3>
						{#if openFaq === i}<p>{f.a}</p>{/if}
					</div>
				{/each}
			</div>
		</section>

		<!-- 11 · inquiry -->
		<section id="aanvraag" class="section glacier contact">
			<div class="head-text">
				<span class="label">Aanvraag</span>
				<h2>Welke week wordt het?</h2>
				<p class="sub">
					Stuur je data en het aantal personen. Wij kijken of het vrij is en sturen binnen 24 uur
					een voorstel. Liever direct? WhatsApp werkt ook.
				</p>
				<a href={DEMO} class="btn secondary self"
					><Icon name="wa" size={18} /> {site.phoneDisplay}</a
				>
			</div>
			<form class="card form" onsubmit={submit}>
				<div class="two">
					<label class="field"
						><span>Appartement</span>
						<select name="apartment"
							>{#each apartments as a (a.slug)}<option value={a.slug}
									>{a.name} · {a.sleeps} pers.</option
								>{/each}</select
						></label
					>
					<label class="field"
						><span>Personen</span><input
							name="persons"
							type="number"
							min="1"
							max="8"
							value="4"
						/></label
					>
				</div>
				<div class="two">
					<label class="field"
						><span>Aankomst</span><input name="arrival" type="date" required /></label
					>
					<label class="field"
						><span>Vertrek</span><input name="departure" type="date" required /></label
					>
				</div>
				<label class="field"
					><span>Naam</span><input name="name" type="text" autocomplete="name" required /></label
				>
				<label class="field"
					><span>E-mail</span><input
						name="email"
						type="email"
						autocomplete="email"
						required
					/></label
				>
				<label class="field"
					><span>Vragen of wensen (optioneel)</span><textarea name="message" rows="3"
					></textarea></label
				>
				<button type="submit" class="btn primary"
					>Stuur aanvraag <Icon name="arrow" size={18} /></button
				>
				<span class="meta muted">Binnen 24 uur antwoord. Geen account, geen betaling nu.</span>
			</form>
		</section>

		<Footer />
	</div>
</div>

<VideoModal bind:open={video} />

<style>
	.page {
		position: relative;
	}

	/* hero */
	.hero {
		position: sticky;
		top: 0;
		height: 100svh;
		min-height: 640px;
		overflow: hidden;
		background: var(--ink);
		color: var(--snow);
		z-index: 0;
	}
	.hero .bg,
	.hero .bg img {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		object-fit: cover;
		object-position: 55% 50%;
	}
	.hero .bg img {
		transform: scale(calc(1 + var(--p, 0) * 0.06));
		transform-origin: 50% 40%;
	}
	.hero .scrim {
		position: absolute;
		inset: 0;
		background:
			linear-gradient(
				180deg,
				oklch(0.985 0.004 240 / 0.78) 0%,
				oklch(0.985 0.004 240 / 0.35) 14%,
				transparent 30%
			),
			linear-gradient(180deg, transparent 42%, oklch(0.24 0.05 255 / 0.72) 100%);
	}
	.hero-copy {
		position: absolute;
		left: var(--gutter);
		right: var(--gutter);
		bottom: 56px;
		display: flex;
		flex-direction: column;
		gap: 22px;
		max-width: 880px;
		opacity: calc(1 - var(--p, 0) * 1.4);
		transform: translateY(calc(var(--p, 0) * -40px));
	}
	.kicker {
		font-family: var(--font-label);
		font-weight: 500;
		font-size: 0.75rem;
		letter-spacing: 0.08em;
		text-transform: uppercase;
		opacity: 0.9;
	}
	.hero h1 {
		font-size: clamp(3.4rem, 1rem + 8vw, 7.5rem);
		line-height: 0.9;
		max-width: 10ch;
	}
	.hero .actions {
		display: flex;
		gap: 14px;
		align-items: center;
		flex-wrap: wrap;
	}
	.textlink {
		font-weight: 600;
		border-bottom: 1.5px solid currentColor;
		padding-bottom: 2px;
	}
	.widget-d {
		position: absolute;
		right: var(--gutter);
		bottom: 56px;
		opacity: calc(1 - var(--p, 0) * 1.4);
	}
	.widget-m {
		display: none;
	}
	@media (max-width: 900px) {
		.hero .scrim {
			background:
				linear-gradient(180deg, oklch(0.24 0.05 255 / 0.5) 0%, transparent 30%),
				linear-gradient(180deg, transparent 42%, oklch(0.24 0.05 255 / 0.78) 100%);
		}
		.hero :global(.logo img) {
			content: url('/brand/lockup-white.svg');
		}
		.hero-copy {
			bottom: 36px;
			gap: 16px;
		}
		.hero h1 {
			font-size: clamp(3rem, 14vw, 4.2rem);
			line-height: 0.92;
		}
		.widget-d {
			display: none;
		}
		.widget-m {
			display: block;
		}
	}

	/* everything after the hero slides over it */
	.over {
		position: relative;
		z-index: 2;
		background: var(--snow);
	}

	/* shared section layout */
	.section {
		padding: var(--section) var(--gutter);
		display: flex;
		flex-direction: column;
		gap: clamp(28px, 4vw, 48px);
	}
	.head {
		display: flex;
		justify-content: space-between;
		align-items: flex-end;
		gap: 24px;
		flex-wrap: wrap;
	}
	.head-text {
		display: flex;
		flex-direction: column;
		gap: 12px;
		max-width: 820px;
	}
	.sub {
		font-size: clamp(1rem, 0.9rem + 0.4vw, 1.125rem);
		color: var(--ink-2);
		max-width: 48ch;
	}
	.dark .sub {
		color: var(--ink-3);
	}
	.three {
		display: grid;
		grid-template-columns: repeat(3, minmax(0, 1fr));
		gap: 24px;
	}
	.item {
		border-top: 1.5px solid var(--ink);
		padding-top: 14px;
		display: flex;
		flex-direction: column;
		gap: 8px;
	}
	.item p {
		font-size: var(--fs-small);
		color: var(--ink-2);
	}
	.dark .item {
		border-top: 1px solid oklch(0.36 0.05 255);
	}
	.dark .item p {
		color: var(--ink-3);
	}
	.row {
		display: flex;
		justify-content: space-between;
		align-items: baseline;
		gap: 12px;
		flex-wrap: wrap;
	}
	@media (max-width: 900px) {
		.three {
			grid-template-columns: 1fr;
		}
	}

	/* sheet */
	.sheet {
		position: relative;
		background: linear-gradient(180deg, var(--snow) 0%, var(--snow) 70%, var(--glacier) 100%);
		border-radius: 28px 28px 0 0;
		margin-top: -28px;
		padding: var(--section) var(--gutter);
		display: flex;
		flex-direction: column;
		gap: clamp(28px, 4vw, 48px);
	}
	.sheet .three {
		/* starts fading once the house shape fills the lower third of the screen */
		opacity: calc(1 - max(0, var(--p, 0) - 0.3) * 2.5);
		transform: translateY(calc(max(0, var(--p, 0) - 0.3) * -40px));
	}

	/* mask */
	.mask {
		position: relative;
		height: 220svh;
		background: var(--glacier);
	}
	.pin {
		position: sticky;
		top: 0;
		height: 100svh;
		overflow: hidden;
	}
	.house {
		position: absolute;
		inset: 0;
		--h: var(--p, 0);
		/* house vertices → far outside the box, so at --p = 1 the photo is full-bleed */
		clip-path: polygon(
			calc(10% - 40% * var(--h)) calc(92% + 60% * var(--h)),
			calc(10% - 40% * var(--h)) calc(50% - 90% * var(--h)),
			calc(32% - 12% * var(--h)) calc(27% - 80% * var(--h)),
			calc(50% + 0% * var(--h)) calc(47% - 90% * var(--h)),
			calc(68% + 12% * var(--h)) calc(17% - 80% * var(--h)),
			calc(90% + 40% * var(--h)) calc(40% - 90% * var(--h)),
			calc(90% + 40% * var(--h)) calc(92% + 60% * var(--h))
		);
	}
	.house img {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		object-fit: cover;
		transform: scale(calc(1.15 - var(--p, 0) * 0.15));
	}
	.mask-copy {
		position: absolute;
		left: var(--gutter);
		bottom: 56px;
		display: flex;
		flex-direction: column;
		gap: 10px;
		color: var(--snow);
		opacity: calc((var(--p, 0) - 0.55) * 3);
		transform: translateY(calc((1 - var(--p, 0)) * 30px));
	}
	.mask-copy .label {
		color: var(--ice);
	}
	.mask-copy h2 {
		font-size: clamp(2rem, 1.2rem + 3vw, 3.5rem);
		max-width: 14ch;
	}
	@media (max-width: 900px) {
		.house {
			inset: 0 -10%;
		}
	}

	/* apartments */
	.grid4 {
		display: grid;
		grid-template-columns: repeat(4, minmax(0, 1fr));
		gap: 20px;
	}
	.apt {
		display: flex;
		flex-direction: column;
		background: var(--snow);
		border: 1px solid var(--stone);
		color: inherit;
		transition: transform var(--t-base) var(--ease-out);
	}
	.apt:hover {
		color: inherit;
		transform: translateY(-3px);
	}
	.apt .photo {
		height: 260px;
		border-radius: 0;
	}
	.apt .body {
		padding: 16px 18px 18px;
		display: flex;
		flex-direction: column;
		gap: 10px;
	}
	.apt .price {
		border-top: 1px solid var(--stone);
		padding-top: 10px;
	}
	.apt .price b {
		font-family: var(--font-display);
		font-size: 1.375rem;
		letter-spacing: -0.02em;
	}
	.apt .price small {
		font-family: var(--font-body);
		font-weight: 400;
		font-size: 0.875rem;
		color: var(--stone-2);
	}
	.note {
		font-size: 0.75rem;
	}
	@media (max-width: 1100px) {
		.grid4 {
			grid-template-columns: repeat(2, minmax(0, 1fr));
		}
	}
	@media (max-width: 600px) {
		.grid4 {
			grid-template-columns: 1fr;
		}
		.apt .photo {
			height: 220px;
		}
	}

	/* climb */
	.split {
		display: grid;
		grid-template-columns: 1fr 1.3fr;
		gap: clamp(24px, 5vw, 64px);
		align-items: start;
	}
	.split.wide {
		grid-template-columns: 1.2fr 1fr;
		align-items: center;
	}
	.chart {
		display: flex;
		flex-direction: column;
		gap: 10px;
		min-width: 0;
	}
	.facts.four {
		grid-template-columns: repeat(4, minmax(0, 1fr));
		gap: 24px;
	}
	@media (max-width: 900px) {
		.split,
		.split.wide {
			grid-template-columns: 1fr;
		}
		.facts.four {
			grid-template-columns: repeat(2, minmax(0, 1fr));
			gap: 14px;
		}
		.fact:nth-child(2) {
			border-right: 0;
		}
	}

	/* resort */
	.bigs {
		display: grid;
		grid-template-columns: repeat(4, minmax(0, 1fr));
		gap: 24px;
	}
	.bigs > div {
		display: flex;
		flex-direction: column;
		gap: 6px;
		border-top: 1px solid oklch(0.36 0.05 255);
		padding-top: 14px;
		opacity: 0;
		transform: translateY(12px);
		transition:
			opacity 600ms var(--ease-out),
			transform 600ms var(--ease-out);
	}
	.bigs:global(.in) > div {
		opacity: 1;
		transform: none;
	}
	.bigs > div:nth-child(2) {
		transition-delay: 80ms;
	}
	.bigs > div:nth-child(3) {
		transition-delay: 160ms;
	}
	.bigs > div:nth-child(4) {
		transition-delay: 240ms;
	}
	.bigs b {
		font-family: var(--font-display);
		font-size: clamp(2.25rem, 1.5rem + 2vw, 3rem);
		letter-spacing: -0.03em;
		line-height: 1;
	}
	.photo.tall {
		height: 420px;
	}
	.bar-wrap {
		display: flex;
		flex-direction: column;
		gap: 10px;
		min-width: 0;
	}
	.bar {
		display: flex;
		height: 14px;
		border-radius: 7px;
		overflow: hidden;
		gap: 2px;
		background: var(--snow);
	}
	.bar > div {
		transform-origin: left;
		transform: scaleX(0);
		transition: transform 900ms var(--ease-out);
	}
	.bar-wrap:global(.in) .bar > div {
		transform: none;
	}
	.bar .b,
	.legend .b {
		background: var(--piste);
	}
	.bar .r,
	.legend .r {
		background: oklch(0.55 0.2 25);
	}
	.bar .k,
	.legend .k {
		background: var(--snow);
	}
	.legend {
		display: flex;
		gap: 20px;
		flex-wrap: wrap;
	}
	.legend i {
		display: inline-block;
		width: 10px;
		height: 10px;
		border-radius: 2px;
		margin-right: 6px;
	}
	.src {
		font-size: 0.75rem;
		color: var(--ink-3);
		margin-top: 10px;
	}
	@media (max-width: 900px) {
		.bigs {
			grid-template-columns: repeat(2, minmax(0, 1fr));
		}
		.photo.tall {
			height: 240px;
		}
	}

	/* practical */
	.route {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}
	.items .item {
		border-top: 1px solid var(--stone);
		padding-top: 16px;
		gap: 10px;
	}

	/* prices */
	.table {
		display: flex;
		flex-direction: column;
		border-bottom: 1px solid var(--stone);
	}
	.tr {
		display: grid;
		grid-template-columns: 1.4fr 2fr repeat(4, minmax(0, 1fr));
		gap: 12px;
		align-items: baseline;
		border-top: 1px solid var(--stone);
		padding: 14px 0;
	}
	.tr.th {
		border-top: 0;
		padding: 0 0 12px;
		font-family: var(--font-label);
		font-weight: 500;
		font-size: var(--fs-label);
		letter-spacing: 0.08em;
		text-transform: uppercase;
		color: var(--stone-2);
	}
	.num {
		text-align: right;
	}
	.amount {
		font-family: var(--font-display);
		font-size: 1.375rem;
		letter-spacing: -0.02em;
	}
	.dates {
		font-size: 0.75rem;
	}
	.apt-m {
		display: none;
	}
	.prices .actions,
	.actions {
		display: flex;
		gap: 12px;
		flex-wrap: wrap;
	}
	@media (max-width: 900px) {
		.tr.th {
			display: none;
		}
		.tr {
			grid-template-columns: 1fr 1fr;
			gap: 6px 12px;
			padding: 16px 0;
		}
		.tr > b:first-child {
			grid-column: 1 / -1;
			font-size: 1.125rem;
		}
		.dates {
			grid-column: 1 / -1;
		}
		.num {
			text-align: left;
		}
		.amount {
			font-family: var(--font-body);
			font-size: 0.9375rem;
			font-weight: 400;
			letter-spacing: 0;
		}
		.apt-m {
			display: inline;
		}
		.amount :global(+ .amount) {
			font-weight: 400;
		}
	}

	/* hosts */
	.hosts {
		display: grid;
		grid-template-columns: 1.4fr 1fr;
		gap: 32px;
	}
	.host {
		display: grid;
		grid-template-columns: 1fr 1.2fr;
	}
	.host .photo {
		min-height: 420px;
		border-radius: 0;
	}
	.host .body {
		padding: 40px;
		display: flex;
		flex-direction: column;
		gap: 14px;
		justify-content: center;
	}
	.host h2 {
		font-size: clamp(1.75rem, 1.4rem + 1.5vw, 2.5rem);
	}
	.host .body > p {
		color: var(--ink-2);
	}
	.links {
		display: flex;
		gap: 16px;
		flex-wrap: wrap;
		font-weight: 600;
	}
	.links a {
		display: inline-flex;
		align-items: center;
		gap: 8px;
	}
	.story {
		position: relative;
		display: flex;
		flex-direction: column;
		justify-content: flex-end;
		min-height: 100%;
		padding: 0;
		border: 0;
		text-align: left;
		color: var(--snow);
		background: var(--ink);
		cursor: pointer;
		font: inherit;
	}
	.story > img {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		object-fit: cover;
		opacity: 0.7;
		transition: transform 900ms var(--ease-out);
	}
	.story:hover > img {
		transform: scale(1.04);
	}
	.story::after {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(180deg, transparent 30%, oklch(0.24 0.05 255 / 0.85) 100%);
	}
	.story-copy {
		position: relative;
		z-index: 1;
		padding: 24px;
		display: flex;
		flex-direction: column;
		gap: 10px;
	}
	.story-copy .label {
		color: var(--ice);
	}
	.story-copy h3 {
		font-size: clamp(1.5rem, 1.2rem + 1vw, 1.75rem);
	}
	.play {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		font-weight: 600;
	}
	@media (max-width: 900px) {
		.hosts,
		.host {
			grid-template-columns: 1fr;
		}
		.hosts {
			gap: 20px;
		}
		.host .photo {
			min-height: 240px;
			height: 240px;
		}
		.host .body {
			padding: 24px;
		}
		.story {
			min-height: 280px;
		}
	}

	/* faq */
	.faq {
		display: grid;
		grid-template-columns: 1fr 1.6fr;
		gap: clamp(20px, 5vw, 64px);
	}
	.qs {
		display: flex;
		flex-direction: column;
		border-bottom: 1px solid var(--stone);
	}
	.q {
		border-top: 1px solid var(--stone);
		padding: 18px 0;
		display: flex;
		flex-direction: column;
		gap: 8px;
	}
	.q h3 button {
		width: 100%;
		display: flex;
		justify-content: space-between;
		gap: 16px;
		align-items: center;
		background: none;
		border: 0;
		padding: 0;
		font: inherit;
		color: inherit;
		text-align: left;
		cursor: pointer;
	}
	.q h3 button :global(.ico) {
		transition: transform var(--t-base) var(--ease-out);
	}
	.q.open h3 button :global(.ico) {
		transform: rotate(45deg);
	}
	.q p {
		font-size: var(--fs-small);
		color: var(--ink-2);
		max-width: 60ch;
	}
	@media (max-width: 900px) {
		.faq {
			grid-template-columns: 1fr;
		}
	}

	/* contact */
	.contact {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: clamp(24px, 5vw, 64px);
		align-items: start;
	}
	.contact .head-text {
		gap: 18px;
	}
	.self {
		align-self: flex-start;
	}
	.form {
		padding: 28px;
		background: var(--snow);
		display: flex;
		flex-direction: column;
		gap: 12px;
	}
	.two {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 10px;
	}
	.field {
		display: flex;
		flex-direction: column;
		gap: 6px;
	}
	.field span {
		font-size: var(--fs-small);
		font-weight: 600;
	}
	.field input,
	.field select,
	.field textarea {
		width: 100%;
		min-height: 48px;
		border: 1.5px solid var(--stone);
		border-radius: var(--r-control);
		background: #fff;
		padding: 0 12px;
		color: var(--ink);
		font: inherit;
	}
	.field textarea {
		padding-block: 10px;
		resize: vertical;
	}
	.field input:focus,
	.field select:focus,
	.field textarea:focus {
		border-color: var(--piste);
		outline: none;
	}
	.form .meta {
		font-size: 0.75rem;
	}
	@media (max-width: 900px) {
		.contact {
			grid-template-columns: 1fr;
		}
		.form {
			padding: 20px;
		}
	}
</style>
