import pulp as pl
import matplotlib.pyplot as plt
import numpy as np

print("---problème---")

prob = pl.LpProblem(name="Maximiser", sense=pl.LpMaximize)

x = pl.LpVariable(name="x", lowBound=0, upBound=None, cat=pl.LpInteger)
y = pl.LpVariable(name="y", lowBound=0, upBound=None, cat=pl.LpInteger)

prob += x + 2*y, "Maximum"


c1: pl.LpConstraint = 2*x + y <= 20, "c1"
c2: pl.LpConstraint = -4*x + 5*y <= 10, "c2"
c3: pl.LpConstraint = -x + 2*y >= -2, "c3"

prob += c1
prob += c2
prob += c3

result: int = prob.solve()

print("résultat:", pl.LpStatus[result])
print("statuts possibles ", pl.LpStatus)


for v in prob.variables():
    print(f"{v.name} = {v.value()}")

print("Maximum:", pl.value(prob.objective))



print("---graphique---")

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

ax = plt.gca()

ax.set_xlim([-5, 20])
ax.set_ylim([-5, 30])

plt.legend(loc="upper right")

plt.show()
