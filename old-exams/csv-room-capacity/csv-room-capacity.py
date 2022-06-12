import csv

result = {}

with open('exam-schedule.csv') as f:
    data = csv.DictReader(f)

    for row in data:
        datum = row['Datum']
        dagdeel = row['Dagdeel']
        lokaal = row['Lokaal']
    
        locaties = result.setdefault(lokaal, {})
        key = (datum, dagdeel)
        locaties[key] = locaties.get((datum, dagdeel), 0) + 1
    
locaties = sorted(result.keys())

with open('output.txt', 'w') as out:
    for locatie in locaties:
        maximum = max(result[locatie].values())
        out.write(f'{locatie} {maximum}\n')