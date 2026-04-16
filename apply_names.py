import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Insert getCandidateDisplayName before renderDetail
helper_func = '''    function getCandidateDisplayName(info, municipioName) {
        if (!info) return 'Candidato';
        if (state.currentCargo.startsWith('prefeito') && municipioName && municipioName.toUpperCase() !== 'SAO PAULO') {
            return info.partido ? Partido  : 'Candidato';
        }
        return info.nome;
    }

    function renderDetail(feature) {'''

text = text.replace('    function renderDetail(feature) {', helper_func)

# 2. In renderMetrics (line 1178 roughly)
text = text.replace(
    "value: summary.winner ? ${summary.winner.info.nome} () : 'Sem votos'",
    "value: summary.winner ? ${getCandidateDisplayName(summary.winner.info, props.municipio)} () : 'Sem votos'"
)

# 3. In renderCandidateCards
text = text.replace(
    'aria-label="Personalizar cor de "',
    'aria-label="Personalizar cor de "'
)

text = text.replace(
    '<h4></h4>',
    '<h4></h4>'
)

text = text.replace(
    'openColorPicker(familyKey, entry.info.nome, colorTrigger);',
    'openColorPicker(familyKey, getCandidateDisplayName(entry.info, feature.properties.municipio), colorTrigger);'
)

# 4. In buildTooltipHtml
text = text.replace(
    "const subtitle = winner",
    "const displayName = winner ? getCandidateDisplayName(winner.info, feature.properties.municipio) : null;\n        const subtitle = winner"
)
text = text.replace(
    " ()",
    " ()"
)

text = text.replace(
    ": ",
    ": "
)

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated app.js successfully")
