from optparse import Values
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit


def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)

    plt.plot(dates, levels, '.')

    x1 = np.linspace(dates[0], dates[-1], 30)

    plt.plot(x1, poly(x1))
    plt.show()