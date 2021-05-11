% Aufgabe 4.10
%
% Schreiben Sie ein Programm, welches die folgende Ausgabe bis zu einer vom 
% Benutzer gewählten Zahl fortsetzt:
%
% 1 *
% 2 **
% 3 ***
% 4 ****
% 5 *****
% 6 ******
% 7 *******
%
% Zusatz: Passen Sie das Programm so an, dass es einen Weihnachtsbaum aus 
% Sternchen zeichnet, dessen Höhe vom Benutzer gewählt werden kann.

% Eingabe
anzahl_zeilen = input('Wie viele Zeilen mit Sternen sollen gezeichnet werden? ');
weihnachtsbaum_zeichnen = input("Soll ein Weihnachtsbaum gezeichnet werden ('j'/'n')? ");

% Ausgabe (Lösung mit if, while und fprintf; für eine Lösung mit repelem
% siehe unten den auskommentierten Code
zeile = 1;
while zeile <= anzahl_zeilen
    if weihnachtsbaum_zeichnen == 'j'
        i = 1;
        while i <= anzahl_zeilen - zeile
            fprintf(' ');
            i = i + 1;
        end
        i = 1;
        while i <= zeile
            fprintf('*');
            i = i + 1;
        end
        fprintf('%d', zeile);
        i = 1;
        while i <= zeile
            fprintf('*');
            i = i + 1;
        end
        fprintf('\n')
    else
        fprintf('%d', zeile)
        i = 1;
        while i <= zeile
            fprintf('*');
            i = i + 1;
        end
        fprintf('\n')
    end
    zeile = zeile + 1;
end

% Stamm zeichnen
if weihnachtsbaum_zeichnen == 'j'
    i = 1;
    while i <= anzahl_zeilen - 1
        fprintf(' ')
        i = i + 1;
    end
    fprintf('*****\n')
    i = 1;
    while i <= anzahl_zeilen - 1
        fprintf(' ')
        i = i + 1;
    end
    fprintf('*****\n')
end

% Ausgabe Alternative mit repelem
%zeile = 1;
%while zeile <= anzahl_zeilen
%    if weihnachtsbaum_zeichnen == 'j'
%        fprintf('%s %s %g %s \n', repelem(' ',anzahl_zeilen - zeile), repelem('*',zeile), zeile, repelem('*', zeile));
%    else
%        fprintf('%g %s \n', zeile, repelem('*', zeile));
%    end
%    zeile = zeile + 1;
%end

%if weihnachtsbaum_zeichnen == 'j'
%    fprintf('%s %s \n', repelem(' ', anzahl_zeilen - 1), '*****');
%    fprintf('%s %s \n', repelem(' ', anzahl_zeilen - 1), '*****');
%end