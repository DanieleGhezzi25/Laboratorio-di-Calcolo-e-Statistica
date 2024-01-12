# plot sine and cosine with translation and dilatation

from matplotlib import pyplot as plt
import numpy as np

def f(x):
    A = 2
    return A*np.cos(x-np.pi/2)

def main():
    
    x_coord = np.linspace(0, 2*np.pi, 10000)
    y1_coord = np.cos(x_coord)
    y2_coord = np.sin(x_coord)
    y3_coord = f(x_coord)
    
    fig, ax = plt.subplots(nrows= 1, ncols=1)
    ax.plot(x_coord, y1_coord, label='y = cos(x)')
    # ax.plot(x_coord, y2_coord, label='y = sin(x)', color='r')
    ax.plot(x_coord, y3_coord, label='y = 2*cos(x-pi/2)', color='r')
    ax.set_title('Cosines')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    plt.show()
    
    return

if __name__ == '__main__':
    main()   