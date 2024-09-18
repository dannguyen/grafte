import pytest

# from click.testing import CliRunner
from grafte.lib.data import DataObj


def test_unlabeled_dataobj():
    d = DataObj([["a", 1], ["b", 5]])
    assert d.xvar == 0
    assert d.yvar == 1
    assert d.cvar == None
    assert d.is_multi_series is False


def test_specific_dataobj():
    d = DataObj(
        [
            {"id": "a", "amt": 6},
            {"id": "b", "amt": 7},
        ],
        xvar="id",
        yvar="amt",
    )

    assert d.xvar == "id"
    assert d.yvar == "amt"
    assert d.cvar == None
    assert d.X == ["a", "b"]
    assert d.Y == [6, 7]
    assert d.is_multi_series is False


def test_multiseries_dataobj():
    d = DataObj(
        [
            {"id": "a", "amt": 2, "region": "SE"},
            {"id": "a", "amt": 6, "region": "NW"},
            {"id": "b", "amt": 7, "region": "NW"},
            {"id": "b", "amt": 5, "region": "SE"},
        ],
        xvar="id",
        yvar="amt",
        cvar="region",
    )

    assert d.xvar == "id"
    assert d.yvar == "amt"
    assert d.cvar == "region"
    assert d.X == ["a", "a", "b", "b"]
    assert d.Y == [2, 6, 7, 5]
    assert d.C == [
        "SE",
        "NW",
        "NW",
        "SE",
    ]
    assert d.c_labels == [
        "SE",
        "NW",
    ], "c_labels is supposed to preserve order of series as they appeared in original data"
    assert d.is_multi_series is True


def test_yval_filtering():
    d = DataObj(
        [
            {"id": "a", "amt": 2, "region": "SE"},
            {"id": "a", "amt": 6, "region": "NW"},
            {"id": "b", "amt": 7, "region": "NW"},
            {"id": "b", "amt": 5, "region": "SE"},
        ],
        xvar="id",
        yvar="amt",
        cvar="region",
    )

    assert d.get_yvals(x="a") == [2, 6]
    assert d.get_yvals(c="NW") == [6, 7]
    assert d.get_yvals(x="a", c="NW") == [6]
    assert d.get_yval(x="a", c="NW") is 6

    assert d.get_yval(x="wrong") is None
    assert d.get_yval(x="wrong", default=42) is 42


def test_dataobj_to_dict():
    dob = DataObj([["a", 1], ["b", 5]])
    dx = dob.to_list()

    assert type(dx) is list, "DataObj.to_list should be a plain list"
    assert all(
        type(d) is dict for d in dx
    ), "Each member of DataObj.to_list should be a plain dict"


@pytest.mark.skip
def test_dataobj_on_pd_dataframe():
    """
    should easily read a pandas dataframe
    """
    import pandas as pd

    df = pd.read_csv("/tmp/test.csv")
    dob = DataObj(df)
    assert dob.xvar == "customer"
