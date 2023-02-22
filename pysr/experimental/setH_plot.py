import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

E = np.e

x = np.linspace(10,60,100)

data = pd.read_csv("data/setH.csv", delimiter=',', header=None, names=['x','y'])

pf = pd.read_csv("log/._data_setH_2022-12-05-164334/dso_._data_setH_0_pf.csv", usecols=['complexity','r','expression'])

for complexity, r, expression in zip(pf['complexity'], pf['r'], pf['expression']):
    expr = expression

    expr = re.sub('[\[\]]', '', expr)
    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('log', 'np.log', expr)

    exec("def f_{0}(x1): return {1}".format(complexity, expr))
    

plt.errorbar(data['x'], data['y'], xerr=1, yerr=[0.14, 0.2, 0.33, 0.13, 0.3, 1.15], capsize=0.1)

plt.plot(x, f_22(x), 'r-')
plt.show()
