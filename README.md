# PixelAlchemy

**Transforming Pixels into Unexpected Art through Mathematical Image Experiments**

Ein experimentelles Python-Projekt zur Erforschung künstlerischer Bildtransformationen.

## Projektidee

Ausgangspunkt ist die Frage:

> Können einfache mathematische Transformationen interessante und unerwartete künstlerische Effekte erzeugen?

Anstatt komplexe KI-Modelle oder neuronale Netze einzusetzen, untersucht PixelAlchemy zunächst klassische Methoden der Bildverarbeitung und experimentiert mit deren kreativem Potenzial.

Im Mittelpunkt steht die Verbindung von:

* Bildverarbeitung
* kreativer Programmierung
* experimenteller Kunst
* reproduzierbarer Forschung

Der Fokus liegt auf:

* Porträtfotografie
* Strukturverstärkung
* Kontrastmanipulation
* künstlerischen Effekten
* visueller Exploration
* reproduzierbaren Experimenten

---

## Philosophie

PixelAlchemy versteht Bildverarbeitung nicht nur als technisches Werkzeug, sondern auch als kreativen Forschungsprozess.

Jedes Experiment beginnt mit einer einfachen mathematischen Idee. Durch systematische Variation von Parametern wird untersucht, welche visuellen Strukturen, Muster und ästhetischen Effekte daraus entstehen.

Das Projekt dokumentiert sowohl erfolgreiche als auch unerwartete Ergebnisse und versteht sich als offenes Labor für algorithmische Bildkunst.

---

## Projektstruktur

```text
MyPictureArt/
│
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

![Experiment 01 - Bin Stretch Art](docs/images/experiment_01_collage.jpg)

*Von links oben nach rechts unten: 2, 3, 4 und 5 Bins.*

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
