import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

x = np.linspace(30,70,1000)

data = pd.read_csv('data/Coil.csv', delimiter=',', header=None, names=['x', 'y'])

pf = pd.read_csv('results/solution_temp.csv', delimiter=' ', header=None, names=['logerr', 'logcum','err', 'complexity' , 'squamous', 'expression'])

for complexity, expression in zip(pf['complexity'], pf['expression']):
    expr = expression

    expr = re.sub('asin', 'np.arcs', expr)
    expr = re.sub('acos', 'np.arcc', expr)
    expr = re.sub('atan', 'np.arct', expr)
    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('tan', 'np.tan', expr)
    expr = re.sub('exp', 'np.exp' , expr)
    expr = re.sub('log', 'np.log', expr)
    expr = re.sub('\^', '**', expr)
    expr = re.sub('np.arcs', 'np.arcsin', expr)
    expr = re.sub('np.arcc', 'np.arccos', expr)
    expr = re.sub('np.arct', 'np.arctan', expr)
    expr = re.sub('pi', 'np.pi', expr)
    expr = re.sub('sqrt', 'np.sqrt', expr)

    exec(f"def f(x0): return {expr}")

    try:
        plt.plot(data['x'], data['y'], 'b.')
        plt.plot(x, f(x), 'r-')
        plt.savefig(f'plots/coil_{complexity}.png')
        print(f"Saving under: plots/coil_{complexity}.png")
        plt.clf()
    except ValueError:
        print('ValErr')

