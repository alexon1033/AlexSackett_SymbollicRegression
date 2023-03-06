import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

data = pd.read_csv("data/Coil.csv", delimiter=',', header=None, names=['x', 'y'])

pf = pd.read_csv("log/Coil.csv", delimiter=',', header=0, usecols=['Complexity', 'Equation'])

x = np.linspace(30,70,1000)

comp = []
mse = []

for complexity, expression in zip(pf['Complexity'], pf['Equation']):
    expr = expression

    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('log', 'np.log', expr)
    expr = re.sub('\^', '**', expr)

    #print(expr)

    exec(f"def f(x0): return {expr}")
    
    
    fitted_points = f(data['x'])
    error = (data['y'] - fitted_points)**2
    mean_squared_error = np.mean(error)
    mse.append(mean_squared_error)
    comp.append(complexity)

df_mse = pd.DataFrame(mse)
mse_pct_diff = df_mse.pct_change()
mse_pct_diff = mse_pct_diff.multiply(-1)

fig, ax = plt.subplots(2, 1, sharex='col')
ax[0].plot(comp, mse, 'k-', label='Mean squared error against compelxity')
ax[0].set_ylabel('Mean sqared error')
ax[1].plot(comp, mse_pct_diff[0], 'b-', label='Percentage drop of mean squared error')
ax[1].set_ylabel('Percentage change')
ax[1].set_xlabel('Complexity')

plt.savefig('plots/Coil_pf.png')
print(mse)


