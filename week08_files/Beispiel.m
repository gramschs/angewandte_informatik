classdef Beispiel
    properties
        vorname
        nachname
    end
    methods
        function obj = Beispiel(vorname, nachname)
            obj.vorname = vorname;
            obj.nachname = nachname;
        end
        function schreibe_vorname_nachname(obj)
            fprintf('%s %s', obj.vorname, obj.nachname)
        end
        function schreibe_nachname_vorname(obj)
            fprintf('%s, %s', obj.nachname, obj.vorname)
        end
    end
end
 