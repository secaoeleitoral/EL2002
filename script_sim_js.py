import json

with open('data/stations.geojson', 'r', encoding='utf-8') as f:
    data2002 = json.load(f)

activeWinners = set()
invalid_codes = {'95', '96', '99'}

for feature in data2002['features']:
    votes = feature['properties'].get('presidente_1t', {})
    max_votes = -1
    top_code = None
    for code, v_str in votes.items():
        if code not in invalid_codes:
            v_num = int(v_str) if v_str else 0
            if v_num > max_votes:
                max_votes = v_num
                top_code = code
    if top_code and max_votes > 0:
        activeWinners.add(top_code)

print("Active winners for presidente_1t:", activeWinners)
