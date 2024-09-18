from grafte.charts.chart import Chart

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from typing import List, Optional
import matplotlib.patches as mpatches


def map_cvals_to_colors(cvalues: List) -> (List, List[mpatches.Patch]):
    # tk-todo: colorization should be customizable across all chart types
    # tk-todo: respect the ordering of values when mapping to colors
    if not cvalues:
        return None

    uvals = list(set(cvalues))
    umap = {v: i for i, v in enumerate(uvals)}

    cnums = [umap[v] for v in cvalues]
    # tk-todo: let user specify colormap
    colormap = plt.get_cmap("viridis")
    normed = mcolors.Normalize(vmin=min(cnums), vmax=max(cnums))

    colors = colormap(normed(cnums))

    # tk-todo: legend should be ordered alphabetically
    legend_patches = [
        mpatches.Patch(color=colormap(normed(umap[clabel])), label=clabel)
        for clabel in uvals
    ]

    return colors, legend_patches


class Scatter(Chart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chart_type = "scatter"

    def render(self):
        x = self.data.X
        y = self.data.Y
        s = self.data.Size if self.data.sizevar else None
        c = self.data.C

        if self.data.cvar:
            colors, legend_patches = map_cvals_to_colors(c)
        else:
            colors, legend_patches = None

        self.ax.scatter(x, y, c=colors, label=colors, s=s)

        if colors is not None:
            plt.legend(handles=legend_patches)
