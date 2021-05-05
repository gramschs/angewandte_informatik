# Aufgabe 3.9
#
# Ein Weinhändler verkauft Rotwein zu 12 Euro pro Flasche, Roséwein zu 10 und Weißwein zu 9 Euro pro Flasche. Ein Kunde
# bestellt (beispielsweise) 12 Flaschen Rotwein, 6 Flaschen Rosé und 24 Flaschen Weißwein. Schreiben Sie ein Programm,
# welches den Gesamtpreis berechnet und ausgibt.
#
# In einem zweite Schritt ändern Sie Ihr Programm, denn es kommen noch Portokosten dazu. Bei einem Bestellpreis unter 50
# Euro betragen die Portokosten 13,95 Euro. Zwischen 50 und 100 Euro muss der Kunde 4,95 Euro Porto bezahlen. Ab einem
# Bestellpreis von 100 Euro gibt es keine Portokosten mehr.

# Eingabe
anzahl_rotwein = int(input('Anzahl Rotweinflaschen: '))
anzahl_rosewein = int(input('Anzahl Roseweinflaschen: '))
anzahl_weisswein = int(input('Anzahl Weissweinflaschen: '))


# Verarbeitung
# setze Preis pro Flasche fest:
preis_rotwein = 12
preis_rosewein = 10
preis_weisswein = 9

# berechne die Kosten für den Kauf der Flaschen
flaschen_kosten = anzahl_rotwein * preis_rotwein + anzahl_rosewein * preis_rosewein + anzahl_weisswein * preis_weisswein
if flaschen_kosten < 50:
    porto_kosten = 13.95
elif flaschen_kosten < 100:
    porto_kosten = 4.95
else:
    porto_kosten = 0
gesamt_kosten = flaschen_kosten + porto_kosten

# Ausgabe
print('Die Gesamtkosten sind {} Euro.'.format(gesamt_kosten))