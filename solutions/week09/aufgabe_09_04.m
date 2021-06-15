% Aufgabe 9.4
%
% Stellen Sie die Zugriffszahlen auf die Jupyter Notebooks und die MATLAB 
% Live Scripts in einem Balkendiagramm dar. Dabei gibt es ein Problem, welches?
%
% Anzahl Nutzer/innen mit Zugriff auf die Jupyter Notebooks zum Download im Sommersemester 2021
%
% | Woche | Anzahl Nutzer/innen |
% | --- | --- |
% | 2 | 17 |
% | 3 | 24 |
% | 4 | 73 |
% | 5 | 59 |
% | 6 | 55 |
% | 7 | 57 |
%
%Hier ist eine Tabelle mit den Zugriffszahlen auf das MATLAB Live Script in 
% der Vorlesung angewandte Informatik im Sommersemester 2021
%
% |Woche |Anzahl Nutzer/innen|
% | --- | --- |
% | 3 | 9  |
% | 4 | 17 |
% | 5 | 15 |
% | 6 | 10 |
% | 7 | 11 |

% Eingabe
x_j = [2,3,4,5,6,7];
y_j = [17, 24, 73, 59, 55, 57];
x_m = [3,4,5,6,7];
y_m = [9, 17, 15, 10, 11];

% Ausgabe
bar(x_j,y_j);
hold on;
bar(x_m,y_m);
hold off;

