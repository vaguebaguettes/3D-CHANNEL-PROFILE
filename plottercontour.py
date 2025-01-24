import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def plot(csv_file):
# Step 1: Read Data from CSV # Replace with your CSV file path
    data = pd.read_csv(csv_file)

    # Step 2: Process Data
    # Assuming the CSV file has columns 'x', 'y', and 'z'
    y = data['x'].values
    x = data['y'].values
    z = data['z'].values

    # Create grid data for contour plot
    X, Y = np.meshgrid(np.unique(x), np.unique(y))
    Z = z.reshape(len(np.unique(y)), len(np.unique(x)))

    # Step 3: Create a 3D Contour Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot contour
    ax.contour3D(X, Y, Z, 50, cmap=cm.viridis)

    # Add labels
    ax.set_xlabel('time(s)/X axis(um)')
    ax.set_ylabel('Y Axis (um)')
    ax.set_zlabel('Z Axis Temperature (C)')

    # Show plot
    plt.show()
