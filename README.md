# Manganese, Materials Data Series #15

An interactive data dashboard and LinkedIn carousel on the metal you cannot make steel without, and almost nobody can name. About 90% of manganese goes into steelmaking, it has no satisfactory substitute, and at roughly 20 million tonnes of manganese content a year it is one of the largest metal markets on Earth. The ore is mostly African (South Africa and Gabon), the processing leans on China, and it is now becoming a battery metal too.

Part of my Materials Data Series, where I take one material at a time and tell it as a materials engineer who works in data. Steel, aluminium, copper, rare earths, lithium, nickel, cobalt, titanium, graphite, silicon, silver, tin, magnesium and tungsten came first. Zinc is next.

**Live dashboard:** _(deploy `index.html` to Netlify/GitHub Pages)_

---

## What's inside

| File | What it is |
|------|-----------|
| `index.html` | Interactive Chart.js dashboard, 5 tabs: Production & Geography (with a highlighted world map), The Steel Backbone, Where It Goes, Supply & Risk, Why It Matters |
| `fetch_data.py` | Reproducible Python pipeline that compiles the cited figures into `data/*.csv` |
| `data/*.csv` | Tidy datasets (production, reserves, end uses, metals-scale comparison, price history, supply concentration, scale anchors) |
| `carousel/index.html` | 9-slide LinkedIn carousel (1080x1080) |
| `Manganese_Materials_Carousel.pdf` | Exported carousel, ready to upload |
| `linkedin-post.txt` | Post caption, with the LinkedIn document title and GitHub slug at the top |

## Reproduce the data

```bash
python fetch_data.py      # writes data/*.csv
```

The dashboard embeds the same numbers in JS so it runs from `file://` with no server.

## What the data shows

- The world mined about **20 million tonnes of manganese content in 2025**, one of the largest metal markets there is, more than zinc, nickel, lead and tin combined.
- About **90% of manganese goes into steelmaking**, as ferroalloys that remove oxygen and sulphur and add strength and hardness. USGS states it has **no satisfactory substitute** in its major use.
- Mining is concentrated in **Africa**: **South Africa about 38%** and **Gabon about 25%**, with the top three (adding Ghana) about **73%**. China, the dominant consumer and processor, barely mines any.
- The **processing** is a separate dependency: China dominates the ferroalloys and the **battery-grade manganese sulphate** wanted for electric-vehicle cathodes (NMC and the cheaper LMFP). The United States mines **none** and is 100% import reliant.
- The price moves in a narrow band around **$5 per metric ton unit** (China CIF) and tracks steel demand rather than spiking; it eased in 2025 as steel consumption stayed flat.

## Sources

USGS Mineral Commodity Summaries 2026, the Manganese chapter (world mine production by country for 2024 and 2025 on a manganese-content basis, reserves, China CIF price, US 100% import reliance, the no-satisfactory-substitute statement). The steel link follows USGS and the World Steel Association.

Mine production in thousand tonnes of manganese content; reserves in million tonnes gross weight. The end-use split is approximate (USGS notes manganese demand closely follows steel). Prices are manganese ore China CIF annual averages in USD per metric ton unit. The metals-scale chart shows approximate annual world output of each metal and is indicative. Figures rounded and attributed.

---

*Built by Ibtisam Ahmed Khan · June 2026 · [linkedin.com/in/ibtisam-ahmed-khan](https://linkedin.com/in/ibtisam-ahmed-khan)*
