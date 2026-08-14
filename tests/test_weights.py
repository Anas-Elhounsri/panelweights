import pandas as pd

from panelweights import trim


def test_trim_bounds():
    out = trim(pd.Series([0.01, 1.0, 20.0]), 0.1, 10.0)
    assert list(out) == [0.1, 1.0, 10.0]
