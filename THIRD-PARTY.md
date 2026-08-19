# Verwendete fremde Bestandteile

Alle drei sind frei verwendbar, auch kommerziell, und dürfen weitergegeben
werden. Bedingung ist jeweils nur, dass Copyright-Zeile und Lizenztext
mitgeliefert werden — dafür liegen die vollständigen Texte im Ordner
`LICENSES/`.

| Bestandteil | Version | Lizenz | Lizenztext |
|---|---|---|---|
| [jsPDF](https://github.com/parallax/jsPDF) | 2.5.2 | MIT | [LICENSES/jsPDF-MIT.txt](LICENSES/jsPDF-MIT.txt) |
| [html2canvas](https://html2canvas.hertzen.com) | 1.4.1 | MIT | [LICENSES/html2canvas-MIT.txt](LICENSES/html2canvas-MIT.txt) |
| [Oswald](https://github.com/googlefonts/OswaldFont) | v57 | SIL OFL 1.1 | [LICENSES/Oswald-OFL-1.1.txt](LICENSES/Oswald-OFL-1.1.txt) |

## Wo sie stecken

- **jsPDF** und **html2canvas** liegen unverändert in `vendor/`. Beide tragen
  ihren Lizenzkopf in der Datei selbst — der darf beim Aktualisieren nicht
  wegoptimiert werden.
- **Oswald** (Copyright 2016 The Oswald Project Authors) liegt als
  `tools/oswald-latin.woff2` bei und steckt zusätzlich als Base64 in den
  erzeugten Dateien `assets.css` und `fonts-pdf.js`. Für `fonts-pdf.js` wird
  die Schrift auf feste Strichstärken festgezurrt und auf die benötigten
  Zeichen gekürzt — solche Bearbeitungen erlaubt die OFL ausdrücklich, das
  Ergebnis steht weiterhin unter der OFL. Der Name „Oswald" ist kein Reserved
  Font Name, die bearbeitete Fassung darf ihn also behalten.
- Die OFL erlaubt das Einbetten der Schrift in Dokumente ausdrücklich. Die vom
  Generator erzeugten PDF-Dateien dürfen daher ohne weitere Auflagen
  weitergegeben werden.

Nicht ausgeliefert und deshalb hier ohne Belang: `fonttools` und `brotli`
(beide MIT) werden nur lokal gebraucht, um `tools/embed-assets.py` laufen zu
lassen.

## Nicht abgedeckt: die Vorlagengrafik

`Hintergrund.jpg` ist keine freie Bibliothek, sondern das gestaltete Flyer-Motiv.
Was damit erlaubt ist, richtet sich nach der Vereinbarung mit dem Urheber bzw.
nach der Lizenz der darin verwendeten Stockfotos — und nicht nach diesem
Dokument. Das gilt besonders, weil die Datei in diesem öffentlichen Repository
für jeden herunterladbar ist.
