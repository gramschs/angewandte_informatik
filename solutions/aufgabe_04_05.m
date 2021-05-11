% Aufgabe 4.5
% Schreiben Sie das Programm für einen Ticket-Automaten. Der Benutzer wird 
% nach dem Alter gefragt und ob ein Schülerausweis vorliegt. Das Programm 
% gibt dann aus, welches Ticket gekauft werden muss.
% Alter                          | Ticket
% 0 - 5                          | keine 
% 6 - 14                         | Kinder-Ticket
% 15 - 21 und Schülerausweis     | Kinder-Ticket
% 15 - 59                        | Erwachsenen-Ticket
% ab 60                          | Senioren-Ticket

% Eingabe
alter = input('Wie alt sind Sie?');
hat_schuelerausweis = input("Haben Sie einen Schülerausweis ('j'/'n')");

% Verarbeitung
if alter <= 5
    disp('Sie können eine Kinderfahrkarte kaufen.')
elseif (6 <= alter) && (alter <= 14)
    disp('Sie brauchen ein Kinder-Ticket.')
elseif (15 <= alter) && (alter <= 21) && (hat_schuelerausweis == 'j')
    disp('Sie brauchen ein Kinder-Ticket.')
elseif (15 <= alter) && (alter <= 59)
    disp('Sie brauchen ein Erwachsenen-Ticket.')
else
    disp('Sie brauchen ein Senioren-Ticket.')
end

