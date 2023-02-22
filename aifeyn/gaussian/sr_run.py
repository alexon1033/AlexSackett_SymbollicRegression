import numpy as np 
import pandas as pd
import aifeynman as aif
import sys

file = sys.argv[1]

data = pd.read_csv(f"data/{file}.csv", delimiter=',', names=['x','y'])

x = data['x'].to_numpy().reshape(-1,1)
y = data['y'].to_numpy()

aif.run_aifeynman("./data/", f"{file}.csv", 60, "14ops.txt")
