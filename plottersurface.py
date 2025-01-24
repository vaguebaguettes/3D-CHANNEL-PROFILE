from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

def plot_contour(filename):
    # Read the CSV file
    points = pd.read_csv(filename)

    # Extract x, y, z values
    x = points['x'].values
    y = points['y'].values
    z = points['z'].values

    # Create grid values first.
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    xi, yi = np.meshgrid(xi, yi)

    # Interpolate z values on grid
    zi = griddata((x, y), z, (xi, yi), method='cubic')

    # Create a new figure for the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the 3D contour plot
    ax.contour3D(xi, yi, zi, 50, cmap='viridis')

    # Label the axes
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    # Show the plot
    plt.show()

 # Replace with the actual path to your CSV file

