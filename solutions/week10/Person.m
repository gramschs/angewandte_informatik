% Aufgabe 10.2 korrigierte Klasse

classdef Person
    properties
        first
        last
    end
    methods
        function obj = Person(vorname, nachname)
            obj.first = vorname;    
            obj.last = nachname;         
        end

        function vorstellen(obj) 
            fprintf("Guten Tag. Mein Name ist " + obj.first + " " + obj.last) 
        end
    end
end


