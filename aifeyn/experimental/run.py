from pysr import PySRRegressor
import sys

file = sys.argv[1]

data = pd.read_csv(f"data/{file}.csv", delimiter=',', names=['x','y'])


