import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

E = np.e

x = np.linspace(0,16,100)

data = pd.read_csv("data/setE.csv", delimiter=',', header=None, names=['x','y'])

pf = pd.read_csv("log/._data_setE_2022-12-05-163249/dso_._data_setE_0_pf.csv", usecols=['complexity','r','expression'])

for complexity, r, expression in zip(pf['complexity'], pf['r'], pf['expression']):
    expr = expression

    expr = re.sub('[\[\]]', '', expr)
    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('log', 'np.log', expr)

    exec("def f_{0}(x1): return {1}".format(complexity, expr))
    

plt.errorbar(data['x'], data['y'], xerr=0.5, yerr=0.01)

plt.plot(x, f_53(x), 'r-')
plt.show()
