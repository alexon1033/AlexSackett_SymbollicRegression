import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

E = np.e

x1 = 2 
x2 = np.linspace(6, 8.5, 1000)

data = pd.read_csv("data/setF.csv", delimiter=',', header=None, names=['x1','x2','y'])

pf = pd.read_csv("log/._data_setF_2023-01-19-172533/dso_._data_setF_0_pf.csv", usecols=['complexity','r','expression'])

for complexity, r, expression in zip(pf['complexity'], pf['r'], pf['expression']):
    expr = expression

    expr = re.sub('[\[\]]', '', expr)
    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('log', 'np.log', expr)

    exec("def f_{0}(x1, x2): return {1}".format(complexity, expr))
    

plt.errorbar(data['x2'].where(data['x1']==x1), data['y'].where(data['x1']==x1), xerr=0.1, yerr=0.01, capsize=0.1)

plt.plot(x2, f_195(x1, x2))

plt.show()
