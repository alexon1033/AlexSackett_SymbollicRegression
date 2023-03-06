import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

E = np.e

x = np.linspace(30,70,1000)

data = pd.read_csv("data/CoilExtra.csv", delimiter=',', header=None, usecols=[1,-1], names=['x','y'])

pf = pd.read_csv("log/._data_CoilExtra_2023-03-01-183840/dso_._data_CoilExtra_0_pf.csv", usecols=['complexity','r','expression'])

for complexity, r, expression in zip(pf['complexity'], pf['r'], pf['expression']):
    expr = expression

    expr = re.sub('[\[\]]', '', expr)
    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('log', 'np.log', expr)

    exec("def f(x1): return {1}".format(complexity, expr))
    
    plt.plot(data['x'], data['y'], 'b.')
    plt.plot(x, f(x), 'r-')
    plt.savefig(f"plots/coil_{complexity}.png")
    plt.clf()

    #except:
     #   print(f"Failed to plot complexity: {complexity}")
    


