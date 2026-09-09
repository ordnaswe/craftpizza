#!/usr/bin/env python3
"""
build.py – bygger dist/ för Craft Pizza Bar, Gustavsberg.
Endast standardbibliotek. Redigera DATA nedan, kör: python3 build.py
Bilder ligger i bilder/ och kopieras till dist/bilder/.
"""
from pathlib import Path
import html, shutil

ROOT = Path(__file__).parent

# --------------------------------------------------------------------------
# FAKTA (källor i KÄLLOR.md). Ändra här – aldrig i dist/index.html.
# --------------------------------------------------------------------------
DATA = {
    "namn": "Craft Pizza Bar",
    "ort": "Gustavsberg",
    "adress": "Chamottevägen 8",
    "postadress": "134 40 Gustavsberg",
    "telefon": "072-208 09 01",
    "telefon_tel": "+46722080901",
    "epost": "varmdo@craftsthlm.com",
    "instagram": "craft_gustavsberg",
    "bestall_url": "https://qopla.com/restaurant/craft-pizzeria-gustavsberg/qWEVOwmL1y/order",
    "karta_url": "https://www.openstreetmap.org/search?query=Chamottev%C3%A4gen%208%2C%20Gustavsberg",
    # Öppettider enligt Instagram-bion (@craft_gustavsberg). Verifiera med krögaren.
    "oppettider": [
        ("Måndag–torsdag", "11–22"),
        ("Fredag–lördag", "11–01"),
        ("Söndag", "11–22"),
    ],
}

def esc(s: str) -> str:
    return html.escape(s, quote=True)

def render_hours(rows):
    return "\n".join(
        f'<div class="row"><span>{esc(d)}</span><span>{esc(t)}</span></div>'
        for d, t in rows
    )

CSS = r"""
:root{
  --sot:#141414;        /* logotypens svärta, biljardrummet */
  --sot-ljus:#222220;
  --porslin:#EDEFEC;    /* glaserat vitt */
  --chamotte:#C79A2B;   /* fasadens gula tegel */
  --aska:#8E8D88;
  --max:1120px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--sot);color:var(--porslin);
  font-family:"Barlow",system-ui,-apple-system,"Segoe UI",sans-serif;font-size:1.0625rem;line-height:1.55}
a{color:inherit}
a:focus-visible,button:focus-visible{outline:3px solid var(--chamotte);outline-offset:3px}
img{max-width:100%;height:auto;display:block}
.wrap{max-width:var(--max);margin:0 auto;padding:0 1.25rem}
h1,h2,h3{font-family:"Barlow Condensed",sans-serif;line-height:1;margin:0}
.btn{display:inline-block;background:var(--porslin);color:var(--sot);text-decoration:none;font-weight:600;padding:.8rem 1.25rem;border-radius:3px}
.btn:hover{background:#fff}
.btn.gul{background:var(--chamotte);color:var(--sot)}
.btn.gul:hover{background:#d9ab35}
.btn.ram{background:transparent;color:var(--porslin);border:1.5px solid var(--porslin)}
.btn.ram:hover{background:rgba(255,255,255,.08)}

/* ---- topp ---- */
header{position:sticky;top:0;z-index:5;background:rgba(20,20,20,.92);backdrop-filter:blur(6px);border-bottom:1px solid #2c2c2c}
.top{display:flex;align-items:center;justify-content:space-between;gap:1rem;padding:.6rem 0}
.top img{width:52px;height:52px}
nav{display:flex;gap:1.5rem}
nav a{text-decoration:none;font-weight:500;border-bottom:2px solid transparent;padding-bottom:2px}
nav a:hover{border-color:var(--chamotte)}

/* ---- hero ---- */
.hero .wrap{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;padding:3rem 1.25rem 4rem}
.hero .logo{width:min(420px,80%);margin:0 auto 1.5rem}
.hero h1{font-weight:800;font-size:clamp(2.6rem,6vw,4.6rem);letter-spacing:-.01em;margin-bottom:1rem}
.hero p.lead{font-size:1.2rem;max-width:36ch;color:#cfd1cc;margin:0 0 1.75rem}
.hero .cta{display:flex;gap:.75rem;flex-wrap:wrap}
.hero figure{margin:0;position:relative}
.hero figure img{border-radius:4px;width:100%;aspect-ratio:387/440;object-fit:cover}
.hours{background:var(--porslin);color:var(--sot);padding:1.25rem 1.5rem;border-radius:4px;position:absolute;left:-2rem;bottom:-2rem;min-width:280px;box-shadow:0 20px 40px rgba(0,0,0,.5)}
.hours h2{font-size:1.2rem;font-weight:600;margin-bottom:.75rem;letter-spacing:.03em}
.hours .row{display:flex;justify-content:space-between;gap:1.5rem;padding:.45rem 0;border-top:1px solid #d0d2ce;font-variant-numeric:tabular-nums}
.hours .row:first-of-type{border-top:0}
.hours .row span:last-child{font-family:"Barlow Condensed",sans-serif;font-size:1.3rem;font-weight:700}

/* ---- sektioner ---- */
section{padding:4.5rem 0}
section h2{font-weight:700;font-size:clamp(2rem,4.5vw,3rem);margin-bottom:1.25rem}
.two{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center}
.two p{max-width:58ch;color:#cfd1cc}

/* ---- meny/beställ (Qopla) ---- */
.bestall{background:var(--porslin);color:var(--sot)}
.bestall p{color:#3f3f3c;max-width:60ch;margin:0 0 1.5rem}
.qopla{border:1px solid #cfd1cc;border-radius:4px;overflow:hidden;background:#fff}
.qopla iframe{display:block;width:100%;height:min(82vh,900px);border:0}
.qopla-fallback{padding:1rem 1.25rem;border-top:1px solid #cfd1cc;font-size:.95rem;display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;align-items:center}

/* ---- fest ---- */
.fest img{border-radius:4px}
.tags{display:flex;flex-wrap:wrap;gap:.5rem;margin:1.25rem 0 1.75rem;padding:0;list-style:none}
.tags li{border:1.5px solid var(--porslin);padding:.35rem .8rem;border-radius:999px;font-weight:500}

/* ---- hitta ---- */
.hitta{background:var(--sot-ljus)}
.hitta img{border-radius:4px}
address{font-style:normal;font-size:1.2rem;line-height:1.7;margin-bottom:1.25rem}

footer{padding:2rem 0 2.5rem;font-size:.9rem;color:var(--aska)}
footer .wrap{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;align-items:center}
footer img{width:40px;height:40px;opacity:.6}

@media (max-width:820px){
  .hero .wrap{grid-template-columns:1fr;padding:2rem 1.25rem 3rem;gap:2rem}
  .hero figure{margin-bottom:0}
  .hours{position:static;box-shadow:none;margin-top:1rem;min-width:0}
  .two{grid-template-columns:1fr;gap:2rem}
  nav{display:none}
  section{padding:3.25rem 0}
  .qopla iframe{height:75vh}
}
"""

def page() -> str:
    d = DATA
    return f"""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(d['namn'])} – {esc(d['ort'])}</title>
<meta name="description" content="Pizza, kaffe, vin, öl, biljard och dart i Gustavsbergs hamn. {esc(d['adress'])}, {esc(d['postadress'])}.">
<link rel="icon" href="bilder/craft-logo.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">
{{
 "@context":"https://schema.org","@type":"Restaurant",
 "name":"{esc(d['namn'])} {esc(d['ort'])}",
 "servesCuisine":"Pizza",
 "telephone":"{esc(d['telefon_tel'])}",
 "email":"{esc(d['epost'])}",
 "logo":"bilder/craft-logo.png",
 "address":{{"@type":"PostalAddress","streetAddress":"{esc(d['adress'])}","postalCode":"134 40","addressLocality":"Gustavsberg","addressCountry":"SE"}},
 "sameAs":["https://www.instagram.com/{esc(d['instagram'])}/"]
}}
</script>
</head>
<body>

<header>
  <div class="wrap top">
    <a href="#" aria-label="Craft – till toppen"><img src="bilder/craft-logo-vit.png" alt="Craft"></a>
    <nav aria-label="Huvudmeny">
      <a href="#bestall">Meny &amp; beställ</a>
      <a href="#fest">Fest &amp; biljard</a>
      <a href="#hitta">Hitta hit</a>
    </nav>
    <a class="btn gul" href="#bestall">Beställ</a>
  </div>
</header>

<main>
<div class="hero">
  <div class="wrap">
    <div>
      <img class="logo" src="bilder/craft-logo-vit.png" alt="Craft – pizzabagare med pizzaspade" width="447" height="447">
      <h1>Pizza, öl och biljard i Gustavsbergs hamn.</h1>
      <p class="lead">Pizza, kaffe och fika på dagen. Vin, öl, dart och biljard på kvällen. Uteservering mot den gula tegelfasaden.</p>
      <div class="cta">
        <a class="btn gul" href="#bestall">Beställ takeaway</a>
        <a class="btn ram" href="tel:{esc(d['telefon_tel'])}">Ring {esc(d['telefon'])}</a>
      </div>
    </div>
    <figure>
      <img src="bilder/biljard.jpg" alt="Biljardrummet på Craft med två biljardbord under kvällsbelysning" width="387" height="440">
      <div class="hours" aria-labelledby="oppet">
        <h2 id="oppet">Öppettider</h2>
        {render_hours(d['oppettider'])}
      </div>
    </figure>
  </div>
</div>

<section id="bestall" class="bestall">
  <div class="wrap">
    <h2>Meny &amp; beställ</h2>
    <p>Bläddra i menyn och beställ takeaway direkt här. Betalning sker i beställningsvyn.</p>
    <div class="qopla">
      <iframe src="{esc(d['bestall_url'])}" title="Meny och beställning – Craft Gustavsberg" loading="lazy" allow="payment"></iframe>
      <div class="qopla-fallback">
        <span>Visas inte menyn? Öppna beställningssidan i ett eget fönster.</span>
        <a class="btn" href="{esc(d['bestall_url'])}" target="_blank" rel="noopener">Öppna beställningssidan</a>
      </div>
    </div>
  </div>
</section>

<section id="fest" class="fest">
  <div class="wrap two">
    <div>
      <h2>Fest, biljard och dart</h2>
      <p>Biljardrum och dart mitt i pizzerian – ingen bordsbokning behövs, kom som du är. Lokalen går också att boka för privata fester.</p>
      <ul class="tags"><li>Biljard</li><li>Dart</li><li>Öl</li><li>Naturvin</li><li>Uteservering</li></ul>
      <a class="btn gul" href="mailto:{esc(d['epost'])}">Boka lokalen – {esc(d['epost'])}</a>
    </div>
    <img src="bilder/fasad.jpg" alt="Gäster på uteserveringen framför Crafts gula tegelfasad en sommarkväll" width="595" height="336">
  </div>
</section>

<section id="hitta" class="hitta">
  <div class="wrap two">
    <div>
      <h2>Hitta hit</h2>
      <address>
        {esc(d['adress'])}<br>
        {esc(d['postadress'])}<br>
        <a href="tel:{esc(d['telefon_tel'])}">{esc(d['telefon'])}</a><br>
        <a href="mailto:{esc(d['epost'])}">{esc(d['epost'])}</a>
      </address>
      <p>I det gamla porslinsbrukets kvarter i Gustavsbergs hamn. Uteserveringen får sol på eftermiddag och kväll.</p>
      <a class="btn ram" href="{esc(d['karta_url'])}">Visa på karta</a>
    </div>
    <div>
      <img src="bilder/craft-logo-vit.png" alt="" width="447" height="447" style="width:220px;margin:0 auto">
    </div>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <img src="bilder/craft-logo-vit.png" alt="">
    <span>© {esc(d['namn'])} {esc(d['ort'])}</span>
    <a href="https://www.instagram.com/{esc(d['instagram'])}/">@{esc(d['instagram'])} på Instagram</a>
  </div>
</footer>
</body>
</html>
"""

if __name__ == "__main__":
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    if (dist / "bilder").exists():
        shutil.rmtree(dist / "bilder")
    shutil.copytree(ROOT / "bilder", dist / "bilder")
    out = dist / "index.html"
    out.write_text(page(), encoding="utf-8")
    print(f"Skrev {out} ({out.stat().st_size} bytes) + {len(list((dist/'bilder').iterdir()))} bilder")
