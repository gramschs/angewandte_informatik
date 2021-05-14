% Aufgabe 3.8
%
% Schreiben Sie ein Programm, welches eine Zeitangabe in Stunden, Minuten und Sekunden in die Anzahl Sekunden insgesamt
% umrechnet und ausgibt.


% Eingabe
disp('Bitte geben Sie im folgenden die Stunden, Minuten und Sekunden ein.')
stunden  = input('Stunden: ')
minuten  = input('Minuten: ')
sekunden = input('Sekunden: ')

% Verarbeitung
zeit_in_sekunden = 3600 *  stunden + 60 * minuten + sekunden;

% Ausgabe
fprintf('Das entspricht %f Sekunden.', zeit_in_sekunden);