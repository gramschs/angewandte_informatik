% Aufgabe 5.6
%
% In der Mathematik gibt es die Schreibweise 
% 𝑛! : = 𝑛 ⋅ (𝑛−1) ⋅ (𝑛−2) … 3 ⋅ 2 ⋅ 1.
% So wird zum Beispiel 5! durch  5⋅4⋅3⋅2⋅1 = 120  berechnet. Dies wird in 
% der Mathematik als Fakultät von 5 bezeichnet.
%
%Schreiben Sie ein Programm, welches n! für ein vom Benutzer vorgegebenes n 
% berechnet. Benutzen Sie dafür eine for-Schleife.

% Eingabe
n = input('Bitte geben Sie n ein: ');

% Verarbeitung
ergebnis = 1;
for i = 1:n 
    ergebnis = ergebnis * i;
end

% Ausgabe
fprintf('Die Fakultät von %g lautet %g ! = %g.', n, n, ergebnis);
