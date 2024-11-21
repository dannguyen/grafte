import matplotlib.pyplot as plt

import numpy as np
from grafte.lib.data import DataObj
from grafte.lib.canvas import CanvasConfig
from typing import Union, List, Dict, Iterable, Optional


class Chart:
    def __init__(
        self,
        data: Iterable,
        canvas: Optional[Union[CanvasConfig, dict]] = None,
        **kwargs
    ):
        self.chart_type = "default"

        self.data = DataObj(
            data,
            xvar=kwargs.get("xvar"),
            yvar=kwargs.get("yvar"),
            cvar=kwargs.get("cvar"),
            sizevar=kwargs.get("sizevar"),
        )
        self.canvas = CanvasConfig(canvas)
        self.figure, self.ax = self._setup_canvas()

    def _setup_canvas(self):
        # Set up the canvas based on provided properties
        fig = self.canvas.config_matplotlib_figure(plt)
        ax = fig.add_subplot(111)

        return fig, ax

    def draw(self):
        plt.show()

    def render(self):
        pass

    def show(self):
        self.render()
        self.draw()

    def save(self, filepath):
        """Save the chart to a file."""
        self.figure.savefig(filepath)

    def get_figure(self):
        """Return the figure object, allowing external access."""
        return self.figure

    def get_axes(self):
        """Return the axes object, allowing external access."""
        return self.ax
