import pytest
from grafte.charts.chart import Chart
from grafte.lib.data import DataObj


def test_basic_chart():
    data = [["al", 1], ["bob", 2]]
    cx = Chart(data, canvas={"width": 200, "height": 100})

    # tk-todo: this should be an abstract class, actually...
    assert cx.chart_type == "default"
    assert cx.canvas.width == 200
    assert cx.canvas.height == 100


@pytest.mark.skip("not implemented yet")
def test_chart_data_accessors():
    data = [["al", 1], ["bob", 2]]
    cx = Chart(data, canvas={"width": 200, "height": 100})

    assert (
        type(cx.data) is not DataObj
    ), "Chart should not give direct access to underlying data object, or should it?"

    assert (
        type(cx.data.to_dict) is dict
    ), "allow easy access to transformed and re-labeled data as plain dict"

    assert (
        type(cx.rawdata.to_dict) is dict
    ), "allow easy access to data with its original labels and unused columns"
