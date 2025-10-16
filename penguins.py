

import csv
from pathlib import Path
from statistics import mean




def to_float(x):
    try:
        return float(str(x).strip())
    except (TypeError, ValueError):
        return None

def read_penguins(csv_path: str | Path) -> list[dict]:

    with open(csv_path, newline="") as f:
        return list(csv.DictReader(f))

def write_csv_rows(rows: list[tuple], header: list[str], out_path: str | Path):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)












def avg_bodymass_by_species_sex(rows: list[dict]) -> list[tuple]:
 
   groups: dict[tuple, list[float]] = {}
   for r in rows:
       species = (r.get("species") or "").strip()
       sex = (r.get("sex") or "").strip().title() 
       mass = to_float(r.get("body_mass_g"))
       if not species or not sex or mass is None:
           continue
       groups.setdefault((species, sex), []).append(mass)


   out = []
   for (species, sex), vals in groups.items():
       if vals:
           out.append((species, sex, round(mean(vals), 1)))


   return sorted(out, key=lambda t: (t[0], t[1]))


def avg_flipper_by_species_island(rows: list[dict]) -> list[tuple]:
  
   groups: dict[tuple, list[float]] = {}
   for r in rows:
       species = (r.get("species") or "").strip()
       island = (r.get("island") or "").strip()
       fl  = to_float(r.get("flipper_length_mm"))
       if not species or not island or fl is None:
           continue
       groups.setdefault((species, island), []).append(fl)


   out = []
   for (species, island), vals in groups.items():
       if vals:
           out.append((species, island, round(mean(vals), 2)))
   return sorted(out, key=lambda t: (t[0], t[1]))
