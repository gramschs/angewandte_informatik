'''
Aufgabe 8.9

Implementieren Sie eine Klasse Datum. Diese Klasse speichert Tag, Monat und Jahr als Attribut.

Implementieren Sie Methoden, die diese Attribute verändern können. Dabei soll die Methode per Print()-Funktion warnen,
wenn eine nicht zulässige Zahl verwendet wird und dann nicht die Änderung durchführen.
Implementieren Sie eine Methode get_datum_deutsch(), die das Datum als String nach dem Muster TT.MM.JJJJ zurückgibt,
also z.B. '07.06.2021'.
Implementieren Sie eine Methode get_datum_britisch(), die das Datum als String nach dem Muster TT/MM/JJJJ zurückgibt,
also z.B. '07/06/2021'.
Implementieren Sie eine Methode get_datum_amerikanisch(), die das Datum als String nach dem Muster MM/TT/JJJJ
zurückgibt, also z.B. '06/07/2021'.
'''

class Datum:
    def __init__(self, tag, monat, jahr):
        self.tag = tag
        self.monat = monat
        self.jahr = jahr

    def set_tag(self, tag):
        if (1 <= tag)  and (tag <= 31):
            self.tag = tag
        else:
            print('Sie haben einen unzulässigen Tag angegeben, der Tag muss zwischen 1 und 31 liegen.')

    def set_monat(self, monat):
        if (1<=monat) and (monat <= 12):
            self.monat = monat
        else:
            print('Sie haben einen unzulässigen Monat angegeben, der Monat muss zwischen 1 und 12  liegen.')

    def get_datum_deutsch(self):
        string = '{}.{}.{}'.format(self.tag, self.monat, self.jahr)
        return string

    def get_datum_britisch(self):
        string = '{}/{}/{}'.format(self.tag, self.monat, self.jahr)
        return string

    def get_datum_amerikanisch(self):
        string = '{}/{}/{}'.format(self.monat, self.tag, self.jahr)
        return string

# Test
heute = Datum(0,8,2021)

heute.set_tag(32)
heute.set_tag(7)
print(heute.get_datum_deutsch())
print(heute.get_datum_britisch())
print(heute.get_datum_amerikanisch())