import pytest
from grafte import Bar
import grafte


def test_basic_bar_chart():
    data = [["al", 1], ["bob", 2]]
    cx = Bar(data, canvas={"width": 200, "height": 100})

    assert cx.chart_type == "bar"
    assert cx.canvas.width == 200
    assert cx.canvas.height == 100
    # even though there's no need for grouping, the default group style should be 'grouped'
    assert cx.data.is_multi_series == False
    assert cx.group_style == "grouped"


def test_verbose_api_call_for_bar():
    data = [["al", 1], ["bob", 2]]
    cx = grafte.Bar(data, canvas={"width": 200, "height": 100})
