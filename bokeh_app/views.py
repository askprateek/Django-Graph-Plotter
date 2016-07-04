from django.shortcuts import render, render_to_response
from bokeh.plotting import figure, output_file, show
from bokeh.resources import CDN
from bokeh.embed import components
import math
# Create your views here.

def index(request):
    if request.method == "GET" :
        return render_to_response('bokeh/index.html')

    elif request.method == "POST" :
        domain  = int(request.POST['domain'])
        eqn     = request.POST['equation']
        x = range(domain)
        y = [ eval(eqn) for a in x ]
        #output_file("bokeh_plot.html")
        title = 'y = ' + eqn
        plot = figure(title= title , x_axis_label= 'x', y_axis_label= 'y', plot_width =400, plot_height =400)
        plot.line(x, y, legend= 'f(x)', line_width = 2)

        script, div = components(plot)

        return render_to_response( 'bokeh/index.html', {'script' : script , 'div' : div} )


    else:
        pass
