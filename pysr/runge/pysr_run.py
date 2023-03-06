import numpy as np 
import pandas as pd
from pysr import PySRRegressor
import sys

file = "runge"

data = pd.read_csv(f"{file}.csv", delimiter=',', usecols=['x','y'])

x = data['x'].to_numpy().reshape(-1,1)
y = data['y'].to_numpy()

model = PySRRegressor(
        niterations=1000,
        binary_operators=["+","-","*","/","^"],
        unary_operators=["cos","sin","exp","log"],
        loss="loss(x ,y) = (x - y)^2",
        equation_file=f"log/{file}.csv",
        early_stop_condition=("stop_if(loss, complexity) = loss < 1e-12 && complexity < 10")
        )

model.fit(x, y)

print(model)
