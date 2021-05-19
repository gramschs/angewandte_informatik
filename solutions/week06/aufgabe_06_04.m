% Aufgabe 6.4

computer_zahl = randi([1 100]);

zahl = input('Raten Sie: ');
anzahl_versuche = 1;
while zahl ~= computer_zahl
    if zahl < computer_zahl
        disp('Meine Zahl ist größer. ');
        zahl = input('Raten Sie: ');
    else
        disp('Meine Zahl ist kleiner. ');
        zahl = input('Raten Sie: ');
    end
    anzahl_versuche = anzahl_versuche + 1;
end
        
fprintf('Gratulation, die Zahl %g ist richtig. Sie haben %g Versuche gebraucht.', zahl, anzahl_versuche)