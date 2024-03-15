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

## Quellen
- Conway's Spiel des Lebens: https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens
- Das Spiel des Lebens: https://www.youtube.com/watch?v=DUfdBdrK2ag

## Video
- "Spiel" 1970 erschienen in Scientific American (evtl. Buch Abbildung)
- Spielfeld ist ein unendliches Schachbrett
  - jedes Feld kann zwei Zustände annehmen -> aktiv/inaktiv
- Spiel ohne Spieler -> "Zero Player Game"
- konzipiert als Spielbar auf Go-Brett oder mit "Stift, Papier und Radiergummi" -> volles Potenzial erst mit Computer
- in den 1970ern so beliebt, dass Kosten für verwendete Rechenzeit mehrere Millionen Dollar betrug
- Spiel in Familie der zellulären Automaten
  - Geschichte der zellulären Automaten: nach 1945 Idee des elektronischen Gehirns
  - Erfindung einer Wissenschaft, die auf Informationen beruht -> Kybernetik
  - John von Neumann (beteiligt am ersten Computer) möchte Leben, insbesondere Fortpflanzung, mithilfe komplexer Mathematik modellieren
    - theoretische Frage: Könnte eine Maschine eine funktionsfähige Kopie von sich selbst erstellen?
  - dabei stößt er auf eine einfachere und abstraktere Idee -> zelluläre Automat 
    - = vereinfachte Welt aus identischen Zellen mit verschiedenen Zuständen
    - Zustände ändern sich nach festen Regeln
  - diese einfachere Umgebung vereinfacht die Selbstreproduktion 
    - z.B. erstelle eine Kopie von dir wenn x
  - John von Neumann gelingt es zu zeigen, dass eine Selbstreproduktion von komplexen Systemen theoretisch möglich ist
    - vollständige Theorie durch frühen Tod nie veröffentlicht (erst posthum) (evtl. Buch Abbildung "Theory of self-reproducing automata")
- Buch von John von Neumann inspiration für John Conway (Mathematiker)
  - im Gegensatz zu Systemen interessiert er sich für konkrete manipulierbare Dinge als experimental Mathematiker (z.B. Spiele)
- nutzt Neumanns Theorie (System) als Grundlage für Spiel
- für jede Zelle entscheidet die Anzahl ihrer Nachbarn zum Zeitpunkt t über ihren Zustand zum Zeitpunkt t+1 (siehe Regeln)
- große Fangemeinschaft zur Katalogisierung und Untersuchung der entstehenden Formen 
  - z.B. Stillleben, Oszillatoren, bewegende Formen 
- die meisten Startzustände führen zu einem statischen oder wiederkehrenden Zustand
  - Gibt es Konfigurationen, die zu einer unendlichen Ausdehnung führen?
  - Ja, z.B. Gleiterkanone
- diese Erkenntnis ermöglicht es Conway
  - logischee Schaltkreise von Computern zu bauen
  - Informationen von A nach B schicken
  - Informationen zu speichern
- damit Beweis, dass das Spiel des Lebens ein Universalcomputer ist
  - d.h. kann alle Operationen ausführen, die ein Computer ausführen kann
  - z.B. Kann das Spiel des Lebens mit dem Spiel des Lebens programmiert werden
- Anwendung 
  - Beobachtung physikalischer Phänomene (z.B. Diffusion von Gasen)
  - Beobachtung biologischer Prozesse (z.B. Ausbreitung Epidemie)
- Große Idee/Traum ging viel weiter
  - Leben verstehen, simulieren, erschaffen
  - Aussage von Conway: In einem ausreichend großen und zufällig ausgefüllten Gitter können alle Konfigurationen entstehen, unter diesen Konfigurationen (Milliarden) ist es vorstellbar, dass einige in der Lage sind sich zu reproduzieren, sich zu vermehren und weiterzuentwickeln und damit evtl. auch zu intelligenten Kreaturen zu werden
  - Dazu Hypothese von Konrad Zuse (Informatikpionier): Wenn Leben in einem zellulären Automaten entstehen kann, kann unsere Welt selbst eine Simulation sein, die von einem zellulären Automaten berechnet wird
  - Gegenhypothese: Naive Ansicht, dass sich eine Lebensform aus so simplen Systemen entwickeln könnte -> denn das System ist rein deterministisch und damit komplett vorhersehbar, das kann der aktuellen Wissenschaft nicht standhalten, welche Raum für nichtdeterministische Phänomene lässt
- Faszination: befindet sich zwischen den beiden verschiedenen Welten
  - veranschaulicht wie einfache und deterministische Regeln zu komplexen und scheinbar unvorhersehbaren Phänomenen führen können
- Fazit: Das Spiel des Lebens zeigt, das ein riesiges komplexes, hoch organisiertes Universum kann aus einfachen Regeln entstehen

