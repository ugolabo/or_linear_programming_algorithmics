import pulp as pl
import matplotlib.pyplot as plt
import numpy as np

print("---problème---")

prob = pl.LpProblem(name="Maximiser", sense=pl.LpMaximize)
prob2 = pl.LpProblem(name="Minimiser", sense=pl.LpMinimize)

x = pl.LpVariable(name="x", lowBound=0, upBound=None, cat=pl.LpInteger)
y = pl.LpVariable(name="y", lowBound=0, upBound=None, cat=pl.LpInteger)

prob += x + 2*y, "Maximum"
prob2 += x + 2*y, "Minimum"

c1: pl.LpConstraint = 2*x + y <= 20, "c1"
c2: pl.LpConstraint = -4*x + 5*y <= 10, "c2"
c3: pl.LpConstraint = -x + 2*y >= -2, "c3"

prob += c1
prob += c2
prob += c3
prob2 += c1
prob2 += c2
prob2 += c3

prob.writeLP("faisabilite.lp")
prob2.writeLP("faisabilite2.lp")

result: int = prob.solve()
result2: int = prob2.solve()


print("---prob maximum---")

#print("résultat:", result)
print("résultat:", pl.LpStatus[result])

print("résultat")
for v in prob.variables():
    print(f"{v.name} = {v.value()}")

print("Maximum:", pl.value(prob.objective))

print("---graphique prob maximum---")
print("voir graphique...")

x = np.linspace(-10, 500)

fig, ax = plt.subplots()

# Contraintes...
y = 20 - 2*x
plt.plot(x, y, label="2x + y <= 20", color="dodgerblue")
y = 2 + (4/5)*x
plt.plot(x, y, label="-4x + 5y <= 10", color="orange")
y = x/2 - 1
plt.plot(x, y, label="-x + 2y >= -2", color="cyan")

# Bornes...
# horizontale...
# bornes de y
# y >= 0
#plt.hlines(y=0, xmin=x.min(), xmax=500, label="y >= 0", color="green")
ax.plot(x, np.zeros_like(x), label="y >= 0", color="green")

# verticale...
# borne de x
# x >= 0
plt.vlines(x=0, ymin=-5, ymax=30, label="x >= 0", color="purple")
#ax.plot(np.zeros_like(y), y, label="x >= 0", color="purple")

# Fonction objective
# valeur arbitraire de 0
y = -x/2
plt.plot(x, y,
         '--',
         label="fct objective arb. 0, 0 = x + 2y",
         color="red")

# valeur optimale de 9.5
# 9.5 est le maximum de 19, 19/2 = 9.5
# augmenter y de 9.5 pour que la droite croise l'optimum
y = -x/2 + 9.5
plt.plot(x, y,
         '-.',
         label="fct objective opt., 9.5 = x + 2y",
         color="orangered")

# Optimum
plt.plot(7, 6,
         'o',
         label="Optimum",
         color="gray",
         alpha=0.6)

plt.text(7, 7, 
         s="Optimum",
         color="black",
         alpha=0.8)

ax = plt.gca()

ax.set_xlim([-5, 20])
ax.set_ylim([-5, 30])

plt.legend(loc="upper right")

plt.show()

print("---prob minimum---")

print("résultat2:", pl.LpStatus[result2])

print("résultat2")
for v in prob2.variables():
    print(f"{v.name} = {v.value()}")

print("Minimum:", pl.value(prob2.objective))
