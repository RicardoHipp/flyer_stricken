#!/usr/bin/env python3
"""Baut die eingebetteten Ressourcen des Flyers.

Erzeugt zwei Dateien:

  assets.css     Webfont Oswald (woff2) als data:-URI, fuer die Anzeige.
  bg-data.js     Hintergrundbild als data:-URI. Als data:-URI, weil ein per
                 Dateipfad geladenes Bild beim Oeffnen per Doppelklick (file://)
                 das Canvas verunreinigt und html2canvas dann abbricht.
                 Als JS-Datei und nicht im CSS, weil Chrome CSS-Variablen ab
                 etwa einem Megabyte stillschweigend verwirft.
  fonts-pdf.js   Oswald in 400/600/700 als TrueType-Base64, fuer den PDF-Export.
                 jsPDF braucht TTF -- woff2 und Variable Fonts kann es nicht.

Aufruf (aus dem Projektordner):   python tools/embed-assets.py
Neu ausfuehren, wenn Hintergrund.jpg ausgetauscht wurde.

Benoetigt fuer die TTF-Erzeugung: pip install fonttools brotli
"""

import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BG = ROOT / "Hintergrund.jpg"
WOFF2 = ROOT / "tools" / "oswald-latin.woff2"
OUT_CSS = ROOT / "assets.css"
OUT_BG = ROOT / "bg-data.js"
OUT_JS = ROOT / "fonts-pdf.js"

GEWICHTE = (400, 600, 700)

# Was im Flyer vorkommen kann: Latin-1 plus die Typografie-Zeichen, die in
# deutschen Texten auftauchen (Gedankenstrich, Anfuehrungszeichen, Aufzaehlung).
ZEICHEN = (
    list(range(0x20, 0x100))
    + [0x2013, 0x2014, 0x2018, 0x2019, 0x201A, 0x201C, 0x201D, 0x201E,
       0x2022, 0x2026, 0x20AC, 0x2122]
)


def b64(daten: bytes) -> str:
    return base64.b64encode(daten).decode("ascii")


def css_bauen() -> None:
    teile = ["/* Automatisch erzeugt von tools/embed-assets.py -- nicht von Hand aendern. */\n"]

    if WOFF2.exists():
        teile.append(
            "@font-face{font-family:'Oswald';font-style:normal;font-weight:200 700;"
            "font-display:block;src:url(data:font/woff2;base64,"
            + b64(WOFF2.read_bytes())
            + ") format('woff2');}\n"
        )
    else:
        print(f"Hinweis: {WOFF2.name} fehlt -- es wird die Fallback-Schrift benutzt.")

    OUT_CSS.write_text("".join(teile), encoding="utf-8")
    print(f"{OUT_CSS.name} geschrieben ({OUT_CSS.stat().st_size / 1024:.0f} KB)")


def bild_bauen() -> None:
    OUT_BG.write_text(
        "// Automatisch erzeugt von tools/embed-assets.py -- nicht von Hand aendern.\n"
        'window.FLYER_BG = "data:image/jpeg;base64,' + b64(BG.read_bytes()) + '";\n',
        encoding="utf-8",
    )
    print(f"{OUT_BG.name} geschrieben ({OUT_BG.stat().st_size / 1024:.0f} KB)")


def schriften_bauen() -> None:
    """Variable Schrift auf feste Gewichte festzurren, verkleinern, als TTF ablegen."""
    if not WOFF2.exists():
        print("Hinweis: ohne oswald-latin.woff2 kein fonts-pdf.js -- "
              "der PDF-Download faellt dann auf den Bild-Weg zurueck.")
        return
    try:
        from fontTools.ttLib import TTFont
        from fontTools.varLib import instancer
        from fontTools.subset import Subsetter
    except ImportError:
        print("Hinweis: fonttools fehlt (pip install fonttools brotli) -- "
              "fonts-pdf.js wird nicht erneuert.")
        return

    schriften = {}
    for gewicht in GEWICHTE:
        font = TTFont(str(WOFF2))
        font = instancer.instantiateVariableFont(font, {"wght": gewicht}, inplace=True)

        sub = Subsetter()
        sub.populate(unicodes=ZEICHEN)
        sub.subset(font)

        font.flavor = None                      # als schlichtes TTF speichern
        puffer = __import__("io").BytesIO()
        font.save(puffer)
        schriften[str(gewicht)] = b64(puffer.getvalue())
        print(f"  Oswald {gewicht}: {len(puffer.getvalue()) / 1024:.0f} KB")

    OUT_JS.write_text(
        "// Automatisch erzeugt von tools/embed-assets.py -- nicht von Hand aendern.\n"
        "// Oswald (SIL Open Font License) als TrueType, Base64 -- fuer den PDF-Export.\n"
        "window.FLYER_FONTS = " + json.dumps(schriften) + ";\n",
        encoding="utf-8",
    )
    print(f"{OUT_JS.name} geschrieben ({OUT_JS.stat().st_size / 1024:.0f} KB)")


def main() -> int:
    if not BG.exists():
        print(f"FEHLER: {BG} nicht gefunden.", file=sys.stderr)
        return 1
    css_bauen()
    bild_bauen()
    schriften_bauen()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
