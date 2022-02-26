
import numpy as np
import matplotlib


def polyfit(dates, levels, p):  
    if dates:
        x = matplotlib.dates.date2num(dates)
        p_coeff = np.polyfit(x-x[0], levels, p)
        poly = np.poly1d(p_coeff)
        d0 = x[0]
        return poly, d0
    else:
        return None