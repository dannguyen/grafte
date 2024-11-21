from grafte.charts.chart import Chart


class Line(Chart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chart_type = "line"

    def render(self):
        if not self.data.is_multi_series:
            x = self.data.X
            y = self.data.Y
            self.ax.plot(x, y)
        else:
            pass
