import pytest
from grafte import Line


def test_basic_line_chart():
    data = [["al", 1], ["bob", 2]]
    cx = Line(data, canvas={"width": 200, "height": 100})

    assert cx.chart_type == "line"
    assert cx.canvas.width == 200
    assert cx.canvas.height == 100
