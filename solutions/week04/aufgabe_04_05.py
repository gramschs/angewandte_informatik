'''
Aufgabe 4.5

Schreiben Sie das Programm für einen Ticket-Automaten. Der Benutzer wird nach dem Alter gefragt und ob ein
Schülerausweis vorliegt. Das Programm gibt dann aus, welches Ticket gekauft werden muss.

Alter                      | Ticket
-------------------------- | -------------
0 - 5                      | keine
6 - 14                     | Kinder-Ticket
15 - 21 und Schülerausweis | Kinder-Ticket
15 - 59                    | Erwachsenen-Ticket
ab 60                      | Senioren-Ticket
'''

alter = int(input('Bitte geben Sie Ihr Alter ein: '))
hat_schuelerausweis = input('Haben Sie einen Schülerausweis (j/n)?')

if alter <= 5:
    print('Sie brauchen kein Ticket.')
elif (6 <= alter) and (alter <= 14):
    print('Sie brauchen ein Kinder-Ticket.')
elif (15 <= alter) and (alter <= 21) and (hat_schuelerausweis == 'j'):
    print('Sie brauchen ein Kinder-Ticket.')
elif (15 <= alter) and (alter <= 59):
    print('Sie brauchen ein Erwachsenen-Ticket.')
else:
    print('Sie brauchen ein Senioren-Ticket.')