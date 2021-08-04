import numpy as np
import unittest
from src.Curves.Curve import Curve
from src.StochasticProcesses.HullWhite import HullWhite


def test_b_function():
    tenors = np.array([0.00, 0.25, 0.50, 0.75, 1.00])
    discount_factors = np.array([1.000000000, 0.975309912, 0.951229425, 0.927743486, 0.904837418])
    curve = Curve(tenors=tenors, discount_factors=discount_factors)
    alpha = 0.1
    hw = HullWhite(alpha, 0.2, curve)
    actual = hw.b_function(0, 1)
    expected = (1/alpha)*(1 - np.exp(-1 * alpha))
    assert actual == expected
