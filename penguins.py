import csv
from pathlib import Path
from statistics import mean







def avg_bodymass_by_species_sex(rows: list[dict]) -> list[tuple]:
   
    groups: dict[tuple, list[float]] = {}
    for r in rows:
        species = (r.get("species") or "").strip()
        sex = (r.get("sex") or "").strip().title()  
        mass = _to_float(r.get("body_mass_g"))
        if not species or not sex or mass is None:
            continue
        groups.setdefault((species, sex), []).append(mass)

    out = []
    for (species, sex), vals in groups.items():
        if vals:
            out.append((species, sex, round(mean(vals), 1)))

    return sorted(out, key=lambda t: (t[0], t[1]))
