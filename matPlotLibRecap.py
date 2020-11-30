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
print('SubPlots: ')
plt.subplot(3,2,1)
plt.plot(x,x)
plt.subplot(3,2,2)
plt.plot(x,y)
plt.subplot(3,2,3)
plt.plot(x,z)
plt.subplot(3,2,4)
plt.plot(y,z)
plt.subplot(3,2,5)
plt.subplot(3,2,6)
plt.plot(x,x)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.tight_layout()
print("----------------------------------")