Aufgabe 7.8

Entwickeln Sie für einen Küchenroboter einen Algorithmus zum Kochen von Spaghetti 
Bolognese (z.B. mit diesem Rezept hier: 
https://www.chefkoch.de/rezepte/393031127655461/Spaghetti-Bolognese.html). 
Formulieren sie das Rezept in Pseudocode. Bedenken Sie dabei, dass der Roboter Anweisungen 
wir langsam erhitzen übersetzt bekommen muss a la

Pfanne auf Herdplatte 1 stellen
Hackfleisch in Pfanne legen
Herdplatte 1 auf Stufe 9 schalten
messe Temperatur Herdplatte Herdplatte 1
T = Temperatur Herdplatte 1
solange T < 100 °C:
    messe Temperatur
    T = Temperatur Herdplatte 1
    mache 10 Sekunden Pause 
schalte Herdplatte 1 auf Stufe 3

usw. Führen Sie Variablen ein, so dass Sie am Anfang abfragen können, für wie viele Personen 
gekocht werden soll.

frage, für wie viele Personen gekocht werden soll
N = Anzahl Personen
für Zutat [Zwiebel, Knoblauch, Möhre]:
    hole N * 1/4 Zutat
    schäle Zutat
    schneide Zutat in 0.5 cm^3 Würfelstücke
hole Pfanne und stelle sie auf Herdplatte 1
gebe 1 Esslöffel Öl in Pfanne
schalte Herdplatte 1 auf höchste Stufe
warte 2 Minuten    
hole N * 125 g Hackfleisch und lege es in Pfanne
schalte Herdplatte auf höchste Stufe
messe Temperatur Herdplatte Herdplatte 1
T = Temperatur Herdplatte 1
solange T < 100 °C:
    messe Temperatur
    T = Temperatur Herdplatte 1
    mache 10 Sekunden Pause 
schalte Herdplatte 1 auf niedrige Stufe
beurteile Farbe des Hackfleischs
solange Farbe Hackfleisch nicht braun:
    brate Hackfleisch weiter an
für Zutat [Salz, Pfeffer]:
    hole Zutat
    gebe 1/2 Teelöffel der Zutat in die Pfanne
rühre 10 x um
schütte die Stücke der geschnitten Zutaten [Zwiebel, Knoblauch, Möhre] in Pfanne
rühre 10 x um
schütte N * 50 ml Gemüsebrühe in Pfanne
schütte N * 17,5 g Tomatenmark in Pfanne
schütte N * 1/4 Oregano in Pfanne
schütte N * 100 g stückige Tomaten in Pfanne
schütte N * 1/2 EL Tomatenketchup in Pfanne
schalte Herdplatte auf niedrigste Stufe
warte 20 min
fülle 3 l Wasser in Topf
stelle Wasser-Topf auf Herdplatte 2  
schalte Herdplatte 2 auf höchste Stufe
beobachte Wasseroberfläche
solange Wasseroberfläche glatt:
    beobachte Wasseroberfläche
    warte 30 Sekunden
schütte N * 125 g Spaghetti-Nudel in Wasser-Topf
schalte Herdplatte 2 auf mittlere Stufe
warte 10 min
schalte Herdplatte 2 auf Null
nehme Topf mit Wasser und Spaghetti
schütte Topf-Inhalt in Sieb
schalte Herdplatte 1 auf Null
verteile Sieb-Inhalt auf N Teller
verteile Pfannen-Inhalt auf N Teller
gebe aus: "Guten Appetit!"