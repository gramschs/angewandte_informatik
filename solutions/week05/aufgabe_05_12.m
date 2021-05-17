% Aufgabe 5.12
%
% Schreiben Sie eine Funktion, die als Input einen Integer N entgegen nimmt 
% und dann eine Liste von N Zufallszahlen zwischen 1 und 100 ausgibt. 
% Testen Sie anschließend diese Funktion.
%
% Tipp: die Funktion randi([1 100]) generiert eine Zufallszahl zwischen 1 
% und 100. 

function aufgabe_05_12(anzahl)

    for i = 1:anzahl
        zufallszahl = randi([1 100]);
        disp(zufallszahl);
    end
    
end
