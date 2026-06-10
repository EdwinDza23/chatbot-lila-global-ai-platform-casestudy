import re

filepath = r'd:\Casestudy\Lila Global\V2\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# ── 1. Replace flip CSS ────────────────────────────────────────────────────────
old_css = """/* FLIP CHALLENGES */
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
.cf-hint{position:absolute;bottom:10px;right:12px;font-size:9px;letter-spacing:.1em;color:var(--dimmer);text-transform:uppercase;}"""

new_css = """/* CHALLENGE CARDS (static split) */
.chal-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:52px;}
.cf{display:grid;grid-template-columns:1fr 1fr;border-radius:4px;overflow:hidden;border:.5px solid var(--border);transition:box-shadow .25s,transform .25s;}
.cf:hover{transform:translateY(-3px);box-shadow:0 20px 48px rgba(0,0,0,.45);}
.cf-face{background:var(--surface);padding:24px 22px;}
.cf-front{border-left:2px solid var(--red);border-right:.5px solid var(--border);}
.cf-back{background:var(--s2);border-left:2px solid #10B981;}
.ch-lbl{font-size:10px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:9px;}
.ch-lbl.p{color:var(--red);}
.ch-lbl.s{color:#10B981;}
.ch-txt{font-size:13px;color:var(--dim);line-height:1.6;font-weight:300;}"""

if old_css in content:
    content = content.replace(old_css, new_css, 1)
    changes += 1
    print("✓ CSS replaced")
else:
    print("✗ CSS block NOT found — check whitespace")

# ── 2. Replace subtitle text ──────────────────────────────────────────────────
old_desc = 'Tap each card to flip and reveal how each challenge was resolved.'
new_desc = 'Each design challenge paired directly with its solution.'
if old_desc in content:
    content = content.replace(old_desc, new_desc, 1)
    changes += 1
    print("✓ Subtitle updated")
else:
    print("✗ Subtitle NOT found")

# ── 3. Replace the 4 flip card HTML blocks with static split cards ─────────────
cards = [
    (
        '<div class="cf"><div class="cf-inner"><div class="cf-face cf-front"><div class="ch-lbl p">Challenge 01</div><p class="ch-txt">Enterprise products become cluttered with features competing for attention, overwhelming users.</p><span class="cf-hint">Tap to flip \u2192</span></div><div class="cf-face cf-back"><div class="ch-lbl s">Solution</div><p class="ch-txt">Navigation kept to 3 elements. Workspace panel collapses. Clutter has nowhere to live.</p></div></div></div>',
        '<div class="cf"><div class="cf-face cf-front"><div class="ch-lbl p">Challenge 01</div><p class="ch-txt">Enterprise products become cluttered with features competing for attention, overwhelming users.</p></div><div class="cf-face cf-back"><div class="ch-lbl s">Solution</div><p class="ch-txt">Navigation kept to 3 elements. Workspace panel collapses. Clutter has nowhere to live.</p></div></div>'
    ),
    (
        '<div class="cf"><div class="cf-inner"><div class="cf-face cf-front"><div class="ch-lbl p">Challenge 02</div><p class="ch-txt">Multiple AI models create selection complexity \u2014 users don\u2019t know when or why to switch models.</p><span class="cf-hint">Tap to flip \u2192</span></div><div class="cf-face cf-back"><div class="ch-lbl s">Solution</div><p class="ch-txt">Model selector inside the chat composer \u2014 contextual, not buried in settings. One tap to switch.</p></div></div></div>',
        '<div class="cf"><div class="cf-face cf-front"><div class="ch-lbl p">Challenge 02</div><p class="ch-txt">Multiple AI models create selection complexity \u2014 users don\u2019t know when or why to switch models.</p></div><div class="cf-face cf-back"><div class="ch-lbl s">Solution</div><p class="ch-txt">Model selector inside the chat composer \u2014 contextual, not buried in settings. One tap to switch.</p></div></div>'
    ),
    (
        '<div class="cf"><div class="cf-inner"><div class="cf-face cf-front"><div class="ch-lbl p">Challenge 03</div><p class="ch-txt">Three capability areas can feel disconnected \u2014 undermining the \u201cone platform\u201d promise.</p><span class="cf-hint">Tap to flip \u2192</span></div><div class="cf-face cf-back"><div class="ch-lbl s">Solution</div><p class="ch-txt">Unified workspace architecture with consistent card components. All three areas share identical visual language.</p></div></div></div>',
        '<div class="cf"><div class="cf-face cf-front"><div class="ch-lbl p">Challenge 03</div><p class="ch-txt">Three capability areas can feel disconnected \u2014 undermining the \u201cone platform\u201d promise.</p></div><div class="cf-face cf-back"><div class="ch-lbl s">Solution</div><p class="ch-txt">Unified workspace architecture with consistent card components. All three areas share identical visual language.</p></div></div>'
    ),
    (
        '<div class="cf"><div class="cf-inner"><div class="cf-face cf-front"><div class="ch-lbl p">Challenge 04</div><p class="ch-txt">Non-technical maritime professionals need to adopt a complex AI platform without training.</p><span class="cf-hint">Tap to flip \u2192</span></div><div class="cf-face cf-back"><div class="ch-lbl s">Solution</div><p class="ch-txt">Chat-first experience on familiar patterns. Domain-specific prompt suggestions. Zero-onboarding by design.</p></div></div></div>',
        '<div class="cf"><div class="cf-face cf-front"><div class="ch-lbl p">Challenge 04</div><p class="ch-txt">Non-technical maritime professionals need to adopt a complex AI platform without training.</p></div><div class="cf-face cf-back"><div class="ch-lbl s">Solution</div><p class="ch-txt">Chat-first experience on familiar patterns. Domain-specific prompt suggestions. Zero-onboarding by design.</p></div></div>'
    ),
]

for i, (old, new) in enumerate(cards, 1):
    if old in content:
        content = content.replace(old, new, 1)
        changes += 1
        print(f"✓ Card {i:02d} replaced")
    else:
        # Try with straight quotes / apostrophes as fallback
        print(f"✗ Card {i:02d} NOT found — trying regex fallback")
        # Use a regex to find and replace the card block
        pattern = rf'<div class="cf"><div class="cf-inner">(<div class="cf-face cf-front">.*?</div>)(<div class="cf-face cf-back">.*?</div>)</div></div>'
        # We'll handle all 4 in a batch below

# ── 4. Batch regex fallback for all 4 cards ────────────────────────────────────
# Only run if some cards were still not replaced (changes < expected 6)
if changes < 6:
    print("\nRunning regex fallback for remaining cards...")
    pattern = r'<div class="cf"><div class="cf-inner">(<div class="cf-face cf-front">.*?</div>)(<div class="cf-face cf-back">.*?</div>)</div></div>'
    replacement = r'<div class="cf">\1\2</div>'
    new_content, n = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if n:
        content = new_content
        # Remove cf-hint spans that remain
        content = re.sub(r'<span class="cf-hint">.*?</span>', '', content)
        changes += n
        print(f"✓ Regex fallback replaced {n} card(s) and removed hints")
    else:
        print("✗ Regex fallback also found nothing")

# ── 5. Remove JS flip click handler ──────────────────────────────────────────
old_js = """/* FLIP CARDS */
document.querySelectorAll('.cf').forEach(c=>c.addEventListener('click',()=>c.classList.toggle('flipped')));"""
new_js = "/* FLIP CARDS — removed (static layout now) */"
if old_js in content:
    content = content.replace(old_js, new_js, 1)
    changes += 1
    print("✓ JS click handler removed")
else:
    print("✗ JS handler NOT found")

# ── Save ──────────────────────────────────────────────────────────────────────
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone. Total changes applied: {changes}")
