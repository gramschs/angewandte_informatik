% Aufgabe 2.8 Kostenkalkulation Urlaubsreise
%
% Schreiben Sie ein Programm, das die Kosten für eine Urlaubsreise für eine 
% Reisegruppe mit einem Bus berechnet. Vom Benutzer werden folgende Angaben 
% erfragt: 
% Anzahl der Personen, 
% Hotelkosten pro Person, 
% Gesamtkosten für den Reisebus, 
% Gesamtkosten für touristische Events am Zielort.
%
% Ausgegeben werden die Gesamtkosten der Fahrt und der Betrag, den jeder 
% Teilnehmer zahlen muss. Möglicher Programmlauf:
%
% Kostenplan für eine Reise 
% ---------------------------
% Kosten für den Reisebus: 1000
% Hotelkosten pro Person: 300
% Gesamtkosten für touristische Events: 500 
% Anzahl der Teilnehmer: 30
%
% Die Gesamtkosten betragen 10500 EUR. Die Kosten pro Person sind 350 EUR.
%
% Hinweise: Machen Sie sich erstmal einen Plan, welche Eingaben abgefragt 
% werden müssen, wie diese verarbeitet werden sollen und was das Programm 
% am Ende ausgeben soll. Danach implementieren Sie Ihren Algorithmus.  
% Achten Sie auf guten Programmierstil. Verwenden Sie »sprechende« 
% Variablennamen. Setzen Sie die Funktion input() für die Eingabe der 
% Zahlenwerte ein und denken Sie an die Umwandlung in einen Integer oder 
% einen Float, falls Sie Python verwenden.

disp("Kostenplan für eine Reise")
disp("-------------------------")

% Eingabe
bus_kosten = input("Kosten für den Reisebus: ");
hotel_kosten = input("Hotelkosten pro Person: ");
event_kosten = input("Gesamtkosten für touristische Events: ");
anzahl_personen = input("Anzahl der Teilnehmer: ");

% Verarbeitung
gesamtkosten = bus_kosten  + event_kosten + anzahl_personen * hotel_kosten;
kosten_pro_person = gesamtkosten / anzahl_personen;

% Ausgabe
disp("Die Gesamtkosten betragen ")
disp(gesamtkosten)
disp("Die Kosten pro Person sind ")
disp(kosten_pro_person)