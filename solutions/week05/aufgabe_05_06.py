'''
Aufgabe 5.6

Schreiben Sie ein Programm, das eine Einmaleins-Tabelle bis zu 10x10 ausgibt. Also

1 x 1 = 1
2 x 1 = 2
3 x 1 = 3

usw.
'''

for i in range(1,11):
    for j in range(1,11):
        print('{} x {} = {}'.format(i, j, i*j))
    print('\n')
