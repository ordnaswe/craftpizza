# Källor för faktauppgifterna i build.py (kontrollerade 2026-09-09)

| Uppgift | Källa |
|---|---|
| Namn "Craft Pizza Bar – Gustavsberg", telefon 0722080901, öppettider mån–tor/sön 11–22, fre–lör 11–01, biljard & dart, "pizza, kaffe, fika, vin, öl" | Instagram-bio @craft_gustavsberg – https://www.instagram.com/craft_gustavsberg/ |
| Adress Chamottevägen 8, 134 40 Gustavsberg | Instagram/Facebook/HappyCow/öppet.se (samstämmiga) |
| E-post Varmdo@craftsthlm.com, beställningslänk (qopla) | Facebook-sida – https://www.facebook.com/p/Craft-Pizzeria-Gustavsberg-61554418754002/ |
| Festlokal för uthyrning, uteservering mot Konstnärshusets gula chamottetegelvägg, sol eftermiddag/kväll | gustavsbergshamn.se/restauranger/ (ca 2 år gammal) |
| Biljardrum, "ingen bordsbokning behövs" | Facebook-inlägg återgivna på restaurants10.com (2024–2025) |
| Naturvin | Recension på Thatsup (2025-04-29) – enskild gästs uppgift |

## Ej verifierat / avvikelser
- **Öppettider** – öppet.se anger mån–tis 15–22 (sajten flaggar själv datan som gammal). Instagram-bion (mest aktuell) används. Bekräfta med krögaren.
- **Meny och priser** – hittade inga verifierbara rätter/priser (qopla-sidan är JS-renderad). Menyn i build.py är därför tom och länkar till beställningssidan.
- **"Vedugn"** – nämns endast av novacircle.com (AI-liknande text). Jag kan inte bekräfta detta; ordet "vedugnspizza" i heron bör kontrolleras.
- **Veganska pizzor** – HappyCow (2 år gammalt) nämner två märkta veganska pizzor. Ej med på sajten pga ålder.

## Bilder (levererade av Sandro 2026-09-09, ursprung Instagram @craft_gustavsberg)
- `bilder/craft-logo.png` / `craft-logo-vit.png` – logotypen, vit bakgrund gjord transparent, vit variant för mörk bakgrund. 447×447 px.
- `bilder/biljard.jpg` – interiör, beskuren nedtill för att ta bort textöverlägget om julöppettider. 387×440 px.
- `bilder/fasad.jpg` – uteserveringen. 595×336 px.
Bilderna är lågupplösta (skärmdumpar). Be krögaren om originalfiler innan lansering.

## Qopla-inbäddning
Beställningssidan bäddas in med `<iframe>` i sektionen "Meny & beställ". Jag kan inte bekräfta att qopla.com tillåter inbäddning (X-Frame-Options/CSP) – testa i webbläsare efter deploy. Fallback-länk finns under ramen.
