const fs = require('fs');
const filepath = 'd:\\Casestudy\\Lila Global\\V2\\index.html';
const content = fs.readFileSync(filepath, 'utf8');

// 1. Find dark blue color swatch
['dark','Dark','--blue','#1D3662','cs-swatch','color-row','ds-cell'].forEach(term => {
  const i = content.indexOf(term);
  if (i >= 0) console.log(`"${term}" at ${i}:`, JSON.stringify(content.slice(i, i + 120)));
});

// 2. Find IA checkmarks
const iacCk = content.indexOf('iac-ck');
if (iacCk >= 0) console.log('\niac-ck CSS at:', iacCk, JSON.stringify(content.slice(iacCk - 5, iacCk + 200)));

// 3. Find all iac-ck color usages
let idx = 0;
while ((idx = content.indexOf('iac-ck', idx)) >= 0) {
  console.log('iac-ck occurrence at', idx, ':', JSON.stringify(content.slice(idx - 5, idx + 100)));
  idx += 6;
}
