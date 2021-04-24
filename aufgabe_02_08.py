'''
Aufgabe 2.8 Kostenkalkulation Urlaubsreise (nach Weigend, Python 3, Kapitel 3)

Schreiben Sie ein Programm, das die Kosten für eine Urlaubsreise für eine Reisegruppe mit einem Bus berechnet.
Vom Benutzer werden folgende Angaben erfragt:

* Anzahl der Personen,
* Hotelkosten pro Person,
* Gesamtkosten für den Reisebus,
* Gesamtkosten für touristische Events am Zielort,
* sonstige Kosten pro Person.

Ausgegeben werden die Gesamtkosten der Fahrt und der Betrag, den jeder Teilnehmer zahlen muss. Möglicher Programmlauf:

Kostenplan für eine Reise
---------------------------
Kosten für den Reisebus: 1000
Hotelkosten pro Person: 300
Gesamtkosten für touristische Events: 500
Anzahl der Teilnehmer: 30

Die Gesamtkosten betragen 10500 EUR. Die Kosten pro Person sind 350 EUR.

Hinweise: Machen Sie sich erstmal einen Plan, welche Eingaben abgefragt werden müssen, wie diese verarbeitet werden
sollen und was das Programm am Ende ausgeben soll. Danach implementieren Sie Ihren Algorithmus.  Achten Sie auf guten
Programmierstil. Verwenden Sie »sprechende« Variablennamen. Setzen Sie die Funktion input() für die Eingabe der
Zahlenwerte ein und denken Sie an die Umwandlung in einen Integer, falls Sie Python verwenden.
'''

print("Kostenplan für eine Reise")
print("-------------------------")


# Eingabe
personen = int(input("Anzahl der Teilnehmer: "))
hotel_kosten = float(input("Hotelkosten pro Person: "))
bus_kosten = int(input("Gesamtkosten für den Reisebus: "))
event_kosten = float(input("Gesamtkosten für touristische Events: "))
sonstige_kostigen = int(input("Sonstige Kosten pro Person: "))


# Verarbeitung
gesamt_kosten = personen * hotel_kosten + personen * sonstige_kostigen + bus_kosten + event_kosten
kosten_pro_person = gesamt_kosten / personen


# Ausgabe
print()
print("Die Gesamtkosten betragen", gesamt_kosten, "EUR.")
print("Die Kosten pro Person sind", kosten_pro_person, "EUR.")