from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas
def plot(filename):
    points = pandas.read_csv(filename)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = points['x'].values
    y = points['y'].values
    z = points['z'].values

    #  x   y   z  
    # 1.1,1.2,1.3
    # 2.1,2.2,2.3
    # 3.1,3.2,3.3
    # 4.1,4.2,4.3

    ax.scatter(x, y, z, c='r', marker='o')

    plt.show()

