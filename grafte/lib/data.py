from collections import namedtuple
from typing import Union, List, Dict, Optional, Iterable


DatumTuple = namedtuple("Datum", ["x", "y", "c", "size"])


class Datum(DatumTuple):
    def as_dict(self):
        return self._asdict()

    def to_dict(self):
        return self.as_dict()

    # Implement dict-like methods
    def keys(self):
        return self._fields

    def values(self):
        return tuple(getattr(self, field) for field in self._fields)

    def items(self):
        return self._asdict().items()


class DataObj:
    def __init__(
        self,
        data: Iterable[Union[list, dict, tuple]],
        xvar: Optional[str] = None,
        yvar: Optional[str] = None,
        cvar: Optional[str] = None,
        sizevar: Optional[str] = None,
    ):

        self.rawdata = data
        self.xvar = xvar or 0
        self.yvar = yvar or 1
        self.cvar = cvar
        self.sizevar = sizevar

    def to_list(self) -> List[dict]:
        return [d.to_dict() for d in self.data]

    @property
    def data(self) -> List[Datum]:
        raw = self.rawdata
        dx = []
        if type(raw) in (list, tuple):
            # simplest object: [(1, 2), (2, 5), (3, 4.2)]
            _x = self.xvar or 0
            _y = self.yvar or 1
            _c = self.cvar
            _s = self.sizevar

            for d in raw:
                o = Datum(
                    x=d[_x],
                    y=d[_y],
                    c=d[_c] if self.cvar else None,
                    size=d[_s] if self.sizevar else None,
                )
                dx.append(o)
        else:
            pass
        return dx

    @property
    def X(self) -> list:
        return [d.x for d in self.data]

    def Xc(self, c) -> list:
        return [d.x for d in self.data if d.c == c]

    @property
    def x_labels(self) -> list:
        """
        effectively a list of all categorical variables,
        which is necessary when making multiseries charts
        """
        return list(dict.fromkeys(self.X))

    @property
    def Y(self) -> list:
        return [d.y for d in self.data]

    def get_yvals(self, x=None, c=None) -> list:
        yvals = [
            d.y
            for d in self.data
            if (x is None or d.x == x) and (c is None or d.c == c)
        ]
        return yvals

    def get_yval(self, x=None, c=None, default=None):
        yvals = self.get_yvals(x, c)
        return yvals[0] if yvals else default

    @property
    def C(self) -> list:
        return [d.c for d in self.data]

    @property
    def c_labels(self) -> list:
        return list(dict.fromkeys(self.C))
        # return list(set(self.C))

    @property
    def is_multi_series(self) -> bool:
        return len(self.c_labels) > 1

    @property
    def Size(self) -> list:
        return [d.size for d in self.data]
