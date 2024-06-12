import csv

from LeiaRaceID import LeiaRaceID


def Leia_voit(race_ids):
    total_races = 0
    wins_from_pole = 0
    with open("results.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  #Jätab päise vahele, kui see on olemas.
        for row in reader:
            if row[1] in race_ids:  # Kontrolli, kas raceId on analüüsitavate raceId-de nimekirjas
                total_races += 1
                if row[5] == '1' and row[6] == "1":  # Eeldades, et 'grid' on indeksis 5 ja 'lõppposition' 6
                    wins_from_pole += 1
    return len(race_ids), wins_from_pole

race_ids = LeiaRaceID("22") #Lisameetod mis leib kõik võidusõitude id´d vastavalt ringraja id'le
total_races, pole_wins = Leia_voit(race_ids)
print( "võidu % startides P1", round(pole_wins / total_races * 100, 1) )

