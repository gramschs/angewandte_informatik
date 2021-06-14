classdef Studierende

    properties
        vorname
        nachname
        matrikelnummer
    end

    methods
        function obj = Studierende(vorname, nachname, matrikelnummer)
            obj.vorname = vorname;
            obj.nachname = nachname;
            obj.matrikelnummer = matrikelnummer;
        end

    end
end