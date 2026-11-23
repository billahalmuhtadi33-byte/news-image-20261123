# The World Today — Monday, 23 November 2026

Entry for the make.fun bounty
**[Sum up 23 November's world news in one image](https://make.fun/bounty/news-image-20261123)**
(`news-image-20261123`, $100, 50 places paid).

## What it is

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` — a 1024×1024 PNG, under 1 MiB — to `/output/entry.png`.
No network, fully deterministic: every run writes the same bytes.

The image sums up the day's world news in four illustrated panels
plus a footer strip:

1. **COP31 COLLAPSES** — the UN climate talks in Antalya, Turkey,
   collapsed on Sunday 22 November after countries failed to agree on
   a deal; the final draft did not even mention fossil fuels.
   Sources: CNN, Wall Street Journal, Le Monde.
2. **HORMUZ ON EDGE** — Iran's IRGC said it struck US positions at
   two bases in Bahrain (Al-Riffa and Awali), a civilian industrial
   facility in Sitra caught fire, two people were injured, and
   tankers were hit in the Strait of Hormuz as the US blockade
   passed 130 days. Sources: CNBC Indonesia / Bangkok Post,
   Madhyamam, The Geneva Times.
3. **KYIV UNDER FIRE** — a Russian drone destroyed part of a
   five-storey apartment block in Dymer, Kyiv region; at least one
   person killed and 14–15 missing, nine evacuated.
   Sources: Reuters, Euronews / Europe Says.
4. **EL CHAPO ISIDRO CAUGHT** — Mexican special forces captured
   Fausto Isidro Meza-Flores, "El Chapo Isidro", an FBI Ten Most
   Wanted fugitive, in Guasave, Sinaloa, on 20 November; 11 people
   were killed in the gunfight that followed. Sources: CNN,
   Wall Street Journal, The Times.
5. **ALSO** — South Korea's education minister resigned over an
   AI-driven exam-cheating scandal.

All five stories led the world-news coverage published on
23 November 2026.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
