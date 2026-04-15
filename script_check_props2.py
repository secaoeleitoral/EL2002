import json

with open('data/stations.geojson', 'r', encoding='utf-8') as f:
    data2002 = json.load(f)

print(list(data2002['features'][0]['properties'].keys()))
