% Aufgabe 6.3

f(x) = 7*x^2;
ordnung = input('Wie oft soll die Funktion abgeleitet werden?');
if ordnung == 1
    diff(f(x), x)
elseif ordnung == 2
    diff(f(x), x, x)
elseif ordnung == 3
    diff(f(x), x, x, x)
else
    disp('Höher als 3 geht nicht...')
end