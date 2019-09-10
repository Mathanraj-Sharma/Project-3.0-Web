from django.shortcuts import render, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

from math import pi
import pandas as pd
from bokeh.palettes import Category20c
from bokeh.transform import cumsum

# Create your views here.
def graph(request):

    #Graph Coordinates
    X = [1,2,3,4,5]
    Y = [1,2,3,4,5]

    #Graph plot to display graph
    plot = figure(title = 'Line Graph', x_axis_label= 'X-Axis', y_axis_label= 'Y-axis', plot_width = 400, plot_height= 400)

    #plot line
    plot.line(X, Y, line_width= 2)

    #store graph Components
    script, div = components(plot)

    x = {
        'United States': 157,
        'United Kingdom': 93,
        'Japan': 89,
        'China': 63,
        'Germany': 44,
        'India': 42,
        'Italy': 40,
        'Australia': 35,
        'Brazil': 32,
        'France': 31,
        'Taiwan': 31,
        'Spain': 29
    }

    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
            tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend='country', source=data)

    p.axis.axis_label=None
    p.axis.visible=False
    p.grid.grid_line_color = None

    s, d = components(p)

    context = {
        'script': script,
        'div': div, 
        'script2': s,
        'div2': d
    }

    return render(request, 'graph.html', context)