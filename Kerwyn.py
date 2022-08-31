%matplotlib qt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


excel_data_path = "C:/Users/sebra/Documents/Kerwyn/3D_data.xlsx"

df = pd.read_excel(excel_data_path)

x = df['X']
y = df['Y']
z = df['Step']

# Creating figure
fig = plt.figure(figsize = (16, 9))
ax = plt.axes(projection ="3d")
   
# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.3,
        alpha = 0.2)
 
 
# Creating color map
my_cmap = plt.get_cmap('hsv')
 
# Creating plot
sctt = ax.scatter3D(x, y, z,
                    alpha = 0.8,
                    c = (x + y + z),
                    cmap = my_cmap,
                    marker ='^')
 
plt.title("Drunk Guy Walking")
ax.set_xlabel('X-axis', fontweight ='bold')
ax.set_ylabel('Y-axis', fontweight ='bold')
ax.set_zlabel('Step', fontweight ='bold')

ax.plot(x[:1], y[:1], z[:1], 'o-',c='black', label="first", zorder=10)
ax.plot(x[-1:], y[-1:], z[-1:], 'o-',c='grey', label="last", zorder=10)

fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)
 
# show plot
plt.show()
