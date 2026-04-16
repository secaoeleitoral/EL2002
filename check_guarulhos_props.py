import json

with open('data/EL2000_web.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)

# check a random feat in guarulhos
for feat in data['features']:
    if feat['properties'].get('municipio') == 'GUARULHOS':
        props = feat['properties']
        keys = list(props.keys())
        print(f"Prop keys for Guarulhos: {keys}")
        print(f"Prefeito_1t value: {props.get('prefeito_1t')}")
        break
