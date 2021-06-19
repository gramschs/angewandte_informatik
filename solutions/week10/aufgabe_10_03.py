'''
Aufgabe 10.3

Ein Zeitreisender kommt auf Sie zu. Fragen Sie ihn nach dem Jahr, aus dem er kommt und begrüßen Sie ihn. Falls er aus
einem Jahr vor 1900 kommt mit "Sie kommen ja aus der Vergangenheit!", zwischen 1900 und 2021 mit "Sie stammen also aus
unserer Zeit!" und ansonsten mit "Können Sie mir die Lottozahlen von nächster Woche verraten?". Schreiben Sie als erstes
Ihr eigenes Programm in der nächsten Code-Zelle:
'''

jahr = int(input("Ein Zeitreisender??? Aus welchem Jahr kommen Sie denn? "))

if jahr <= 1900:
    print ('Sie kommen ja aus der Vergangenheit!')
elif jahr > 1900 and jahr < 2020:
    print("Sie stammen also aus unserer Zeit!")
else:
    print("Können Sie mir die Lottozahlen von nächster Woche verraten?")
