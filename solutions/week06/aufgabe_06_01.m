% Aufgabe 6.1

% Eingabe
anzahl_versuche = input('Wie oft sollen die Würfelversuche durchgeführt werden? ');

% Verarbeitung
summe_versuche = 0; 
for i = 1:anzahl_versuche
    summe_versuche = summe_versuche + wuerfeln_bis_sechs();
end
mittelwert = summe_versuche / anzahl_versuche;
    
% Ausgabe
fprintf('Im Durchschnitt wurde nach %.1f maligem Würfeln eine 6 gewürfelt.', mittelwert);

%% Funktion
function anzahl_wuerfe = wuerfeln_bis_sechs()
    anzahl_wuerfe = 0;
    wurf = randi([1 6]);
    while wurf ~= 6
        anzahl_wuerfe = anzahl_wuerfe + 1;
        wurf = randi([1 6]);
        
    end
end