import pulp as pl
from typing import List
from typing import Dict

# typage dans le code...

# sac_dos_v2 ici et plus bas
sac_dos_v2: pl.LpProblem = pl.LpProblem("Sac_a_dos_v2",
                                        pl.LpMaximize)

items: List[str] = ["x1", "x2", "x3",
                    "x4", "x5", "x6",
                    "x7", "x8", "x9",
                    "x10", "x11", "x12"]

var_decisionnelles: Dict[str, pl.LpVariable] = pl.LpVariable.dicts("",
                                                                   items,
                                                                   lowBound=0,
                                                                   upBound=1,
                                                                   cat=pl.LpInteger)

valeur: Dict[str, int] = {"x1": 20,  "x2": 30, "x3": 10,
                          "x4": 90,  "x5": 10, "x6": 40,
                          "x7": 100, "x8": 60, "x9": 70,
                          "x10": 50,  "x11": 30, "x12": 20}

poids: Dict[str, int] = {"x1": 5,  "x2": 6, "x3": 7,
                         "x4": 32, "x5": 2, "x6": 5,
                         "x7": 7,  "x8": 9, "x9": 12,
                         "x10": 11, "x11": 1, "x12": 2}

# fonction objective
# maximiser la valeur des items
fobjective: pl.LpAffineExpression = pl.lpSum( [valeur[i] * var_decisionnelles[i] for i in items])

sac_dos_v2 += fobjective, "La fonction objective maximise la valeur du sac"

# contrainte
# minimiser le poids des items
c1: pl.LpConstraint = pl.lpSum([poids[i] * var_decisionnelles[i] for i in items]) <= 32

sac_dos_v2 += c1, "La contrainte verifie que la capacite du sac ne depasse pas 32kg"

resultat: int = sac_dos_v2.solve(pl.PULP_CBC_CMD(msg=False))

print("La valeur de la fonction objective optimale:", pl.value(sac_dos_v2.objective))

inc: List[str] = []
non_inc: List[str] = []
total: int = 0
for i in sac_dos_v2.variables():
    if i.value() == 1:
        inc.append(i.name)
        total += i.value()
    else:
        non_inc.append(i.name)

inc2: List[str] = []
for i in inc:
    inc2.append(i.replace("_", ""))

non_inc2: List[str] = []
for i in non_inc:
    non_inc2.append(i.replace("_", ""))

print("Liste des items mis dans le sac:", inc2)
print("Liste des items restants:", non_inc2)

contrainte: int = 32
somme: float = 0.0
for i in inc2:
    somme += poids[i]

print(f"Taux de remplissage du sac: {somme}/32 = {somme*100/contrainte}%")
