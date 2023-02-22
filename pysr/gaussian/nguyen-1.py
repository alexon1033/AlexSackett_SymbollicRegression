import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import re
import os

N = 50

N_test = 999

Ns = np.linspace(100,1000,9)
sds = np.linspace(0,1,11)

x_test = np.linspace(0.1,1,N_test)
y_test =  x_test**3 + x_test**2 + x_test

df = pd.DataFrame({"x" : x_test, "y" :  y_test})
df.to_csv("./data/Nguyen1_test.csv", index=False, header=False)

for i in range(len(Ns)):
    for j in range(len(sds)):
        x = np.random.random(int(Ns[i]))
        y = x**3 + x**2 + x
        
        noise = np.random.normal(0, sds[j], int(Ns[i]))
        y = y + noise

        df = pd.DataFrame({"x" : x, "y" : y})
        df.to_csv("./data/Nguyen1_N{0}_sd{1}.csv".format(int(Ns[i]), round(sds[j],1)), index=False, header=False)



