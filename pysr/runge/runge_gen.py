import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return 1/(1 + x**2)

xs = np.linspace(-5, 5, 10)

ys = f(xs)

df = pd.DataFrame({'x':xs, 'y':ys})

df.to_csv("runge.csv", sep=',')
