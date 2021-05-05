% Aufgabe 3.7 (nach Weigend, Python 3, Kapitel 5)
%
% Alkalimetalle sind die Stoffe Lithium (Li), Natrium (Na), Kalium (K), Rubidium (Rb), Caesium (Cs). Schreiben Sie ein
% Programm, das Folgendes leistet: Der Benutzer gibt die Formel eines chemischen Elementes an. Anschließend wird
% gemeldet, ob es sich um ein Alkalimetall handelt oder nicht.
%
% Beispieldialog:
%
% Bitte geben Sie die Formel eines chemischen Elementes an. Element: Na
% Es handelt sich um ein Alkalimetall.

% Eingabe
chemische_formel = input('Bitte geben Sie die Formel Ihres chemischen Elementes an: ');

% Ausgabe
if chemische_formel == 'Li'
    disp('Ist ein Alkalimetall.')
elseif chemische_formel == 'Na'
    disp('Ist ein Alkalimetall.')
elseif chemische_formel == 'K'
    disp('Ist ein Alkalimetall.')
elseif chemische_formel == 'Rb'
    disp('Ist ein Alkalimetall.')
elseif chemische_formel == 'Cs'
    disp('Ist ein Alkalimetall.')
else
    disp('Ist *kein* Alkalimetall.')
end
