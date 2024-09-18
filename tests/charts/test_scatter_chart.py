import pytest
from grafte import Scatter


def test_basic_scatter_chart():
    data = [["al", 1], ["bob", 2]]
    cx = Scatter(data, canvas={"width": 200, "height": 100})

    assert cx.chart_type == "scatter"
    assert cx.canvas.width == 200
    assert cx.canvas.height == 100
