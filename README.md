# Game of Life: Factsheet

## Einführung

- entwickelt von dem Mathematiker J.H. Conway in 1970
- basiert auf zweidimensionalen zellulären Automaten
  - d.h. eigener Zustand zu Zeitpunkt t+1 hängt von eigenen Zustand und dem der Nachbarschaft zu Zeitpunkt t ab
  - modellieren räumlich diskrete dynamische Systeme
- "Spiel" = Geschehen, das nach festgelegten einfachen Regeln abläuft

## Spielfeld

- Spielfeld besteht aus Zeilen und Spalten
- jedes Gitterquadrat (Zelle) ist ein zellulärer Automat
- eine Zelle kann zwei Zustände einnehmen (aktiv oder inaktiv)

## Spielregeln
- eine inaktive Zelle mit genau drei aktiven Nachbarn wird aktiv (Geburt)
- eine aktive Zelle mit weniger als zwei aktiven Nachbarn wird inaktiv (Einsamkeit)
- eine aktive Zelle mit zwei oder drei aktiven Nachbarn bleibt aktiv
- eine aktive Zelle mit mehr als drei aktiven Nachbarn wird inaktiv (Überbevölkerung)



