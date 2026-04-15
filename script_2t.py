import json
with open('data/stations_2000.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

cities_with_2t = set()
for feature in data['features']:
    mun = feature['properties'].get('municipio')
    votes_2t = feature['properties'].get('prefeito_2t', {})
    # check if any total votes > 0
    if sum(votes_2t.values()) > 0:
        cities_with_2t.add(mun)

print(sorted(list(cities_with_2t)))
