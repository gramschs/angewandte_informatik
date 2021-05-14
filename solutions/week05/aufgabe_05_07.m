% Aufgabe 5.7
%
% Erweitern Sie das Programm aus Aufgabe 5.6 mit der Einmaleins-Tabelle so, 
% dass sich ein Benutzer aussuchen darf, welche Spalte ausgegeben wird. 
% Wenn der Benutzer sich für die 6 entscheidet, wird 1 x 6 = 6, 2 x 6 = 12, 
% 3 x 6 = 18, usw. bis 10 x 6 = 60 ausgegeben.

% Eingabe
spalte = input('Welche Spalte soll ausgegeben werden? ');

% Ausgabe
for i = 1:10
    fprintf('%g x %g = %g \n', i, spalte, i*spalte)
end

