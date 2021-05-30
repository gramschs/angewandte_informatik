% Aufgabe 7.7
%
% Schreiben Sie das Lotto-Programm (Aufgabe 5.14) neu. 
% 1. Schreiben Sie eine Funktion, die den Benutzer sechs Zahlen zwischen 1 
% und 49 wählen lässt und eine Liste der gewählten Zahlen zurückgibt. Falls 
% der Benutzer eine ungültige Zahl eingibt, soll die Funktion dem Benutzer 
% mitteilen, warum die Zahl ungültig ist und solange nach einer gültigen 
% Zahl weiterfragen, bis die Engabe gültig ist. Wenn die Zahl schon in der 
% Liste ist, soll die Funktion dem Benutzer mitteilen, welche Zahlen schon 
% gewählt wurden und solange weiterfragen, bis eine gültige neue Zahl 
% eingegeben wurde.
%
% 2. Schreiben Sie eine Funktion, in der sechs Lottozahlen zufällig gezogen 
% werden. Die Lottozahlen werden in einer Liste gespeichert, die am Ende 
% zurückgegeben wird. Sobald die zweite, dritte Zufallszahl usw. in die 
% Liste gespeichert werden soll, wird erst überprüft, ob sie in der Liste 
% schon vorhanden ist, damit keine Zahl doppelt vorkommt.
%
% 3. Danach schreiben Sie eine Funktion, die zwei Listen mit Zahlen 
% vergleicht und berechnet, wie viele Zahlen davon übereinstimmen. Die 
% Rückgabe ist die Anzahl der übereinstimmenden Zahel (d.h. die Anzahl der 
% richtigen Lottozahlen). 
%
% Zuletzt schreiben Sie ein Programm, das die drei Funktionen verwendet. 
% Zuerst die Abfrage nach den Benutzer-Zahlen, dann das Ziehen der 
% Zufallszahlen und zuletzt eine Ausgabe, wie viele Zahlen richtig waren.
% Tipp1: Die Funktion ismember(x,A) überprüft, ob das Element x in dem Array A 
% enthalten ist. 
% Tipp2: Ein eindimensionales Array gefüllt mit Nullen wird durch die Funktion 
% A = zeros(6,1) erzeugt. Das muss man machen, bevor man in einer For-Schleife das 
% Array befüllt.

% Eingabe
benutzerzahlen = waehle_zahlen();


% Verarbeitung
lottozahlen = ziehe_lottozahlen();
anzahl_richtige = berechne_anzahl_richtige(benutzerzahlen, lottozahlen);

% Ausgabe
disp('Sie haben die folgenden Zahlen gewählt: ');
disp(benutzerzahlen);
disp('Der Computer hat die folgenden Lottozahlen gezogen: ');
disp(lottozahlen);
fprintf('Das ist/sind %g richtige Zahl(en).', anzahl_richtige);

function zahlenarray = waehle_zahlen()
    zahlenarray = zeros(6,1);
    for i = 1:6
        zahl = input('Bitte wählen Sie eine Lottozahl: ');
        while (zahl < 1) | (49 < zahl) | ismember(zahl, zahlenarray) == true
            if zahl < 1
                zahl = input('Die Zahl muss zwischen 1 und 49 liegen, bitte versuchen Sie es erneut: ');
            elseif zahl > 49
                zahl = input('Die Zahl muss zwischen 1 und 49 liegen, bitte versuchen Sie es erneut: ');
            else
                disp('Diese Zahlen haben Sie schon gewählt: ');
                disp(zahlenarray);
                zahl = input('Bitte wählen Sie eine andere Zahl: ');
            end
        end

        zahlenarray(i,1) = zahl;
    end
end


function lottozahlen = ziehe_lottozahlen()
    lottozahlen = zeros(6,1);
    for i  = 1:6
        zahl = randi(49);
        while ismember(zahl, lottozahlen) == true
            zahl = randi(49);
        end
        lottozahlen(i,1) = zahl;
    end
end


function anzahl_richtige = berechne_anzahl_richtige(benutzerzahlen, lottozahlen)
    anzahl_richtige = 0;
    for i = 1:6
        if ismember(benutzerzahlen(i), lottozahlen) == true
            anzahl_richtige = anzahl_richtige + 1;
        end
    end
end