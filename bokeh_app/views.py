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
        domain  = request.POST['domain'].split()
        eqn     = request.POST['equation']
        domain = range( int(domain[0]), int(domain[1]) )
        y = [ eval(eqn) for x in domain ]
        title = 'y = ' + eqn

        plot = figure(title= title , x_axis_label= 'X-Axis', y_axis_label= 'Y- Axis', plot_width =400, plot_height =400)
        plot.line(domain, y, legend= 'f(x)', line_width = 2)
        script, div = components(plot)

        return render_to_response( 'bokeh/index.html', {'script' : script , 'div' : div} )


    else:
        pass
