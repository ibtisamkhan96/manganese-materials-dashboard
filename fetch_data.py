"""
Manganese Materials Data Series - data pipeline.
Compiles cited, verified figures into tidy CSVs for the dashboard and carousel.

Primary sources (verified 2026-06):
- USGS Mineral Commodity Summaries 2026, "Manganese" chapter (world mine production by country
  2024 and 2025 on a manganese-content basis, reserves, China CIF price, US 100% import reliance,
  the "no satisfactory substitute" statement).
  https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-manganese.pdf
- World Steel Association via USGS for the steel link (manganese demand follows steel).

The headline story: manganese is the metal you cannot make steel without. Around 90% of it goes
into steelmaking as a deoxidiser, desulphuriser and strengthener, and USGS states plainly that it
has no satisfactory substitute. The world mines about 20 million tonnes of manganese content a
year, one of the largest of any metal, mostly in South Africa and Gabon. The United States has not
mined any since 1970 and is 100% import reliant. The newer twist is batteries: high-purity
manganese for lithium-ion cathodes, where China dominates the processing.
"""

import pandas as pd
import os

os.makedirs("data", exist_ok=True)

WORLD_MINE_KT = 20_000        # USGS 2025e world manganese mine production, kt of manganese content
WORLD_RESERVES_MT = 1_800     # USGS reserves, 1,800,000 kt = 1,800 Mt gross weight

# 1) Manganese mine production by country, 2025e (kt of manganese content). USGS MCS 2026.
production = pd.DataFrame([
    ["South Africa",   7_600, 38.0],
    ["Gabon",          5_000, 25.0],
    ["Ghana",          2_000, 10.0],
    ["Australia",      1_600,  8.0],
    ["Brazil",           800,  4.0],
    ["India",            790,  4.0],
    ["China",            700,  3.5],
    ["Côte d'Ivoire",    350,  1.8],
    ["Other",          1_300,  6.5],
], columns=["country", "kt", "share_pct"])
production.to_csv("data/production.csv", index=False)

# 2) Manganese reserves by country (Mt, gross weight). USGS MCS 2026; world ~1,800 Mt.
reserves = pd.DataFrame([
    ["Australia",     580],
    ["South Africa",  550],
    ["Brazil",        300],
    ["China",         260],
    ["Gabon",          61],
    ["India",          34],
    ["Ghana",          13],
], columns=["country", "reserves_mt"])
reserves.to_csv("data/reserves.csv", index=False)

# 3) Manganese end-use split (approximate). USGS: demand closely follows steel.
end_uses = pd.DataFrame([
    ["Steelmaking",            90, "deoxidiser, desulphuriser, strength"],
    ["Batteries",               4, "lithium-ion cathodes, dry cells"],
    ["Other",                   6, "chemicals, fertiliser, aluminium alloy"],
], columns=["use", "share_pct", "note"])
end_uses.to_csv("data/end_uses.csv", index=False)

# 4) How big a metal manganese is: annual world output of major metals (Mt). Highlight manganese.
metals = pd.DataFrame([
    ["Aluminium", 72.0],
    ["Copper",    22.0],
    ["Manganese", 20.0],
    ["Zinc",      12.0],
    ["Lead",       4.5],
    ["Nickel",     3.7],
    ["Tin",        0.29],
], columns=["metal", "mt"])
metals.to_csv("data/metals_scale.csv", index=False)

# 5) Price history. Manganese ore, China CIF, annual average USD per metric ton unit. USGS MCS 2026.
price = pd.DataFrame([
    [2021, 5.27],
    [2022, 5.97],
    [2023, 4.80],
    [2024, 5.53],
    [2025, 4.50],
], columns=["year", "china_cif_usd_per_mtu"])
price.to_csv("data/price_history.csv", index=False)

# 6) Supply concentration (% of 2025 mine output). USGS-derived. Not a China story for mining.
concentration = pd.DataFrame([
    ["South Africa",                       38],
    ["Gabon",                              25],
    ["Top 3 (South Africa, Gabon, Ghana)", 73],
    ["Top 5 producers",                    85],
], columns=["measure", "share_pct"])
concentration.to_csv("data/concentration.csv", index=False)

# 7) Scale comparisons (make it tangible).
STEEL_T_PER_YEAR = 1_890_000_000
mn_to_steel_t = WORLD_MINE_KT * 1000 * 0.90
mn_per_tonne_steel = mn_to_steel_t / STEEL_T_PER_YEAR * 1000  # kg per tonne of steel
per_second = WORLD_MINE_KT * 1000 * 1000 / 31_557_600

scale = pd.DataFrame([
    ["Manganese per tonne of steel", round(mn_per_tonne_steel), "kg of manganese in every tonne of steel"],
    ["Steel share", 90, "percent of all manganese that goes into steel"],
    ["Substitutes", 0, "satisfactory substitutes in its major use (USGS)"],
    ["Top two miners", 63, "percent from South Africa and Gabon together"],
    ["Manganese per second", round(per_second), "kg of manganese content mined every second"],
], columns=["item", "value", "unit"])
scale.to_csv("data/scale_comparisons.csv", index=False)

print("Manganese datasets written to data/:")
for f in sorted(os.listdir("data")):
    print("  -", f)
print(f"\nMine production 2025e: ~{WORLD_MINE_KT:,} kt Mn content  |  South Africa 38%, Gabon 25%")
print(f"Steel share ~90%, no satisfactory substitute (USGS)")
print(f"Manganese per tonne of steel: ~{mn_per_tonne_steel:.0f} kg  |  per second ~{per_second:.0f} kg")
print(f"Price 2025 China CIF: ~$4.50/mtu  |  US 100% import reliant, none mined since 1970")
