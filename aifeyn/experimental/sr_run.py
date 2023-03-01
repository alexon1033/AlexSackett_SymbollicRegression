import numpy as np 
import pandas as pd
import aifeynman as aif
import sys

file = sys.argv[1]

#data = pd.read_csv(f"data/{file}.csv", delimiter=',', names)

data = np.genfromtxt(f"data/{file}.csv", delimiter=',')

#x = data['x'].to_numpy()
#y = data['y'].to_numpy()
#data = np.stack((x,y), axis=-1)
np.savetxt('./data/temp.csv', data)


aif.run_aifeynman("./data/", "temp.csv", 60, "14ops.txt")
