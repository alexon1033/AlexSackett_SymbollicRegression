import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("runge.csv", delimiter=',', header=0, usecols=['x','y'])


for i in range(1,50):
    n = i*2
    poly = np.poly1d(np.polyfit(data['x'], data['y'], i*2))

    xs = np.linspace(-5, 5, 1000)

    plt.plot(data['x'], data['y'], 'b.')
    plt.plot(xs, poly(xs), 'r-')
    plt.savefig(f"plots/poly_{n}.png")
    plt.clf()
