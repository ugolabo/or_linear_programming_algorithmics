# Programmation linéaire, recherche opérationnelle et algorithmique 

**Objectif:** maitriser les fondements de la programmation fonctionnelle en Python, de la programmation défensive, de la programmation orientée objet, de l'algorithmique, de la programmation linéaire et aborder la programmation mixte.

- Programmation fonctionnelle et plus: employer les fonctions, les décorateurs pour modifier temporairement une fonction avec une autre fonction; utiliser des modules standards comme `itertools`, `random`, `os`, `sys`, `time`, `datetime`, des modules scientifiques comme `numpy`, `pandas`, `matplotlib`; déployer des environnements virtuels, élaborer des fichiers de déploiement `requirements.txt` avec `pipreqs`

decorators.jpg

- Programmation défensive et plus: employer les conventions et les bonnes pratiques avec les PEP et `pylint`; gérer les erreurs, les exceptions (`try`); aborder des patrons de conception, le débogueur `pdp`, le typage et `mypy`

|   |   |   |
|:---|:---|:---|
| <img src="img/pep8.jpg" alt="" width="300"> | <img src="img/pylint.jpg" alt="" width="300">  | <img src="img/mypy.jpg" alt="" width="300">  |

- Programmation orientée objet et plus: employer les classes, les classes abstraites (`from abc import ABC`, `abstractmethod`), l'héritage, les itérateurs, la surcharge pour redéfinir une méthode dans une sous-classe ou faire du polymorphisme sur différents types, les constructeurs, les instances, les attributs et méthodes de classe, les attributs et méthodes d'instance, les variables et constantes de classe et d'instance; documenter le code source avec les *docstring*; gérer des paquets de fichiers

|   |   |   |
|:---|:---|:---|
| <img src="img/oop.jpg" alt="" width="300"> | <img src="img/oop2.jpg" alt="" width="300">  | <img src="img/package.jpg" alt="" width="300">  |

- Algorithmique: employer des notions tirées d’Artificial Intelligence, A Modern Approach, Stuart Russell et Peter Norvig; employer A* en Python 2.7 format portable; aborder la programmation dynamique et la récursivité, les structures linéaires comme une pile (*stack*), une file (*queue*), les algorithmes gloutons; solutionner des problèmes classiques comme celui du sac à dos (*knapsack problem*) avec différentes approches pour changer résultats

|   |   |   |
|:---|:---|:---|
| <img src="img/aima.jpg" alt="" width="250"> | <img src="img/stack.jpg" alt="" width="300">  | <img src="img/queue.jpg" alt="" width="300">  |
|   | <img src="img/astar2.jpg" alt="" width="300">  | <img src="img/astar.jpg" alt="" width="300">  |

- Programmation linéaire et plus: utiliser `pulp` pour solutionner des problèmes de planification, de production, de transport, pour maximiser les profits ou minimiser les coûts, déterminer les variables décisionnelles, les fonctions objectives avec différents types de frontières, les contraintes, utiliser différents algorithmes de solution, visualiser les zones de faisabilité; travailler avec des listes, des dictionnaires ou des DataFrames Pandas; aborder la programmation mixte avec `mip`

PuLP: faisabilité

faisabilite.jpg
faisabilite2.jpg
max.jpg

PuLP: sac à dos

knapsack.jpg
