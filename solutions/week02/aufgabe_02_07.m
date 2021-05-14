% Aufgabe 2.7  Fläche und Umfang eines Kreises
% Schreiben Sie ein Programm, das den Benutzer nach dem Radius eines 
% Kreises fragt und anschließend Fläche und Umfang des Kreises ausgibt.

% Eingabe
radius = input('Bitte geben Sie den Radius ein: ');

% Verarbeitung
A = pi * radius^2;
U = 2 * pi * radius; 

% Ausgabe
disp('Die Fläche des Kreises ist: ')
disp(A)
disp('Der Umfang des Kreises ist: ')
disp(U)