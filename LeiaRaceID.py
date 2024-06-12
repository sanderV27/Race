import csv

def LeiaRaceID(circuit_id):
    race_ids = []
    with open(".venv/share/races.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header
        for row in reader:
            _, _, _, current_circuit_id, _, _, _, _, _, _, _, _, _, _, _, _, _, _ = row
            if str(circuit_id) == current_circuit_id:
                race_id = row[0]
                race_ids.append(race_id)
    return race_ids

# Example circuit ID
circuit_id = 1  # This should correspond to an actual circuitId in your CSV
race_ids = LeiaRaceID(circuit_id)
print(race_ids)
