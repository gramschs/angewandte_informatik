% Aufgabe 7.6 
% 
% Schon zweimal haben wir uns mit den Alkali-Metallen beschäftigt 
% (siehe Aufgabe 3.7 und 4.12). Alkalimetalle sind die Stoffe Lithium (Li), 
% Natrium (Na), Kalium (K), Rubidium (Rb), Caesium (Cs). Schreiben Sie ein 
% Programm, das Folgendes leistet: Der Benutzer gibt die Formel eines 
% chemischen Elementes an. Anschließend wird gemeldet, ob es sich um ein 
% Alkalimetall handelt oder nicht. 
% Verwenden Sie diesmal ein Array mit den Alkalimetallen.

% Eingabe
eingabe = input('Bitte geben Sie Ihr chemisches Element ein: ','s');

% Ausgabe
if contains(['Li', 'Na', 'K', 'Rb', 'Cs'], eingabe) == true
    fprintf('%s ist ein Alkalimetall.', eingabe);
else
    fprintf('%s ist *kein* Alkalimetall.', eingabe);
end