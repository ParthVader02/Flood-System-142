<<<<<<< HEAD
def plot_water_levels(station, dates, levels):
    
=======
from optparse import Values
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import matplotlib
import numpy as np

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(x, levels, p)

    plt.plot(x, levels, '.')

    x1 = np.linspace(x[0], x[-1], 30)

    plt.plot(x1, poly(x1))
    plt.show()
>>>>>>> 15ad3a2d01fe97ba0f0134980be2d6e943f37f1b
