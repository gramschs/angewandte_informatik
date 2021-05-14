% Aufgabe 4.8

% Schreiben Sie ein Programm, das eine minimale Zahl a und eine maximale 
% Zahl b abfragt. Dann berechnet das Programm die Quadratzahlen von a^2 bis
% b^2 und gibt diese aus.

% Eingabe
a = input('Bitte geben Sie a an: ');
b = input('Bitte geben Sie b an: ');

% Verarbeitung und Ausgabe
while a <= b
    disp(a^2)
    a = a + 1;
end