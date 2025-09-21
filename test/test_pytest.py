from src.stats_tools import mean, median, variance, zscores

def test_mean(): assert mean([1,2,3,4]) == 2.5
def test_median():
    assert median([1,3,2]) == 2
    assert median([1,2,3,4]) == 2.5

def test_variance():
    assert variance([1,2,3,4], ddof=0) == 1.25   # population
    assert variance([1,2,3,4], ddof=1) == 1.6666666666666667  # sample

def test_zscores_len():
    zs = zscores([1,2,3])
    assert len(zs) == 3 and abs(sum(zs)) < 1e-9
