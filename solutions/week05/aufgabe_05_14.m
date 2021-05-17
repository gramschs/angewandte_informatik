% Aufgabe 5.14 Lotto
% 
% Schreiben Sie ein Programm, das zuerst den Benutzer sechs Zahlen zwischen 1 und 49 wählen lässt. Dabei soll das Programm
% überprüfen, dass keine Zahl mehrfach eingegeben wird. Lassen Sie dann den Zufallszahlengenerator sechs Lottozahlen
% zwischen 1 und 49 ziehen (Hinweis: randi([1 49]) ). Dabei darf ebenfalls keine Zufallszahl mehrfach
% gezogen werden. Teilen Sie dem Benutzer anschließend mit, wie viele richtige Zahlen getippt wurden.

% Eingabe

zahl1 = zahl_abfragen();
zahl2 = zahl_abfragen();
while zahl2 == zahl1
    fprintf('Sie haben die Zahl %g schon gewählt. Bitte wählen Sie eine andere Zahl. ', zahl1);
    zahl2 = zahl_abfragen();
end

zahl3 = zahl_abfragen();
while (zahl3 == zahl2) || (zahl3 == zahl1)
    fprintf('Sie haben bereits die Zahlen %g und %g gewählt. Bitte wählen Sie eine andere Zahl. ', zahl1, zahl2);
    zahl3 = zahl_abfragen();
end

zahl4 = zahl_abfragen();
while (zahl4 == zahl3) || (zahl4 == zahl2) || (zahl4 == zahl1)
    fprintf('Sie haben bereits die Zahlen %g, %g und %g gewählt. Bitte wählen Sie eine andere Zahl. ', zahl1, zahl2, zahl3);
    zahl4 = zahl_abfragen();
end

zahl5 = zahl_abfragen();
while (zahl5 == zahl4) || (zahl5 == zahl3) || (zahl5 == zahl2) || (zahl5 == zahl1)
    fprintf('Sie haben bereits die Zahlen %g, %g, %g und %g gewählt. Bitte wählen Sie eine andere Zahl. ', zahl1, zahl2, zahl3, zahl4);
    zahl5 = zahl_abfragen();
end

zahl6 = zahl_abfragen();
while (zahl6 == zahl5) || (zahl6 == zahl4) || (zahl6 == zahl3) || (zahl6 == zahl2) || (zahl6 == zahl1)
    fprintf('Sie haben bereits die Zahlen %g, %g, %g, %g und %g gewählt. Bitte wählen Sie eine andere Zahl. ', zahl1, zahl2, zahl3, zahl4, zahl5);
    zahl6 = zahl_abfragen();
end

% Verarbeitung

zufallszahl1 = randi([1 49]);
zufallszahl2 = randi([1 49]);
while zufallszahl2 == zufallszahl1
    zufallszahl2 = randi([1 49]);
end
zufallszahl3 = randi([1 49]);
while (zufallszahl3 == zufallszahl2) || (zufallszahl3 == zufallszahl1)
    zufallszahl3 = randi([1 49]);
end
zufallszahl4 = randi([1 49]);
while (zufallszahl4 == zufallszahl3) || (zufallszahl4 == zufallszahl2) || (zufallszahl4 == zufallszahl1)
    zufallszahl4 = randi([1 49]);
end
zufallszahl5 = randi([1 49]);
while (zufallszahl5 == zufallszahl4) || (zufallszahl5 == zufallszahl3) || (zufallszahl5 == zufallszahl2) || (zufallszahl5 == zufallszahl1)
    zufallszahl5 = randi([1 49]);
end
zufallszahl6 = randi([1 49]);
while (zufallszahl6 == zufallszahl5) || (zufallszahl6 == zufallszahl4) || (zufallszahl6 == zufallszahl3) || (zufallszahl6 == zufallszahl2) || (zufallszahl6 == zufallszahl1)
    zufallszahl6 = randi([1 49]);
end

% Ausgabe
anzahl_richtige = 0;
if (zahl1 == zufallszahl1) || (zahl1 == zufallszahl2) || (zahl1 == zufallszahl3) || (zahl1 == zufallszahl4) || (zahl1 == zufallszahl5) || (zahl1 == zufallszahl6)
    anzahl_richtige = anzahl_richtige + 1;
end
if (zahl2 == zufallszahl1) || (zahl2 == zufallszahl2) || (zahl2 == zufallszahl3) || (zahl2 == zufallszahl4) || (zahl2 == zufallszahl5) || (zahl2 == zufallszahl6)
    anzahl_richtige = anzahl_richtige + 1;
end
if (zahl3 == zufallszahl1) || (zahl3 == zufallszahl2) || (zahl3 == zufallszahl3) || (zahl3 == zufallszahl4) || (zahl3 == zufallszahl5) || (zahl3 == zufallszahl6)
    anzahl_richtige = anzahl_richtige + 1;
end
if (zahl4 == zufallszahl1) || (zahl4 == zufallszahl2) || (zahl4 == zufallszahl3) || (zahl4 == zufallszahl4) || (zahl4 == zufallszahl5) || (zahl4 == zufallszahl6)
    anzahl_richtige = anzahl_richtige + 1;
end
if (zahl5 == zufallszahl1) || (zahl5 == zufallszahl2) || (zahl5 == zufallszahl3) || (zahl5 == zufallszahl4) || (zahl5 == zufallszahl5) || (zahl5 == zufallszahl6)
    anzahl_richtige = anzahl_richtige + 1;
end
if (zahl6 == zufallszahl1) || (zahl6 == zufallszahl2) || (zahl6 == zufallszahl3) || (zahl6 == zufallszahl4) || (zahl6 == zufallszahl5) || (zahl6 == zufallszahl6)
    anzahl_richtige = anzahl_richtige + 1;
end

fprintf('Sie haben %g richtige Lottozahlen.', anzahl_richtige)
fprintf('Die 1. Lottozahl ist: %g \n', zufallszahl1)
fprintf('Die 2. Lottozahl ist: %g \n', zufallszahl2)
fprintf('Die 3. Lottozahl ist: %g \n', zufallszahl3)
fprintf('Die 4. Lottozahl ist: %g \n', zufallszahl4)
fprintf('Die 5. Lottozahl ist: %g \n', zufallszahl5)
fprintf('Die 6. Lottozahl ist: %g \', zufallszahl6)


function zahl = zahl_abfragen()
    zahl = input('Bitte geben Sie eine Zahl zwischen 1 und 49 ein: ');
    while (zahl < 1) || (zahl > 49)
        zahl = input('Bitte geben Sie eine Zahl zwischen 1 und 49 ein: ');
    end
end
