import json
with open('data/stations_2000.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('data/stations.geojson', 'r', encoding='utf-8') as f:
    data2002 = json.load(f)

print("2000 PREF 1T:", data['features'][0]['properties'].get('prefeito_1t'))
print("2002 PRES:", data2002['features'][0]['properties'].get('presidente'))
