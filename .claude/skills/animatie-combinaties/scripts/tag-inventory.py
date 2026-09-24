#!/usr/bin/env python3
"""Inventariseer een map met losse animatie-HTML-bestanden.

Leest van elk .html-bestand het commentaarblok bovenaan (bron, wat het doet,
afhankelijkheden, wat er veranderd is) en de <title>, en schrijft een JSON-lijst met
per bestand de gevonden velden, lege tag-kolommen om in te vullen, en een eerste gok
(`afgeleid`) voor soort en trigger op basis van de woorden in titel en beschrijving.

Gebruik:
    python3 tag-inventory.py <map>            JSON naar stdout
    python3 tag-inventory.py <map> --md       markdown-tabel om in te vullen

De gok is een gok. Tags die Jaymar niet heeft bevestigd blijven 'afgeleid'.
"""
import json
import re
import sys
from pathlib import Path

LABELS = {
    "bron": ("bron", "source", "origin", "van"),
    "beschrijving": ("wat het doet", "doet", "beschrijving", "description", "what"),
    "afhankelijkheden": ("afhankelijkheden", "dependencies", "deps", "libs", "stack"),
    "veranderd": ("wat er veranderd is", "veranderd", "changes", "changed", "aangepast"),
}

SOORT_WOORDEN = {
    "tekst": ("tekst", "text", "heading", "kop", "split", "letters", "words", "typewriter", "type", "char"),
    "beeld": ("beeld", "image", "foto", "photo", "frames", "sequence", "video", "ken burns", "kenburns", "masker", "mask", "clip", "gallery", "grid"),
    "navigatie": ("nav", "menu", "hamburger", "header", "page transition", "paginawissel"),
    "laden": ("loader", "preloader", "laad", "loading", "intro", "counter"),
    "hover": ("hover", "cursor", "magnetic", "tilt", "button", "knop", "card", "kaart"),
    "overgang": ("overgang", "transition", "stack", "sticky", "panels", "vlakken", "section", "sectie", "curtain"),
    "hero": ("hero", "entree", "entrance", "opening"),
}

TRIGGER_WOORDEN = {
    "scrub": ("scrub", "scroll-driven", "scrolldriven", "frames op scroll", "pin"),
    "scroll": ("scroll", "reveal", "enter", "in view", "inview", "viewport"),
    "hover": ("hover", "cursor", "magnetic", "tilt"),
    "klik": ("click", "klik", "toggle", "open", "menu"),
    "laden": ("load", "laden", "loader", "preloader", "intro", "mount"),
    "tijd": ("loop", "marquee", "ticker", "auto", "interval"),
}


def kop_commentaar(html: str) -> str:
    """Eerste HTML-commentaarblok, of leeg."""
    m = re.search(r"<!--(.*?)-->", html, re.S)
    return m.group(1).strip() if m else ""


def velden(commentaar: str) -> dict:
    uit = {k: "" for k in LABELS}
    huidig = None
    for regel in commentaar.splitlines():
        regel = regel.strip().lstrip("*-• ").strip()
        if not regel:
            continue
        kop, sep, rest = regel.partition(":")
        kop_l = kop.strip().lower()
        gevonden = None
        if sep:
            for veld, namen in LABELS.items():
                if kop_l in namen or any(kop_l.startswith(n) for n in namen):
                    gevonden = veld
                    break
        if gevonden:
            huidig = gevonden
            uit[huidig] = rest.strip()
        elif huidig:
            uit[huidig] = (uit[huidig] + " " + regel).strip()
    if not any(uit.values()) and commentaar:
        uit["beschrijving"] = " ".join(commentaar.split())
    return uit


def titel(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    return " ".join(m.group(1).split()) if m else ""


def gok(tekst: str, woordenboek: dict) -> list:
    t = tekst.lower()
    return [k for k, woorden in woordenboek.items() if any(w in t for w in woorden)]


def deps_uit_html(html: str) -> list:
    deps = []
    for naam, patroon in (
        ("gsap", r"gsap(\.min)?\.js|gsap\.registerPlugin|from ['\"]gsap"),
        ("scrolltrigger", r"ScrollTrigger"),
        ("lenis", r"lenis", ),
        ("splittext", r"SplitText"),
        ("lottie", r"lottie"),
        ("three", r"three(\.min)?\.js|THREE\."),
    ):
        if re.search(patroon, html, re.I):
            deps.append(naam)
    if not deps:
        deps.append("css-only" if "<script" not in html.lower() else "vanilla-js")
    return deps


def inventaris(map_: Path) -> list:
    items = []
    for pad in sorted(map_.glob("*.html")):
        if pad.name.lower() == "index.html":
            continue
        html = pad.read_text(encoding="utf-8", errors="replace")
        v = velden(kop_commentaar(html))
        t = titel(html)
        basis = " ".join([pad.stem, t, v["beschrijving"]])
        items.append({
            "bestand": pad.name,
            "titel": t or pad.stem,
            "bron": v["bron"],
            "beschrijving": v["beschrijving"],
            "afhankelijkheden": v["afhankelijkheden"] or ", ".join(deps_uit_html(html)),
            "veranderd": v["veranderd"],
            "webgl": bool(re.search(r"getContext\(\s*['\"]webgl", html)),
            "reduced_motion_css": "prefers-reduced-motion" in html,
            "tags": {"geluid": "", "soort": "", "trigger": "", "klasse": ""},
            "afgeleid": {
                "soort": gok(basis, SOORT_WOORDEN),
                "trigger": gok(basis, TRIGGER_WOORDEN),
                "klasse": "C?" if re.search(r"getContext\(\s*['\"]webgl", html) else "",
            },
        })
    return items


def markdown(items: list) -> str:
    regels = [
        "| bestand | titel | afgeleid soort | afgeleid trigger | geluid | soort | trigger | klasse |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for it in items:
        regels.append(
            f"| {it['bestand']} | {it['titel']} | {', '.join(it['afgeleid']['soort']) or '—'} | "
            f"{', '.join(it['afgeleid']['trigger']) or '—'} |  |  |  | {it['afgeleid']['klasse']} |"
        )
    return "\n".join(regels)


def main(argv: list) -> int:
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 2
    map_ = Path(argv[1])
    if not map_.is_dir():
        print(f"geen map: {map_}", file=sys.stderr)
        return 1
    items = inventaris(map_)
    if "--md" in argv:
        print(markdown(items))
    else:
        json.dump(items, sys.stdout, ensure_ascii=False, indent=2)
        print()
    print(f"{len(items)} bestanden gelezen uit {map_}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
