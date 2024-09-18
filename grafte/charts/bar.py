from grafte.charts.chart import Chart
from matplotlib.patches import Patch
import numpy as np


class Bar(Chart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chart_type = "bar"
        self.group_style = kwargs.get("group_style", "grouped")

    def render(self):
        if not self.data.is_multi_series:
            x = self.data.X
            y = self.data.Y
            self.ax.bar(x, y)
        else:
            if self.group_style == "grouped":
                # tk-todo: handle stacked chart
                # tk-todo: generalize charts so that it handles an option to custom sort x-axis
                # or should it be done at the chart/dataobj init level?
                xlabels = self.data.x_labels
                clabels = self.data.c_labels
                xpos = np.arange(len(xlabels))

                # tk-todo: let user specify group padding/margins
                bar_width = 0.8 / len(clabels)
                offset = np.linspace(
                    -bar_width * (len(clabels) - 1) / 2,
                    bar_width * (len(clabels) - 1) / 2,
                    len(clabels),
                )

                for i, clabel in enumerate(clabels):
                    yvals = []
                    for xv in xlabels:
                        yv = self.data.get_yval(x=xv, c=clabel, default=np.nan)
                        yvals.append(yv)
                    rects = self.ax.bar(
                        xpos + offset[i], yvals, bar_width, label=clabel
                    )
                    self.ax.bar_label(rects, padding=3)

                self.ax.set_xticks(xpos)
                self.ax.set_xticklabels(xlabels)
                # tk-todo: honor user legend options
                self.ax.legend(ncols=len(clabels))
                # tk-todo: user should be able to set y-padding
                self.ax.set_ylim(0, max(self.data.get_yvals()))

            elif self.group_style == "stacked":
                xlabels = self.data.x_labels
                clabels = self.data.c_labels
                xpos = np.arange(len(xlabels))

                rects_list = []

                stackpos = np.zeros(len(xlabels))
                for clabel in clabels:
                    yvals = []
                    for xv in xlabels:
                        yv = self.data.get_yval(x=xv, c=clabel, default=0)
                        yvals.append(yv)

                    rects = self.ax.bar(xlabels, yvals, bottom=stackpos, label=clabel)
                    rects_list.append(rects[0])
                    stackpos += yvals
                    self.ax.bar_label(rects, label_type="center")

                self.ax.set_xticks(xpos)
                self.ax.set_xticklabels(xlabels)
                # tk-todo: honor user legend options
                legend_handles = [
                    Patch(facecolor=rect.get_facecolor(), label=clabel)
                    for rect, clabel in zip(rects_list, clabels)
                ]

                # tk-todo: legend order by default follows stack order, let user customize
                legend_handles = legend_handles[::-1]

                self.ax.legend(handles=legend_handles)
                # tk-todo: user should be able to set y-padding
                self.ax.set_ylim(0, np.max(stackpos) * 1.1)
