import json
with open('data/stations_2000.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

for feat in data['features']:
    if feat['properties'].get('municipio') == 'DIADEMA':
        print(feat['properties'].get('prefeito_1t'))
        break
