# -*- coding: utf-8 -*-
import csv
import json

municipios = {}
with open('rmsp_filtrado_2000.csv', 'r', encoding='utf-8', errors='replace') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        if len(row) < 10: continue
        if row[0] == 'UF': continue 
        mun_nome = row[2]
        num_cand = row[5]
        nome_urna = row[7].title()
        partido = row[9]
        if mun_nome not in municipios:
            municipios[mun_nome] = {}
        municipios[mun_nome][num_cand] = {'nome': nome_urna, 'partido': partido}

with open('mapping.json', 'w', encoding='utf-8') as f:
    json.dump(municipios, f, ensure_ascii=False, indent=4)
