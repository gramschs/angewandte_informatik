% Aufgabe 9.3
% 
% Stellen Sie die Funktionen
% f1(x) = sin(x)
% f2(x) = sin(2x)
% f3(x) = sin(3x)
%
% als xy-Diagramm im Intervall [-2\pi,2\pi] dar und beschriften Sie die 
% Kurven mit einer geeigneten Legende.

% Eingabe
x = linspace(-2*pi, 2*pi, 1000);
y1 = sin(x);
y2 = sin(2*x);
y3 = sin(3*x);

% Ausgabe
plot(x, y1);
hold on;
plot(x, y2);
plot(x, y3);
legend('f1', 'f2', 'f3');

