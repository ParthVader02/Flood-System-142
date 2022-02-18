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