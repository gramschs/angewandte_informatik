% Aufgabe 8.9
% 
% Implementieren Sie eine Klasse Datum. Diese Klasse speichert Tag, Monat 
% und Jahr als Attribut.
%
% Implementieren Sie Methoden, die diese Attribute verändern können. Dabei 
% soll die Methode per Print()-Funktion warnen, wenn eine nicht zulässige 
% Zahl verwendet wird und dann nicht die Änderung durchführen.
% Implementieren Sie eine Methode get_datum_deutsch(), die das Datum als 
% String nach dem Muster TT.MM.JJJJ zurückgibt, also z.B. '07.06.2021'.
% Implementieren Sie eine Methode get_datum_britisch(), die das Datum als 
% String nach dem Muster TT/MM/JJJJ zurückgibt, also z.B. '07/06/2021'.
% Implementieren Sie eine Methode get_datum_amerikanisch(), die das Datum 
% als String nach dem Muster MM/TT/JJJJ zurückgibt, also z.B. '06/07/2021'.

classdef Datum
    properties
        tag
        monat
        jahr
    end

    methods
        function obj = Datum(tag, monat, jahr)
            obj.tag = tag;
            obj.monat = monat;
            obj.jahr = jahr;
        end

        function string = get_datum_deutsch(obj)
            string = sprintf("%g.%g.%g", obj.tag, obj.monat, obj.jahr);
        end
        function string = get_datum_britisch(obj)
            string = sprintf("%g/%g/%g", obj.tag, obj.monat, obj.jahr);
        end
        function string = get_datum_amerikanisch(obj)
            string = sprintf("%g/%g/%g", obj.monat, obj.tag, obj.jahr);
        end
    end
end


