# Aufgabe 3.4
#
# Schreiben Sie ein Programm, dass den Benutzer nach seinem Geburtsjahr fragt. Danach rechnet das Programm aus, wie alt
# der Benutzer dieses Jahr wird. Wenn der Benutzer dieses Jahr volljährig wird, soll das Programm ausgeben: "Hurra, Sie
# werden oder wurden dieses Jahr volljährig!" Wenn der Benutzer schon volljährig ist, soll das Programm ausgeben: "Sie
# sind bereits volljährig."

# Eingabe
geburtsjahr = int(input('In welchem Jahr wurden Sie geboren? '))

# Verarbeitung: berechne Alter
aktuelles_jahr = 2021
alter = aktuelles_jahr - geburtsjahr

# Ausgabe
if alter == 18:
    print('Hurra, Sie werden oder wurden dieses Jahr volljährig!')

if alter > 18:
    print('Sie sind bereits volljährig.')