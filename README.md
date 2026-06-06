# MyPictureArt

Ein experimentelles Python-Projekt zur künstlerischen Transformation von Fotografien.

## Projektidee

Ausgangspunkt ist die Frage:

> Können einfache mathematische Transformationen interessante künstlerische Effekte erzeugen?

Anstatt komplexe KI-Modelle zu verwenden, werden zunächst klassische Bildverarbeitungsmethoden untersucht.

Der Fokus liegt auf:

* Porträtfotografie
* Strukturverstärkung
* Kontrastmanipulation
* künstlerischen Effekten
* reproduzierbaren Experimenten

---

## Projektstruktur

```text
MyPictureArt/

├── data/
│   ├── raw/
│   ├── intermediate/
│   └── output/
│
├── docs/
├── examples/
├── notebooks/
│
├── src/
│   ├── io/
│   ├── transformations/
│   ├── utils/
│   └── visualization/
│
├── tests/
│
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

## Experiment 01 – Bin Stretch Art

### Grundidee

Jeder RGB-Kanal wird in mehrere Intensitätsbereiche (Bins) unterteilt.

Jeder Bereich wird anschließend unabhängig wieder auf den vollen Wertebereich von 0 bis 255 gestreckt.

Beispiel bei 5 Bins:

```text
0-51     -> 0-255
51-102   -> 0-255
102-153  -> 0-255
153-204  -> 0-255
204-255  -> 0-255
```

Dadurch entstehen neue Strukturen, Konturen und Farbmuster.

---

## Erste Ergebnisse

Für das erste untersuchte Porträtbild erwiesen sich folgende Varianten als besonders interessant:

* 2 Bins
* 3 Bins
* 4 Bins

Zusätzlich entstand bei 5 Bins ein eigener Stil mit deutlich stärkeren Mikromustern.

Beobachtete Effekte:

* detailliertere Himmelsstrukturen
* neue Texturen in Kleidung
* veränderte Hautstrukturen
* künstlerische Konturbildung

---

## Aktueller Status

Version: 0.1

Abgeschlossen:

* Projektstruktur
* Entwicklungsumgebung
* Bildimport
* Histogrammanalyse
* Bin-Stretch-Transformation
* RGB-Transformation
* Parameterstudien
* Speicherung der Ergebnisse

Geplante Experimente:

* weitere Strukturtransformationen
* kanalabhängige Transformationen
* Vergleich mehrerer Bildtypen
* automatisierte Bewertung künstlerischer Effekte
* Machine-Learning-basierte Parametersuche

---

## Motivation

Das Projekt dient gleichzeitig als:

* Lernprojekt für Bildverarbeitung
* Forschungsprojekt für kreative Transformationen
* Vorbereitung für spätere Machine-Learning-Experimente
* GitHub-Portfolio-Projekt

```
```
