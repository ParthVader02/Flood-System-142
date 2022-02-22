from optparse import Values
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import matplotlib
import numpy as np
from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels
def plot_water_levels(station, dates, levels):
    "plots time series of level data"
    
   

    

    # Plots available level data
    
    plt.plot(dates, levels)
    # checks if historic level data is available
    if not levels:
        # if not, ignores and prints a warning
        print("Past Level Data Unavailable")
    else:
        # if available, plots lines of maximum/minimum levels
        plt.plot(dates, [max(levels)]*len(dates))
        plt.plot(dates, [min(levels)]*len(dates))
        
    # set up plot nicely
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()  
    # plot
    plt.show()







def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(x, levels, p)

    plt.plot(x, levels, '.')

    x1 = np.linspace(x[0], x[-1], 30)

    plt.plot(x1, poly(x1))
    plt.show()
