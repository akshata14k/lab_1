# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def mean(xs):
    if not xs: raise ValueError("empty")
    return sum(xs) / len(xs)

def median(xs):
    if not xs: raise ValueError("empty")
    ys = sorted(xs)
    n = len(ys)
    mid = n // 2
    return ys[mid] if n % 2 else (ys[mid-1] + ys[mid]) / 2

def variance(xs, ddof=0):
    """Population variance (ddof=0) or sample variance (ddof=1)."""
    if not xs or len(xs) - ddof <= 0: raise ValueError("insufficient data")
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - ddof)

def zscores(xs):
    """Return z-scores using population std (ddof=0)."""
    m = mean(xs)
    var = variance(xs, ddof=0)
    sd = var ** 0.5
    return [(x - m) / sd if sd else 0.0 for x in xs]
