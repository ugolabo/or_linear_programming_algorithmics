import pulp as pl

# sac_dos_v1 ici et plus bas
sac_dos_v1 = pl.LpProblem("Sac_a_dos_v1", pl.LpMaximize)

x1 = pl.LpVariable(name="x1", lowBound=0, upBound=1, cat=pl.LpInteger)
x2 = pl.LpVariable(name="x2", lowBound=0, upBound=1, cat=pl.LpInteger)
x3 = pl.LpVariable(name="x3", lowBound=0, upBound=1, cat=pl.LpInteger)
x4 = pl.LpVariable(name="x4", lowBound=0, upBound=1, cat=pl.LpInteger)
x5 = pl.LpVariable(name="x5", lowBound=0, upBound=1, cat=pl.LpInteger)
x6 = pl.LpVariable(name="x6", lowBound=0, upBound=1, cat=pl.LpInteger)
x7 = pl.LpVariable(name="x7", lowBound=0, upBound=1, cat=pl.LpInteger)
x8 = pl.LpVariable(name="x8", lowBound=0, upBound=1, cat=pl.LpInteger)
x9 = pl.LpVariable(name="x9", lowBound=0, upBound=1, cat=pl.LpInteger)
x10 = pl.LpVariable(name="x10", lowBound=0, upBound=1, cat=pl.LpInteger)
x11 = pl.LpVariable(name="x11", lowBound=0, upBound=1, cat=pl.LpInteger)
x12 = pl.LpVariable(name="x12", lowBound=0, upBound=1, cat=pl.LpInteger)

fobjective = 20*x1 + 30*x2 + 10*x3 + 90*x4 + 10*x5 + 40*x6 \
    + 100*x7 + 60*x8 + 70*x9 + 50*x10 + 30*x11 + 20*x12
sac_dos_v1 += fobjective, "La fonction objective maximise la valeur du sac"

c1 = 5*x1 + 6*x2 + 7*x3 + 32*x4 + 2*x5 + 5*x6 \
    + 7*x7 + 9*x8 + 12*x9 + 11*x10 + 1*x11 + 2*x12 <= 32
sac_dos_v1 += c1, "La contrainte verifie que la capacite du sac ne depasse pas 32kg"

# aucune trace par défaut
resultat = sac_dos_v1.solve(pl.PULP_CBC_CMD(msg=False))

# message personnalisé à la place de la trace par défaut
if pl.LpStatus[resultat] == "Optimal":
    print("La valeur de la fonction objective optimale =", pl.value(sac_dos_v1.objective))
else:
    print("Il n'y a pas de solution optimale")

"""
Une contrainte invraisemblable du genre: le poids maximal doit être -1

c1 = 5*x1 + 6*x2 + 7*x3 + 32*x4 + 2*x5 + 5*x6 + 7*x7 + 9*x8 + 12*x9 + 11*x10 + 1*x11 + 2*x12 <= -1

Le statut serait 'Infeasible'
"""
