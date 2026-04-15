import json
with open('data/stations_2000.geojson', 'r', encoding='utf-8') as f:
    data2000 = json.load(f)
print(type(data2000['features'][0]['properties']['prefeito_1t']))
