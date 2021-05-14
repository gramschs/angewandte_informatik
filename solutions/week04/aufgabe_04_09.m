% Aufgabe 4.9
% 
% Erweitern Sie Programm 4.8 so, dass erst überprüft wird, ob die 
% eingegebene Zahl b auch wirklich größer als a ist.
% Wenn dies nicht der Fall ist, soll solange weiter nach einer Zahl b 
% gefragt werden, bis diese größer als a ist.
%
% Testen Sie Ihr Programm für die Beispiele a=4 und b=10 und anschließend 
% für a=10 und b=4.

% Eingabe
a = input('Bitte geben Sie eine minimale Zahl a ein: ');
b = input('Bitte geben Sie eine maximale Zahl b ein: ');

while b <= a
    b = input('b muss echt größer als a sein, bitte nochmal b eingeben: ');
end

% Verarbeitung und Ausgabe
while a <= b
    disp(a^2)
    a = a + 1;
end