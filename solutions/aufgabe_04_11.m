% Aufgabe 4.11
%
% Unter https://www.frankfurt-university.de/de/hochschule/fachbereich-2-informatik-und-ingenieurwissenschaften/corona-faqs-fuer-fb-2/
% finden Sie die Erklärungen, bei welchen Krankheitssymptoman man an die 
% Hochschule kommen darf.
%
% Schreiben Sie ein Programm, dass dem Benutzer mehrere Fragen nach 
% Symptomen stellt, z.B. "Haben Husten?" und auf die Antworten reagiert. 
% Wenn z.B. die Frage nach dem Husten mit "Ja" beantwortet wird, fragt das 
% Programm nach, ob der Husten trocken ist oder nur gelegenlich auftritt. 
% Am Ende soll das Programm entscheiden, ob der Benutzer an die Hochschule 
% kommen darf oder nicht.

% Vorbereitungen
hat_fieber = false;
ist_fieber_hoch = false;
hat_husten = false;
ist_husten_trocken = false;
hat_stoerung_sinne = false;
hat_schnupfen = false;
hat_keine_weiteren_symptome = false;

% Eingabe
antwort = input("Haben Sie Fieber ('j'/'n'?");
if antwort == 'j'
    antwort = input("Ist das Fieber höher als 38,0 °C ('j'/'n')? ");
    if antwort == 'j'
        ist_fieber_hoch = True;
    end
end

antwort = input("Haben Sie Husten ('j'/'n')? ");
if antwort == 'j'
    hat_husten = true;
    antwort = input("Ist der Husten trocken ('j'/'n')? ");
    if antwort == 'j'
        ist_husten_trocken = true;
    end
end

antwort = input("Ist Ihr Geruchssinn oder Ihr Geschmackssinn gestört ('j'/'n')?");
if antwort == 'j'
    hat_stoerung_sinne = true;
end

antwort = input("Haben Sie weitere Krankheitssymptome ('j'/'n')? ");
if antwort ~= 'j'
    hat_keine_weiteren_symptome = true;
end

% Verarbeitung
darf_kommen = (~ist_fieber_hoch) && (~ist_husten_trocken) && (~hat_stoerung_sinne) && hat_keine_weiteren_symptome;

if darf_kommen == true
    disp('Sie dürfen zur Hochschule kommen.');
else
    disp('Sie fürfen NICHT zur Hochschule kommen.');
end