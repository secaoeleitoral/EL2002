import json
with open('data/EL2000.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)
print("Number of features:", len(data.get('features', [])))
if len(data.get('features', [])) > 0:
    print("Properties of first feature:")
    print(json.dumps(data['features'][0]['properties'], indent=2, ensure_ascii=False))
