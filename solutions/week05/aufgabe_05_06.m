% Aufgabe 5.6
%
% Schreiben Sie ein Programm, das eine Einmaleins-Tabelle bis zu 10x10 aus-
% gibt. Also
%
% 1 x 1 = 1
% 2 x 1 = 2
% 3 x 1 = 3
%
% usw.

for i = 1: 10
    for j = 1:10
        fprintf('%g x %g = %g \n', i, j, i*j);
    end
    fprintf('\n');
end
    