# My own easy charting library wrapping around matplotlib


"I want to create a grouped bar chart, using `region` as the series, `animal` as the x val, `amount` as the y val"



## CLI examples

```sh
# simple chart
$ grafte bar ./tests/fixtures/single-catg.csv


# save chart to file (in addition to displaying it)
$ grafte bar ./tests/fixtures/single-catg.csv -o /tmp/mychart.png


# grouped bar
$ grafte bar ./tests/fixtures/multi-catg.csv -x name -y amount -c season

# stacked bar
$ grafte bar ./tests/fixtures/multi-catg.csv -x name -y amount -g stacked


# line chart
$ grafte line ./tests/fixtures/single-cont.csv 

# scatter, colored series
$ grafte scatter ./tests/fixtures/multi-cont.csv -x age -y avg_score -c region  


# scatter, dot size defined
$ grafte scatter ./tests/fixtures/multi-cont.csv -x age -y avg_score --size population
```



## References and additional info

- The works of Nicolas P. Rougier
    - His excellent matplotlib tutorial: https://github.com/rougier/matplotlib-tutorial
    - His open access book: Scientific Visualization: Python + Matplotlib https://github.com/rougier/scientific-visualization-book
        + PDF https://hal.inria.fr/hal-03427242/document
    + His cheatsheets and handouts: https://matplotlib.org/cheatsheets/


## TODOS


### 2024-09-14

- sized Scatter plot should be Bubble chart? 
    - e.g. plotly convention: https://plotly.com/python/line-and-scatter/#bubble-scatter-plots
    - scatter plots don't have size param, but have optional symbol param

- [ ] DataObj should handle pd.DataFrame

- rethink api and common argument names 
    - (e.g. `Chart(data, x=xvar, y=yvar)` instead of `Chart(data, xvar, yvar)`)
    - `-g` for group styles?
    - `-f` for facet attribute?
More charts
- area chart
- horizontal bar chart
- histogram
- pie chart
    + donut chart
- cumulative line chart
- scatterplot with trendline
- slope chart https://altair-viz.github.io/gallery/slope_graph.html
- heatmap
- hexbins
- geomaps
    - heatmap
    - bubble plot
    - hexbin
    - regions
        - world countries
        - us states
        - us counties
        - custom shapefiles

- [ ] write script to generate documentation
- write tests for each chart type
    - [ ] test bar subtypes, e.g. stacked and grouped
- figure out API for passing in style info, e.g. legends, titles, font-faces, padding, etc
    - read up on automated legend to create legend for dotsize: https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html#automated-legend-creation
- [ ] by default derive axes labels from column headers
- Get common example datasets (i.e. iris)
    - census county/tract with population, demographics, and incomes

### 2024-09-12
- [x] write tests for CLI
- handle multi-series charts
    - [x] grouped bar chart
    - [x] stacked bar chart
    - [ ] stacked normalized bar chart
    - [x] multi-colored scatter plot
    - [ ] multi-line chart



----------



## Future thinking

- Create default stylesheets
- Rename to grufte? 
- change underlying library from matplotlib to [altair-vega](https://altair-viz.github.io, so that there's option to output vega 
- implement facet_grid type charts
- use altair-type data labeling, e.g. x='year:O' to indicate ordinal values
Bespoke labeling and highlights 

- e.g. https://altair-viz.github.io/gallery/scatter_with_labels.html
- line chart with labeled endpoints: https://altair-viz.github.io/gallery/line_with_last_value_labeled.html

- label single points of user's choosing
- colorize a single series of data
    - require user to have a bool column, and to specify highlight color, e.g.
        `--highlight column_name//green`

- allow for log scales
- mark y-value/rule: https://altair-viz.github.io/gallery/line_chart_with_datum.html

- geographic mapping/charting
    - matplotlib: https://matplotlib.org/basemap/stable/users/examples.html
    - rougier 


