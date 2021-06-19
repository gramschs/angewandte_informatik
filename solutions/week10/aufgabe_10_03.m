% Aufgabe 10.3
%
% Ein Zeitreisender kommt auf Sie zu. Fragen Sie ihn nach dem Jahr, aus 
% dem er kommt und begrüßen Sie ihn. Falls er aus einem Jahr vor 1900 kommt 
% mit "Sie kommen ja aus der Vergangenheit!", zwischen 1900 und 2021 mit 
% "Sie stammen also aus unserer Zeit!" und ansonsten mit "Können Sie mir 
% die Lottozahlen von nächster Woche verraten?". Schreiben Sie als erstes 
% Ihr eigenes Programm in der nächsten Code-Zelle:

jahr = input("Ein Zeitreisender??? Aus welchem Jahr kommen Sie denn? ");
if jahr <= 1900   
    disp ('Sie kommen ja aus der Vergangenheit!') 
elseif jahr > 1900 && jahr < 2020
    disp ("Sie stammen also aus unserer Zeit!") 
else
    disp ("Können Sie mir die Lottozahlen von nächster Woche verraten?")
end