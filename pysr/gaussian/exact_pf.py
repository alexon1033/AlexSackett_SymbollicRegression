import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import sys
import os
import seaborn as sns

E = 0

testp = 'data/Nguyen1_test.csv'
testf = pd.read_csv(testp, delimiter=',', header=0, names=['x','y'])

paths = []
 
for root, dirs, files in os.walk("./log"):
    for file in files:
        if file.endswith("test_0_pf.csv"):
            pass

        elif file.endswith(".csv"):
            paths.append(os.path.join(root, file))

paths = np.sort(paths)
paths = np.roll(paths, -11)


i=1
squares = []
for path in paths:
    print(path)
    df = pd.read_csv(path, delimiter=',', header=0, usecols=['Equation'])
    squaredtot = []
    print(i)
    i=i+1
    for expression in df['Equation']:
        expr = expression
        expr = re.sub(r'[\]\[]',r'', expr)
        expr = re.sub('\^', '**', expr)
        expr = re.sub('exp', 'np.exp', expr)
        expr = re.sub('cos', 'np.cos', expr)
        expr = re.sub('sin', 'np.sin', expr)
        expr = re.sub('log', 'np.log', expr)
        exec("def f(x0): return {0}".format(expr))
        

        squaredel = (f(testf['x']) - testf['y'])**2
        squaredtot.append(np.mean(squaredel))
        
    squaredav = np.min(squaredtot)
    squares.append(squaredav)

squares = np.array(squares)
error = squares.reshape((9,11))
error = np.round(error, 4)


sns.heatmap(error, annot=True, cbar_kws={'label': 'Best mean squared error of pareto frontier'})
plt.xticks(np.arange(0,11,1), np.round(np.linspace(0.0,1.0,11),1))
plt.yticks(np.arange(0,10,1), np.round(np.linspace(100,1000,10),0))
plt.xlabel('Standard deviation of absolute error')
plt.ylabel('Number of samples')
plt.show()
