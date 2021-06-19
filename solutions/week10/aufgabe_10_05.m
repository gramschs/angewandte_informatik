% Aufgabe 6.2

% Eingabe 
anzahl_aufgaben = bestimme_anzahl_aufgaben();

% Verarbeitung
anzahl_richtige_aufgaben = stelle_einmaleins_aufgaben(anzahl_aufgaben);
prozent = anzahl_richtige_aufgaben / anzahl_aufgaben * 100;

% Ausgabe
fprintf('Sie haben %g von %g Aufgaben richtig gelöst, das sind %f Prozent.', anzahl_richtige_aufgaben, anzahl_aufgaben, prozent);


%% Funktion
function anzahl_aufgaben = bestimme_anzahl_aufgaben()
  anzahl_aufgaben = input('Wie viele Aufgaben sollen gestellt werden? ');  
  while anzahl_aufgaben <= 0
       anzahl_aufgaben = input('Sie müssen eine positive ganze Zahl wählen. Wie viele Aufgaben sollen gestellt werden? ');  
  end
end

function anzahl_richtigen_antworten = stelle_einmaleins_aufgaben(anzahl_aufgaben)
    
    anzahl_richtigen_antworten = 0;
    
    for i = 1:anzahl_aufgaben
        % Eingabe
        a = randi([1 10]);
        b = randi([1 10]);
        fprintf('Was ist %g x %g ',a,b)
        ergebnis = input('= ');
        
        % Verarbeitung
        if ergebnis == a*b
            anzahl_richtigen_antworten = anzahl_richtigen_antworten + 1;
            disp('Richtig!')
        else
            fprintf('Leider falsch, das richtige Ergebnis wäre %g', a*b);
        end
    end
end
    