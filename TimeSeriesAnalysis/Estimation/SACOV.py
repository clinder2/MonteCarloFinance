import numpy as np
import pandas as pd

def SampleAC(series, h):
    series = pd.Series(series)
    mean = series.mean()
    n = 0
    for i in range(0, len(series)-h):
        n = n + (series[i+h] - mean)*(series[i] - mean)
    n /= len(series)
    return n