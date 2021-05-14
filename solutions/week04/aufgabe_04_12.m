% Aufgabe 4.12
% 
% Aufgabe 3.7 lautete:
% 
% Alkalimetalle sind die Stoffe Lithium (Li), Natrium (Na), Kalium (K), 
% Rubidium (Rb), Caesium (Cs). Schreiben Sie ein Programm, das Folgendes 
% leistet: Der Benutzer gibt die Formel eines chemischen Elementes an. 
% Anschließend wird gemeldet, ob es sich um ein Alkalimetall handelt oder 
% nicht.
%
% Schreiben Sie Ihr Programm aus Aufgabe 3.7 so um, dass nur noch _eine_ 
% if - else - Struktur ohne elseif verwendet wird, indem Sie logische 
% Operatoren einsetzen.

% Eingabe
chemische_formel = input('Bitte geben Sie die Formel Ihres chemischen Elementes an: ');

% Ausgabe
if (chemische_formel == 'Li') | (chemische_formel == 'Na') | (chemische_formel == 'K') | (chemische_formel == 'Rb') | (chemische_formel == 'Cs')
    fprintf('%s ist ein Alkalimetall.', chemische_formel)
else
    fprintf('%s ist *kein* Alkalimetall.', chemische_formel)
end


