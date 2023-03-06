import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

ref = pd.read_csv('../data/Coil.csv', delimiter=',', names=['x','y'])

data = pd.read_csv('CoilManyRuns.csv', names=['expression'])

for expression in data['expression']:
    expr = expression
    expr = re.sub('sin', 'np.sin', expr) 
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('tan', 'np.tan', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('\^', '**', expr)

    exec(f"def f(x0): return {expr}")

    plt.plot(ref['x'], ref['y'])
    plt.plot(ref['x'], f(ref['x']), 'r-')

    error = ref['y'] - f(ref['x'])
    se = error**2
    mse = np.mean(se)

    print(f"{expression},\n MSE: {mse}")

    plt.show()

