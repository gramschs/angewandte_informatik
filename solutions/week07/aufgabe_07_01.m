% Aufgabe 7.1
% Schreiben Sie Code, der Ihren Vornamen abfragt und anschließend die Länge 
% Ihres Vornamens bestimmt.
% Tipp: wird die Funktion input mit dem zusätzlichen Argument 's' 
% aufgerufen, so wird die Eingabe als String interpretiert, also 
% input('Fragetext', 's').

% Eingabe
name = input('Bitte geben Sie Ihren Vornamen ein: ','s');

% Verarbeitung
laenge = strlength(name);

% Ausgabe
fprintf('Ihre Vorname hat %g Zeichen.', laenge)