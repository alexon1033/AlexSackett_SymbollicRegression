import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

data = pd.read_csv("data/Coil.csv", delimiter=',', header=None, names=['x', 'y'])

pf = pd.read_csv("log/Coil.csv", delimiter=',', header=0, usecols=['Complexity', 'Equation'])

x = np.linspace(30,70,1000)

for complexity, expression in zip(pf['Complexity'], pf['Equation']):
    expr = expression

    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('log', 'np.log', expr)
    expr = re.sub('\^', '**', expr)

    #print(expr)

    exec(f"def f(x0): return {expr}")
    
    try:
        plt.plot(data['x'], data['y'], 'b.', label='Measured magentic field')
        plt.plot(x, f(x), 'r-', label=f'SR fit (complexity: {complexity})')
        #plt.legend()
        plt.xlabel('x / cm')
        plt.ylabel('B / mT')
        plt.savefig(f"plots/Coil_{complexity}.png")
        print(f"Saved plot with complexity: {complexity}")
        plt.clf()

    except:
        print("Dimension error")




