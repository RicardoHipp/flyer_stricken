# Stricktreff-Flyer

`index.html` doppelklicken — fertig. Kein Server, kein Internet nötig.

Links Termine eintragen, rechts entsteht der Flyer live. Alle Eingaben bleiben im
Browser gespeichert, beim nächsten Öffnen ist alles wieder da.

## PDF

**PDF herunterladen** legt die fertige Datei im Download-Ordner ab, ohne
Rückfragen. Eine Seite **200 × 300 mm**, randlos — das Seitenverhältnis der
Vorlage. Auf A4 gedruckt bleibt oben und unten ein schmaler weißer Rand; wer A4
randfüllend braucht, sagt Bescheid.

(Strg+P funktioniert weiterhin und setzt dieselbe Seite; im Dialog dann die
Ränder auf „Keine" stellen.)

Der Download rastert den Flyer **nicht** ab, sondern baut das PDF nach:
`Hintergrund.jpg` wird Byte für Byte unverändert eingebettet (kein Hochrechnen,
kein zweites Komprimieren) und der Text als echter Vektortext mit eingebetteter
Schrift gesetzt — beliebig scharf, egal wie weit man hineinzoomt. Die Geometrie
liest er dafür aus der fertig gerenderten Vorschau aus, es gibt also nur eine
Layout-Quelle: das CSS. Falls das mal scheitert, fällt er still auf den alten
Bild-Weg (300 dpi) zurück.

## Wenn Text verrutscht ist

In `index.html` ganz oben im Block **„1. JUSTIERUNG"** stehen alle Positionen,
Größen und Farben als CSS-Variablen. Nur dort schrauben. Zum Zielen die Checkbox
**„Textflächen anzeigen"** unten im Formular anhaken — dann werden die beiden
Textflächen rot umrandet.

## Hintergrundbild austauschen

Neue Datei genau so benennen — `Hintergrund.jpg` — und die alte im Ordner
überschreiben, Seitenverhältnis 2:3 beibehalten. Dann **`Hintergrund
aktualisieren.bat`** doppelklicken (oder `python tools/embed-assets.py`) und
`index.html` neu laden.

Der Umweg ist nötig, weil das Bild nicht über den Dateipfad geladen wird,
sondern als data:-URI in `bg-data.js` steckt — sonst würde der Direkt-Download
beim Öffnen per Doppelklick am Canvas-Schutz des Browsers scheitern.

Braucht `pip install fonttools brotli` (nur für die Schriften; ohne das werden
Bild und CSS trotzdem neu gebaut).

Die Vorlage hat 1684 × 2528 px, auf 200 mm sind das rund 214 dpi — für Aushang
und Digitaldruck gut. Das Bild kann nie schärfer werden als die Datei; der
eingesetzte *Text* ist davon nicht betroffen, der ist immer Vektor.

## Dateien

- `index.html` — die ganze Anwendung
- `assets.css` — erzeugt: Schrift Oswald als data:-URI (Anzeige)
- `bg-data.js` — erzeugt: Hintergrundbild als data:-URI
- `Hintergrund aktualisieren.bat` — baut die drei erzeugten Dateien neu
- `fonts-pdf.js` — erzeugt: Oswald 400/600/700 als TrueType (PDF-Export)
- `tools/embed-assets.py` — erzeugt die drei
- `tools/oswald-latin.woff2` — Schriftquelle (SIL Open Font License)
- `vendor/` — jsPDF, dazu html2canvas für die Rückfallebene
- `Hintergrund.jpg` — Vorlage
