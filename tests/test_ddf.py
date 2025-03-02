import numpy as np
from ddf import DDFOptimizer

def test_ddf():
    X = np.array([[3, 3, 3]])
    Y = np.array([[4, 2, 5]])
    B = np.array([[1, 2, 1]])

    ddf = DDFOptimizer(X, Y, B)
    results = ddf.solve_all()

    assert isinstance(results, dict)
    assert "DMU1" in results
    assert results["DMU1"]["success"] is True
