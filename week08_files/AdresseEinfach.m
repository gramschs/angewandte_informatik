classdef AdresseEinfach
    properties
        strasse
        hausnummer
        postleitzahl
        stadt
    end
    methods
        function obj = AdresseEinfach(strasse, hausnummer, postleitzahl, stadt)
            obj.strasse = strasse;
            obj.hausnummer = hausnummer;
            obj.postleitzahl = postleitzahl;
            obj.stadt = stadt;
        end
        function print(obj)
            fprintf('%s %g, %g %s \n', obj.strasse, obj.hausnummer, obj.postleitzahl, obj.stadt)
        end
    end
end
 