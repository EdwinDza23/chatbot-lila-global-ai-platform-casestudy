const fs = require('fs');
const filepath = String.raw`d:\Casestudy\Lila Global\V2\index.html`;

let content = fs.readFileSync(filepath, 'utf8');
let changes = 0;

// ── 1. Replace flip CSS ────────────────────────────────────────────────────────
const oldCss = `/* FLIP CHALLENGES */
.chal-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:52px;}
.cf{perspective:1000px;height:172px;cursor:none;}
.cf-inner{position:relative;width:100%;height:100%;transform-style:preserve-3d;transition:transform .65s cubic-bezier(.4,.2,.2,1);}
.cf.flipped .cf-inner{transform:rotateY(180deg);}
.cf-face{position:absolute;inset:0;background:var(--surface);border:.5px solid var(--border);border-radius:4px;padding:24px 26px;backface-visibility:hidden;-webkit-backface-visibility:hidden;}
.cf-front{border-left:2px solid var(--red);}
.cf-back{transform:rotateY(180deg);background:var(--s2);border-left:2px solid #10B981;}
.ch-lbl{font-size:10px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:9px;}
.ch-lbl.p{color:var(--red);}
.ch-lbl.s{color:#10B981;}
.ch-txt{font-size:13px;color:var(--dim);line-height:1.6;font-weight:300;}
.cf-hint{position:absolute;bottom:10px;right:12px;font-size:9px;letter-spacing:.1em;color:var(--dimmer);text-transform:uppercase;}`;

const newCss = `/* CHALLENGE CARDS (static split) */
.chal-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:52px;}
.cf{display:grid;grid-template-columns:1fr 1fr;border-radius:4px;overflow:hidden;border:.5px solid var(--border);transition:box-shadow .25s,transform .25s;}
.cf:hover{transform:translateY(-3px);box-shadow:0 20px 48px rgba(0,0,0,.45);}
.cf-face{background:var(--surface);padding:24px 22px;}
.cf-front{border-left:2px solid var(--red);border-right:.5px solid var(--border);}
.cf-back{background:var(--s2);border-left:2px solid #10B981;}
.ch-lbl{font-size:10px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:9px;}
.ch-lbl.p{color:var(--red);}
.ch-lbl.s{color:#10B981;}
.ch-txt{font-size:13px;color:var(--dim);line-height:1.6;font-weight:300;}`;

if (content.includes(oldCss)) {
  content = content.replace(oldCss, newCss);
  changes++;
  console.log('✓ CSS replaced');
} else {
  console.log('✗ CSS block NOT found — trying line-by-line match');
}

// ── 2. Replace subtitle text ──────────────────────────────────────────────────
const oldDesc = 'Tap each card to flip and reveal how each challenge was resolved.';
const newDesc = 'Each design challenge paired directly with its solution.';
if (content.includes(oldDesc)) {
  content = content.replace(oldDesc, newDesc);
  changes++;
  console.log('✓ Subtitle updated');
} else {
  console.log('✗ Subtitle NOT found');
}

// ── 3. Strip .cf-inner wrappers and cf-hint spans via regex ──────────────────
// This removes: <div class="cf-inner">...</div> wrapper inside each .cf
// and <span class="cf-hint">...</span>

const before3 = content.length;

// Remove cf-hint spans
content = content.replace(/<span class="cf-hint">.*?<\/span>/g, '');

// Unwrap cf-inner: replace <div class="cf-inner"><div class="cf-face ...
// Pattern: inside each .cf, remove the extra cf-inner div wrapper
content = content.replace(/<div class="cf"><div class="cf-inner">(<div class="cf-face[\s\S]*?)<\/div><\/div>/g,
  '<div class="cf">$1</div>');

const after3 = content.length;
if (before3 !== after3) {
  changes++;
  console.log('✓ Card HTML unwrapped (cf-inner + cf-hint removed)');
} else {
  console.log('✗ Card HTML regex found no changes');
}

// ── 4. Remove JS flip click handler ──────────────────────────────────────────
const oldJs = `/* FLIP CARDS */\ndocument.querySelectorAll('.cf').forEach(c=>c.addEventListener('click',()=>c.classList.toggle('flipped')));`;
const newJs = `/* FLIP CARDS — removed (static layout now) */`;
if (content.includes(oldJs)) {
  content = content.replace(oldJs, newJs);
  changes++;
  console.log('✓ JS click handler removed');
} else {
  console.log('✗ JS handler NOT found');
}

fs.writeFileSync(filepath, content, 'utf8');
console.log(`\nDone. Total changes applied: ${changes}`);
