import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

E = np.e

x1 = np.linspace(-3,12,100)
x2 = 7

data = pd.read_csv("data/setF.csv", delimiter=',', header=None, names=['x1','x2','y'])

pf = pd.read_csv("log/._data_setF_2022-12-05-170246/dso_._data_setF_0_pf.csv", usecols=['complexity','r','expression'])

for complexity, r, expression in zip(pf['complexity'], pf['r'], pf['expression']):
    expr = expression

    expr = re.sub('[\[\]]', '', expr)
    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('log', 'np.log', expr)

    exec("def f_{0}(x1, x2): return {1}".format(complexity, expr))
    

plt.errorbar(data['x1'].where(data['x2']==x2), data['y'].where(data['x2']==x2), xerr=0.1, yerr=0.01, capsize=0.1)

plt.plot(x1, f_53(x1, x2))

plt.show()
