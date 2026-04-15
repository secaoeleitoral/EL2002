const fs = require('fs');

const stationsData = JSON.parse(fs.readFileSync('data/stations.geojson', 'utf8'));
const geojson = stationsData;

const currentCargo = 'presidente_1t';
const currentLocalId = null;
const currentBairro = null;
const currentMunicipio = '';

const INVALID_CODES = new Set(['95', '96', '99']);

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

console.log('2002 activeWinners:', Array.from(activeWinners));
