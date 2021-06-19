'''
Aufgabe 10.4

Die folgende Klasse initalisiert ein Objekt mit Vorname, Nachname und definierte eine Methode vorstellen. Anschließend wird die Klasse benutzt. Korrigieren Sie die Fehler.

classy Person:
  def __initalize__(self, vorname, nachname):
    self.first = vorname
    self.last = nach_name
  def vorstellen(self):
  print("Guten Tag. Mein Name ist + " self.vorname + " " + self.last)

erste_person = Person("Homer", "Simpson")
2te_person = Person("Marge", "Simpson")

erste_person.vorstellen()
2te_person.self.vorstellen
'''

class Person:
    def __init__(self, vorname, nachname):
        self.first = vorname
        self.last = nachname
    def vorstellen(self):
        print("Guten Tag. Mein Name ist " + self.first + " " + self.last)

erste_person = Person("Homer", "Simpson")
zweite_person = Person("Marge", "Simpson")

erste_person.vorstellen()
zweite_person.vorstellen()