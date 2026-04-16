import json
with open('data/EL2000.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)
with open('debug_feature.txt', 'w', encoding='utf-8') as out:
    out.write(json.dumps(data['features'][0]['properties'], indent=2, ensure_ascii=False))
    
    unique_muns = set()
    for feat in data['features']:
        mun = feat['properties'].get('municipio')
        if mun:
            unique_muns.add(mun)
    out.write("\n\nMunicipios:\n" + str(unique_muns))
