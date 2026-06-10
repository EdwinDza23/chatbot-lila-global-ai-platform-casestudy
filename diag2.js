const fs = require('fs');
const filepath = 'd:\\Casestudy\\Lila Global\\V2\\index.html';
const content = fs.readFileSync(filepath, 'utf8');

// Check line endings
const crlfCount = (content.match(/\r\n/g) || []).length;
const lfCount = (content.match(/(?<!\r)\n/g) || []).length;
console.log('CRLF (\\r\\n):', crlfCount, '| LF-only (\\n):', lfCount);

// Find challenge card section
const idx = content.indexOf('chal-grid');
console.log('\nchal-grid at:', idx);
if (idx >= 0) {
  console.log('Context (200 chars):', JSON.stringify(content.slice(idx - 10, idx + 200)));
}

// Find cf- classes
['cf-inner', 'cf-hint', 'cf-face', 'cf-front', 'cf-back', 'FLIP CHALLENGES', 'FLIP CARDS', 'Tap each card'].forEach(term => {
  const i = content.indexOf(term);
  console.log(`\n"${term}" at:`, i, i >= 0 ? '=> ' + JSON.stringify(content.slice(i, i + 80)) : '');
});

// Show exact content of the CSS block for challenges (search via surrounding context)
const cfIdx = content.indexOf('.cf{');
if (cfIdx >= 0) {
  console.log('\n.cf{ block at:', cfIdx);
  console.log(JSON.stringify(content.slice(cfIdx - 50, cfIdx + 300)));
}

// Show the card HTML section
const chalIdx = content.indexOf('Challenge 01');
if (chalIdx >= 0) {
  console.log('\nChallenge 01 section at:', chalIdx);
  console.log(JSON.stringify(content.slice(chalIdx - 60, chalIdx + 600)));
}
