"""
Gera o bloco MUNICIPIOS_1996 do candidates.js a partir do
dicionario 1996.csv (TSE, RMSP).

Uso (da raiz do projeto):
    python scripts/build_municipios_1996.py
"""

import csv
import json
import os
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')

CSV_PATH = os.path.join("data", "dicionario 1996.csv")
OUT_PATH = os.path.join("scripts", "_municipios_1996_generated.js")

# 39 municípios RMSP (nomes como aparecem no geojson - sem acento, caixa alta)
RMSP_39 = {
    "ARUJA", "BARUERI", "BIRITIBA MIRIM", "CAIEIRAS", "CAJAMAR", "CARAPICUIBA",
    "COTIA", "DIADEMA", "EMBU DAS ARTES", "EMBU GUACU", "FERRAZ DE VASCONCELOS",
    "FRANCISCO MORATO", "FRANCO DA ROCHA", "GUARAREMA", "GUARULHOS",
    "ITAPECERICA DA SERRA", "ITAPEVI", "ITAQUAQUECETUBA", "JANDIRA", "JUQUITIBA",
    "MAIRIPORA", "MAUA", "MOGI DAS CRUZES", "OSASCO", "PIRAPORA DO BOM JESUS",
    "POA", "RIBEIRAO PIRES", "RIO GRANDE DA SERRA", "SALESOPOLIS", "SANTA ISABEL",
    "SANTANA DE PARNAIBA", "SANTO ANDRE", "SAO BERNARDO DO CAMPO",
    "SAO CAETANO DO SUL", "SAO LOURENCO DA SERRA", "SAO PAULO", "SUZANO",
    "TABOAO DA SERRA", "VARGEM GRANDE PAULISTA",
}

# Alias no TSE -> nome usado no geojson
ALIAS = {
    "EMBU": "EMBU DAS ARTES",
    "MOJI DAS CRUZES": "MOGI DAS CRUZES",  # grafia antiga do TSE
}


def normalize(s):
    """Remove acentos, caixa alta, sem espaços duplicados."""
    if not s:
        return ""
    nfkd = unicodedata.normalize("NFKD", s)
    ascii_only = "".join(c for c in nfkd if not unicodedata.combining(c))
    return " ".join(ascii_only.upper().split())


def to_titlecase(name):
    """Converte 'ANTONIO SILVA' -> 'Antonio Silva', preservando hifens etc."""
    parts = name.split()
    return " ".join(p.capitalize() for p in parts)


def main():
    print(f"Lendo {CSV_PATH}...")

    with open(CSV_PATH, encoding="latin-1") as f:
        reader = csv.DictReader(f, delimiter=";")
        rows = list(reader)

    print(f"Total de linhas no CSV: {len(rows)}")

    # Agrupar por município RMSP
    muns = {}  # {"SAO PAULO": {"11": {"nome": "Maluf", "partido": "PPB"}, ...}}

    for row in rows:
        mun_raw = row.get("NM_UE", "").strip()
        mun_norm = normalize(mun_raw)
        mun_norm = ALIAS.get(mun_norm, mun_norm)

        if mun_norm not in RMSP_39:
            continue

        code = row.get("NR_CANDIDATO", "").strip()
        # NM_URNA no TSE 1996 é truncado em 30 chars — usar NM_CANDIDATO (nome completo)
        nome_full = row.get("NM_CANDIDATO", "").strip()
        nome_urna = row.get("NM_URNA_CANDIDATO", "").strip()
        # Se NM_URNA for um apelido distinto (não é prefixo do nome completo), prefere
        if nome_urna and nome_full and not nome_full.startswith(nome_urna.rstrip(".")):
            nome = nome_urna
        else:
            nome = nome_full or nome_urna
        partido = row.get("SG_PARTIDO", "").strip()

        if not code or not nome:
            continue

        if mun_norm not in muns:
            muns[mun_norm] = {}

        # Se já existe (turno diferente ou duplicata), mantém o primeiro
        if code not in muns[mun_norm]:
            muns[mun_norm][code] = {
                "nome": to_titlecase(nome),
                "partido": partido,
            }

    print(f"\nMunicípios RMSP encontrados: {len(muns)}")
    missing = sorted(RMSP_39 - set(muns.keys()))
    if missing:
        print(f"FALTANDO ({len(missing)}):")
        for m in missing:
            print(f"  - {m}")
    else:
        print("Todos os 39 municípios cobertos!")

    # Contagem por município
    print(f"\nCandidatos por município:")
    for m in sorted(muns.keys()):
        print(f"  {m}: {len(muns[m])} candidatos")

    # Gerar JS
    # Ordenar por chave
    muns_sorted = dict(sorted(muns.items()))

    print(f"\nGerando {OUT_PATH}...")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("// Gerado por scripts/build_municipios_1996.py\n")
        f.write("const MUNICIPIOS_1996 = ")
        f.write(json.dumps(muns_sorted, ensure_ascii=False, indent=4))
        f.write(";\n")

    print(f"[OK] {sum(len(v) for v in muns.values())} candidatos totais")


if __name__ == "__main__":
    main()
