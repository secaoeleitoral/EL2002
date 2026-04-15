const fs = require('fs');

const candidatesContent = fs.readFileSync('js/candidates.js', 'utf8');
eval(candidatesContent);

const geojson = JSON.parse(fs.readFileSync('data/stations.geojson', 'utf8'));
const currentCargo = 'presidente_1t';

const activeWinners = new Set();
geojson.features.forEach((feature) => {
    let votes = feature.properties[currentCargo];
    if (!votes) {
        const baseCargo = currentCargo.replace('_1t', '').replace('_2t', '');
        votes = feature.properties[baseCargo] || feature.properties['votos_' + baseCargo] || {};
    }
    
    if (typeof votes === 'string') {
        try { votes = JSON.parse(votes); } catch(e) { votes = {}; }
    }
    if (typeof votes !== 'object' || votes === null) votes = {};
    
    let maxVotes = -1;
    let topCode = null;
    for (const code in votes) {
        if (typeof INVALID_CODES !== 'undefined' && !INVALID_CODES.has(code)) {
            const v = Number(votes[code]) || 0;
            if (v > maxVotes) {
                maxVotes = v;
                topCode = code;
            }
        }
    }
    if (topCode && maxVotes > 0) {
        activeWinners.add(topCode);
    }
});

const cargoData = CANDIDATES[currentCargo];
let entries = Object.entries(cargoData.candidates).filter(([code]) => !INVALID_CODES.has(code));
entries = entries.filter(([code]) => activeWinners.has(code));

console.log("Entries:", entries);
console.log("Total features:", geojson.features.length);
console.log("Active winners:", Array.from(activeWinners));
