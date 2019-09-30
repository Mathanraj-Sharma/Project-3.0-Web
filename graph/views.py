from django.shortcuts import render, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from frontend.views import get_total_review_score

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

    
    # doughnut
    s, d = get_total_score_doughnut(1)

    context = {
        'script': script,
        'div': div, 
        'script2': s,
        'div2': d
    }

    return render(request, 'graph.html', context)


def get_total_score_doughnut(hotel_id):
    """
    this function will get hotel id as an input and return doughnut graph (script and div)
    for total score
    """
    score = get_total_review_score(hotel_id)
    x = {
        # pass the id of selected hotel here to get the doughnut graph
        'Score': score,
        'Rest' : (5-score)
    }

    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
    data['angle'] = data['value']/5 * 2*pi
    data['color'] = ['blue', 'white']

    p = figure(plot_height=350, title="Doughnut Chart", toolbar_location=None,
            tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

    p.annular_wedge(x=0, y=1,inner_radius = 0.2, outer_radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="black", fill_color='color', legend='country', source=data)

    p.axis.axis_label=None
    p.axis.visible=False
    p.grid.grid_line_color = None

    script,div = components(p)

    return [script,div]