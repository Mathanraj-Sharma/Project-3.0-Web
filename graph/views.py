from django.shortcuts import render, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from frontend.views import get_total_review_score
from reviews.models import review
from math import pi
import pandas as pd
import ast
from bokeh.palettes import viridis
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

    s_p, d_p = get_question_pie(1, "How good was the outside environment of the restaurant?")

    context = {
        'script': script,
        'div': div, 
        'script2': s,
        'div2': d,
        'script_p': s_p,
        'div_p': d_p
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

    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'scoring'})
    data['angle'] = data['value']/5 * 2*pi
    data['color'] = ['blue', 'white']

    p = figure(plot_height=250, plot_width = 375, title="Overall Score", toolbar_location=None,
            tools="hover", tooltips="@scoring: @value", x_range=(-0.5, 1.0))

    p.annular_wedge(x=0, y=1,inner_radius = 0.2, outer_radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="black", fill_color='color', legend='scoring', source=data)

    p.axis.axis_label=None
    p.axis.visible=False
    p.grid.grid_line_color = None

    script,div = components(p)

    return [script,div]


def get_question_answers(hotel_id, question):
    """
    this function will get a hotel id and question as input and return the list of answers
    for that question in all reviews for that hotel
    """
    reviews  = review.objects.filter(hotel = hotel_id).values('qa')
    answers = []
    for rev in reviews:
        rev_list = ast.literal_eval(rev['qa'])
        for dic in rev_list:
            if dic['question'] == question:
               answers.append(dic["answer"])

    return answers

def get_question_pie(hotel_id, question):
    """
    this function gets hotel_id and question as input and returns pie chart for that questions
    answers for that hotel
    """
    
    x = dict(pd.DataFrame({'col1': get_question_answers(hotel_id,question)}).col1.value_counts())
    # print(x)
    
    data = pd.Series(x).reset_index(name='value').rename(columns={'index':'answer'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = viridis(len(x))

    p = figure(plot_height=250, plot_width = 375, title= question, toolbar_location=None,
            tools="hover", tooltips="@answer: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1,radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="black", fill_color='color', legend='answer', source=data)

    p.axis.axis_label=None
    p.axis.visible=False
    p.grid.grid_line_color = None

    script,div = components(p)

    return [script,div]

