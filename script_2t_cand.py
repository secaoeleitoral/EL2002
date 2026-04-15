import json

with open('data/stations_2000.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

cidades_2t = {}
for feature in data['features']:
    mun = feature['properties'].get('municipio')
    votes_2t = feature['properties'].get('prefeito_2t', {})
    if sum(votes_2t.values()) > 0:
        if mun not in cidades_2t:
            cidades_2t[mun] = set()
        for code, v in votes_2t.items():
            if v > 0 and code not in ('95', '96'):
                cidades_2t[mun].add(code)

for mun, codes in cidades_2t.items():
    print(f"{mun}: {sorted(list(codes))}")
