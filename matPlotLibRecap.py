import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("Matplotlib recap")
print("==================================")
print('First we need a graph (--> Jupyter):')
x = np.linspace(0,10,20)
y = x * x
z = x + y
myGraph = plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('justSomeTitle')
print(myGraph)
print('- - - - - - - - - - - - - - - - -')
print("----------------------------------")