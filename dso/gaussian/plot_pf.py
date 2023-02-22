import numpy as np 
import pandas as pd
import os
import sys
import re
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap

x = np.linspace(0.1,1,999) 

testf = 'data/Nguyen1_test.csv'
test = pd.read_csv(testf, delimiter=',', header=0, names=['x','y'])

name = sys.argv[1]

pf = pd.read_csv(name, delimiter=',', header=0, usecols=['complexity','expression'])

N = pf.shape[0]
colors = plt.cm.viridis(np.linspace(0,1,N))

for i, expression, complexity in zip(pf.index, pf['expression'], pf['complexity']):
    expr = expression
    expr = re.sub('[\[\]]','', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('log', 'np.log', expr)
    exec("def f(x1): return {0}".format(expr))

    plt.plot(test['x'],f(test['x']), color=colors[i], label=complexity)


plt.plot(test['x'],test['y'], 'r', label='True') 
plt.legend()
plt.show()


