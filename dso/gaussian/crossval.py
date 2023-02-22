import numpy as np
import pandas as pd
import re
import os
import time
E = 0 

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()



def pythonize(expr): 
    expr = re.sub(r'[\]\[]',r'', expr)
    expr = re.sub('exp', 'np.exp', expr)
    expr = re.sub('cos', 'np.cos', expr)
    expr = re.sub('sin', 'np.sin', expr)
    expr = re.sub('log', 'np.log', expr)
    return expr

x = np.linspace(1,10,1000)
paths = [] 

for root, dirs, files in os.walk("./log"):
    for file in files:
        if file.endswith("test_0_pf.csv"):
            pass

        elif file.endswith("pf.csv"):
            paths.append(os.path.join(root, file))

paths = np.sort(paths)
paths = np.roll(paths, -11)

printProgressBar(0, len(paths), prefix='Progress:', suffix='Complete', length=50)
results = pd.DataFrame(columns=['expression', 'numerical matches'])
i=0
for path in paths:
    df = pd.read_csv(path, delimiter=',', header=0, usecols=['expression'])
    for expression in df['expression']:
        expr = pythonize(expression)
        exec("def f(x1): return {0}".format(expr))
        numerical = 0
        exact = 0

        for nextpath in paths:
            df2 = pd.read_csv(path, delimiter=',', header=0, usecols=['expression'])
            for expression2 in df2['expression']:
                expr = pythonize(expression2)
                exec("def g(x1): return {0}".format(expr))

                square = (f(x) - g(x))**2
                mse = np.mean(square)
                
                if mse < 1e-9:
                    numerical = numerical + 1

                if expression == expression2:
                    exact = exact + 1
        
        result = pd.DataFrame({'expression': [expression], 'numerical matches': [numerical], 'exact matches': [exact]})
        results = pd.concat([result, results])

    i=i+1
    printProgressBar(i + 1, len(paths), prefix = 'Progress:', suffix = 'Complete', length = 50)


results.sort_values('exact matches')
results.to_csv('exact_count.csv')
results.sort_values('numerical matches')
results.to_csv('numerical_count.csv')



