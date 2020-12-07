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
print('- - - - - - - - - - - - - - - - -')
print('Types of plots: ')
plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.hist(x,y)
plt.subplot(2,2,3)
plt.bar(x,y)
plt.subplot(2,2,4)
plt.fill(x,y)
plt.tight_layout()
print('- - - - - - - - - - - - - - - - -')
print('even a 360 graph:')
print()
plt.polar(x,y)
print()
print('All clear!')
print('- - - - - - - - - - - - - - - - -')
print('Legends:')
plt.plot(x,y,label = 'legend example')
plt.legend(loc = 1)
print('- - - - - - - - - - - - - - - - -')
print('Object oriented plots (for controlling the axes):')
print()
noneOOPlot = plt.plot(x,y)
print(noneOOPlot)
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
oOPlot = axes.plot(x,y)
print(oOPlot)
print("----------------------------------")