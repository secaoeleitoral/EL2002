import json

def get_count(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return len(data.get('features', []))
    except Exception as e:
        return f"Error: {e}"

count_2000 = get_count('data/EL2000_web.geojson')
count_2002 = get_count('data/stations.geojson')

print(f"2000: {count_2000}")
print(f"2002: {count_2002}")
