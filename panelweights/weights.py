import pandas as pd


def design_weights(frame, strata="strata", clusters="cluster"):
    counts = frame.groupby(strata)[clusters].transform("nunique")
    return 1.0 / counts


def trim(weights, lower=0.1, upper=10.0):
    return pd.Series(weights).clip(lower, upper)
