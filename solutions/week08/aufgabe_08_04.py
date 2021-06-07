'''
Aufgabe 8.4

Schreiben Sie eine Klasse, die Studierende mit den Eigenschaften

Vorname
Nachname
Matrikel-Nummer verwalten kann.
Testen Sie anschließend Ihre Klasse, indem Sie ein Beispiel ausprobieren.
'''
class Studierende:
    def __init__(self, vorname, nachname, matrikelnummer):
        self.vorname = vorname
        self.nachname = nachname
        self.matrikelnummer = matrikelnummer


# Test der Klasse
Student1 = Studierende('Alice', 'Wunderland', 123456)
Student2 = Studierende('Bob', 'Baumeister', 234567)
Student3 = Studierende('Charlie', 'Brown', 345678)

print(Student1.vorname)