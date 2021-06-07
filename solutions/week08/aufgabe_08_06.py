'''
Aufgabe 8.6

Fügen Sie Ihrer Klasse zum Verwalten von Studierenden (siehe Aufgabe 8.4) zwei Print-Funktionen hinzu. Die erste
Print-Funktion soll in einer Zeile Vorname Nachname (xxxxxx) ausgeben, wobei das xxxxxx für die Matrikel-Nummer steht,
also z.B.

Alice Wunderland (123456)

ausgeben. Die zweite soll Nachname, Vorname (Matrikel-Nummer: xxxxxx) ausgeben, also z.B.

Wunderland, Alice (Matrikel-Nummer: 123456)
'''

class Studierende:
    def __init__(self, vorname, nachname, matrikelnummer):
        self.vorname = vorname
        self.nachname = nachname
        self.matrikelnummer = matrikelnummer

    def print_vorname_nachname_matrikelnummer(self):
        print('{} {} (Matrikel-Nummer: {})'.format(self.vorname, self.nachname, self.matrikelnummer))

    def print_nachname_vorname_matrikelnummer(self):
        print('{}, {} (Matrikel-Nummer: {})'.format(self.nachname, self.vorname, self.matrikelnummer))


# Test der Klasse
Student1 = Studierende('Alice', 'Wunderland', 123456)
Student1.print_vorname_nachname_matrikelnummer()
Student1.print_nachname_vorname_matrikelnummer()

Student2 = Studierende('Bob', 'Baumeister', 234567)
Student2.print_vorname_nachname_matrikelnummer()
Student2.print_nachname_vorname_matrikelnummer()