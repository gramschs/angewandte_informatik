siege_computer = 0;
wahl_computer = 'Stein';
wahl_benutzer = 'Papier';
siege_benutzer = 0;
if strcmp(wahl_computer, 'Stein')
    if strcmp(wahl_benutzer, 'Stein')
        disp('Unentschieden, ich hatte ebenfalls Stein.');
    elseif strcmp(wahl_benutzer, 'Schere')
        disp('Punkt für mich, Stein schleift Schere.');
        siege_computer = siege_computer + 1;
    else % wahl_benutzer == 'Papier'
        disp('Punkt für Sie, Papier umwickelt Stein.');
        siege_benutzer = siege_benutzer + 1;
    end
end