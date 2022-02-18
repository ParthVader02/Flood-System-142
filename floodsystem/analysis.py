
import numpy as np
import matplotlib


def polyfit(dates, levels, p):  
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x, levels, p)
    poly = np.poly1d(p_coeff)
    d0 = x[0]
    return poly, d0
