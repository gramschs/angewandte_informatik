classdef AdresseKomplex
    properties
        strasse
        hausnummer
        postleitzahl
        stadt
    end

    methods
        function obj = AdresseKomplex(strasse,hausnummer, postleitzahl, stadt)
            obj.strasse = strasse;
            obj.hausnummer = hausnummer;
            obj.postleitzahl = postleitzahl;
            obj.stadt = stadt;
        end

        function print(obj, einzeilig)
            if einzeilig == true
               fprintf('%s %g, %g %s \n', obj.strasse, obj.hausnummer, obj.postleitzahl, obj.stadt); 
            else
               fprintf('Straße: %s \n', obj.strasse)
               fprintf('Hausnummer: %g \n', obj.hausnummer)
               fprintf('Postleitzahl: %g \n', obj.postleitzahl)
               fprintf('Stadt: %s \n', obj.stadt)
            end
        end
        
        function stadt_string = get_stadt(obj, grossschreibung)
            if grossschreibung == true
                stadt_string = upper(obj.stadt);
            else
                stadt_string = obj.stadt;
            end
        end
    end
end