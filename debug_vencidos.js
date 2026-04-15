const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const code = fs.readFileSync('js/app.js', 'utf8');
const candidatesCode = fs.readFileSync('js/candidates.js', 'utf8');

const html = 
<!DOCTYPE html>
<html>
<body>
    <select id="select-cargo"><option value="presidente" selected>Presidente</option></select>
    <select id="select-turno"><option value="_1t" selected>1o Turno</option></select>
    <select id="select-vencidos-candidate"></select>
</body>
</html>
;
const dom = new JSDOM(html);
const window = dom.window;
const document = window.document;

// Execute candidates
eval(candidatesCode);

// Extract just the parts we need from app.js to test populateVencidosCandidates
const Cidades2T = ['DIADEMA', 'GUARULHOS', 'MAUA', 'MOGI DAS CRUZES', 'SAO PAULO']; 
let state = {
    currentYear: '2002',
    currentCargo: 'presidente_1t',
    currentMunicipio: '',
    currentBairro: null,
    currentLocalId: null,
    vencidosCandidateCode: null,
    geojson: JSON.parse(fs.readFileSync('data/stations.geojson', 'utf8'))
};
const domNodes = {
    selectVencidosCandidate: document.getElementById('select-vencidos-candidate')
};

function getFeatureId(f) { return f.properties.id; } // mock

" + code.match(/function populateVencidosCandidates\(\) \{[\s\S]*?\n    \}/)[0] + "

populateVencidosCandidates();
console.log('Result Options:', Array.from(domNodes.selectVencidosCandidate.options).map(o => o.value + ': ' + o.textContent));
