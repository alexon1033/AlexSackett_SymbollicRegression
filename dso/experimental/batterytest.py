import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

testfile = "data/BatteryTest.csv"
outputfile = "log/._data_BatteryData_2023-03-02-162116/dso_._data_BatteryData_0_pf.csv"

mse = []
comp = []

test = pd.read_csv(testfile, delimiter=',', header=0)
output = pd.read_csv(outputfile, delimiter=',', header=0)
output = output.sort_values('complexity')


for expression, complexity in zip(output['expression'],output['complexity']):
    expr = expression
    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('log', 'np.log', expr)
    expr = re.sub('\^', '**', expr)
    expr = re.sub('[\[\]]', '', expr)
    

    exec(f"def f(x1, x2, x3, x4, x5): return {expr}")
    error = test['Y'] - f(test['V'], test['I'], test['Temp'], test['V_avg'], test['I_avg'])

    se = error**2
    mean_squared_error = np.mean(se)
    
    pcterr = error/test['Y'] * 100

    pae = abs(error)
    pae = np.mean(pae)

    mean_squared_error = mean_squared_error
    pae = pae

    print(f" {expression}\n Complexity: {complexity}\n MSE on test set: {mean_squared_error}\n Mean abs pct Error: {pae}%\n----------\n")

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

plt.savefig('plots/Battery_pf.png')
print(min(mse))

