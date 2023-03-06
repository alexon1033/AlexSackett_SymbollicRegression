import numpy as np
import pandas as pd
from pysr import PySRRegressor
import re

file = "data/BatteryData.csv"
testfile = "data/BatteryTest.csv"
outputfile = "log/BatteryRun.csv"

data = pd.read_csv(file, delimiter=',', header=0)

x = data.drop('SOC', axis=1)
x = x.to_numpy()

y = data['SOC'].to_numpy()

model = PySRRegressor(
        niterations=1000,
        binary_operators=["+", "-", "*", "/", "^"],
        unary_operators=["cos", "sin", "exp", "log"],
        loss="loss(x, y) = (x - y)^2",
        equation_file=outputfile,
        early_stop_condition=("stop_if(loss, complexity) = loss < 1e-12 && complexity < 10")
        )

#model.fit(x, y)

#print(model)

test = pd.read_csv(testfile, delimiter=',', header=0)
output = pd.read_csv(outputfile, delimiter=',', header=0)
print(test)

for expression in output['Equation']:
    expr = expression
    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('log', 'np.log', expr)
    expr = re.sub('\^', '**', expr)

    exec(f"def f(x0, x1, x2, x3, x4): return {expr}")

    error = test['Y'] - f(test['V'], test['I'], test['Temp'], test['V_avg'], test['I_avg'])

    se = error**2
    mse = np.mean(se)
    
    pcterr = error/test['Y'] * 100

    pae = abs(error)
    pae = np.mean(pae)

    mse = round(mse, 3)
    pae = round(pae, 3)

    print(f" {expression}\n MSE on test set: {mse}\n Mean abs pct Error: {pae}%\n----------\n")

