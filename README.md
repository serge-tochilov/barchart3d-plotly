# 3D bar chart for Plotly

Currently the Plotly package doesn't have a 3D barcharts plotting function. There are some ideas how to implement it, see for example https://community.plotly.com/t/how-to-do-a-3d-bar-chart-if-possible/32287/2 and https://github.com/AymericFerreira/Plotly_barchart3D). The present repository suggests a function to draw good-looking and customizable 3d bar charts out of the box. Input data are two 1D arrays (labels + data points), and the data bars are fit to a given number of rows.

![Example chart](https://github.com/buran21/barchart3d-plotly/blob/master/barchart3d-pop-2007-top10.png?raw=true)

*def barchart3d(labels, z_data, title, z_title,
               n_row=0, width=900, height=900, thikness=0.7, colorscale='Viridis',
               \*\*kwargs):*
    Draws a 3D barchart
    **labels:** Array_like of bar labels
    **z_data:** Array_like of bar heights (data coords)
    **title:** Chart title
    **z_title:** Z-axis title
    **n_row:** Number of x-rows
    **idth:** Chart width (px)
    **height:** Chart height (px)
    **thikness:** Bar thikness (0; 1)
    **colorscale:** Barchart colorscale
    **\*\*kwargs:** Passed to Mesh3d()
    Returns: 3D barchart figure
