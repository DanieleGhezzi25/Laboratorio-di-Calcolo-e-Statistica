# Create a one-dimensional histogram filled with 5 values and save the histogram image to a png file

from matplotlib import pyplot as plt

def main():
    fig,ax = plt.subplots(nrows=1,ncols=1)
    sample = [2,3,3,2,1,2,3,2]
    ax.hist(sample, bins=3, color='red')
    plt.savefig('es3_1.png')
    return

if __name__ == "__main__":
  main ()