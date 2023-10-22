const GATHER = require('gathertown.js'); // add gather package
const access = require('./config.json'); // load your apikey
const gather = GATHER(access.key); // access keys

// some variables
const spaceId = 'lobby';
const mapId = 'ZenkoAI Hackathon';

function map() {
  gather
    .getMap({ spaceId, mapId })
    .then((data) => console.log(data))
    .catch((err) => console.log(err));
}

map();