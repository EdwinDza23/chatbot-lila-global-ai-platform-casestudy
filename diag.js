const fs = require('fs');
const filepath = 'd:\\Casestudy\\Lila Global\\V2\\index.html';
const content = fs.readFileSync(filepath, 'utf8');

const idx1 = content.indexOf('FLIP CHALLENGES');
const idx2 = content.indexOf('FLIP CARDS');
const idx3 = content.indexOf('Tap each card to flip');
const idx4 = content.indexOf('cf-inner');
const idx5 = content.indexOf('cf-hint');

console.log('FLIP CHALLENGES at:', idx1);
if (idx1 >= 0) console.log('  chars:', JSON.stringify(content.slice(idx1, idx1 + 80)));

console.log('FLIP CARDS JS at:', idx2);
if (idx2 >= 0) console.log('  chars:', JSON.stringify(content.slice(idx2, idx2 + 100)));

console.log('Tap each card at:', idx3);
if (idx3 >= 0) console.log('  chars:', JSON.stringify(content.slice(idx3 - 5, idx3 + 70)));

console.log('cf-inner at:', idx4);
if (idx4 >= 0) console.log('  chars:', JSON.stringify(content.slice(idx4 - 15, idx4 + 50)));

console.log('cf-hint at:', idx5);
if (idx5 >= 0) console.log('  chars:', JSON.stringify(content.slice(idx5 - 5, idx5 + 50)));

// Show the newline chars around FLIP CHALLENGES
if (idx1 >= 0) {
  const region = content.slice(Math.max(0, idx1 - 20), idx1 + 200);
  const codes = [...region].map(c => c.charCodeAt(0));
  console.log('\nChar codes around FLIP CHALLENGES:', codes.slice(0, 40));
}
