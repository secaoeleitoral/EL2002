import json
with open('data/EL2000_web.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

for feat in data['features']:
    if feat['properties'].get('municipio') == 'GUARULHOS':
        print(json.dumps(feat['properties'], indent=2, ensure_ascii=False))
        break
