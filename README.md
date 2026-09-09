# Craft Pizza Bar – Gustavsberg

Statisk sajt. `build.py` (endast stdlib) genererar `dist/` från `DATA` i filen och `bilder/`.
Redigera aldrig `dist/index.html` direkt.

## Lokalt
    python3 build.py && open dist/index.html

## Deploy
Push till `main` → GitHub Actions bygger och deployar `dist/` till Netlify (`.github/workflows/deploy.yml`).
Kräver två repo-secrets: `NETLIFY_AUTH_TOKEN` (Netlify → User settings → Personal access tokens) och `NETLIFY_SITE_ID` (Netlify → Site → Site configuration → Site ID).

`netlify.toml` gör att Netlify även kan bygga själv om repot kopplas direkt i Netlify UI.

Faktakällor: `KÄLLOR.md`.
