import json
import os

with open('data/EL2000.geojson', 'r', encoding='utf-8', errors='replace') as f:
    raw_geojson = json.load(f)

PREFEITO_2000 = {
    "11": {}, "12": {}, "13": {}, "14": {}, "15": {}, "16": {}, "19": {}, "20": {}, "22": {}, 
    "23": {}, "25": {}, "26": {}, "27": {}, "28": {}, "29": {}, "30": {}, "36": {}, "40": {}, 
    "41": {}, "43": {}, "44": {}, "45": {}, "56": {}, "65": {}, "70": {}, "95": {}, "96": {}
}

CARGO_CONFIG = {
    "prefeito_1t": {"prefix": "PF00_", "turno": "1", "candidates": PREFEITO_2000},
    "prefeito_2t": {"prefix": "PF00_", "turno": "2", "candidates": PREFEITO_2000}
}

def extract_votes(record, prefix, turno, candidates):
    votes = {}
    for field_name, value in record.items():
        if not field_name.startswith(prefix) or value is None:
            continue
            
        suffix = field_name[len(prefix):]
        if turno is not None:
            if suffix[0] != turno: continue
            candidate_code = suffix[1:]
        else:
            candidate_code = suffix

        if candidate_code in candidates:
            # Save as string because Javascript frontend JSON.parse fails on single-quote representations, 
            # but wait, since we dump to JSON dict directly, it will serialize to double-quoted keys automatically.
            votes[candidate_code] = int(value)
            
    return votes

features = []
for feature in raw_geojson['features']:
    record = feature['properties']
    if 'geometry' not in feature or feature['geometry'] is None:
         continue
    lon, lat = feature['geometry']['coordinates'][:2]

    props = {
        "id": record.get("ID", record.get("COD_LV", record.get("id"))),
        "nome": record.get("NOME_LV"),
        "endereco": record.get("END_LV"),
        "tipo": record.get("TIPO_LV"),
        "municipio": record.get("MUN_NOME"),
        "distrito": record.get("DIS_NOME", record.get("TEC2_NOM")),
        "zona": record.get("ZE_NUM"),
        "zona_nome": record.get("ZE_NOME")
    }

    for cargo_key, cfg in CARGO_CONFIG.items():
        props[cargo_key] = extract_votes(
            record, cfg["prefix"], cfg["turno"], cfg["candidates"]
        )

    features.append({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [round(lon, 6), round(lat, 6)]
        },
        "properties": props
    })

geojson = {"type": "FeatureCollection", "features": features}

out_path = os.path.join("data", "EL2000_web.geojson")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False)

print("Processed successfully!")
