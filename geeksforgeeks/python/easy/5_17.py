Plot Live Graphs using Python Dash and Plotly



 **Dash** is a Python framework built on top of ReactJS, Plotly and Flask. It
is used to create interactive web dashboards using just python. Live graphs
are particularly necessary for certain applications such as medical tests,
stock data, or basically for any kind of data that changes in a very short
amount of time where it is not viable to reload each time the data is updated.
This can be done using a feature called “hot reloading”, not to be confused
with “live reloading”. Live reloading reloads or refreshes the entire app when
the data is updated, while hot reloading only refreshes the data that was
updated without changing the state of the app. Dash automatically includes
hot-reloading making it the best choice for this kind of visualization.

Now, let’s build a dashboard that generates random data, appends it onto a
buffer at regular intervals and visualizes the same.

Install Dash module and Plotly modules.

    
    
    pip install dash
    pip install plotly
    

First, let’s import all the required modules and dependencies. Import _Output_
and _Input_ for callbacks, _dash_core_components_ for graphs and other basic
components offered by Dash. Import _dash_html_components_ offers basic HTML
components. Also, import _dash_ and _plotly_. Import the _graph_objs_ from
plotly for graph features. Import _deque_ (Doubly Ended Queue) from
_collections_.

    
    
    import dash
    from dash.dependencies import Output, Input
    import dash_core_components as dcc
    import dash_html_components as html
    import plotly
    import random
    import plotly.graph_objs as go
    from collections import deque

Let’s initialize two deques for X and Y components of the graph. Append single
data to it, this will be our first points on the graph.

  

  

    
    
    X = deque(maxlen = 20)
    X.append(1)
    
    Y = deque(maxlen = 20)
    Y.append(1)

Initialize the dash app.

    
    
    app = dash.Dash(__name__)

Now let’s specify the layout of the dashboard that we want to build. It is
important to note that there is no need to write HTML pages for the layout and
we can use dash’s HTML components to make simple layouts. Let’s build a simple
layout with just a graph component. In the code below, let’s set _animate_ to
True, this will easily handle scroll animations for the graph which would look
better than an abrupt change in the values after updating. Let’s assign an
_id_ to the graph component. We have another component named _Interval_ ,
which has properties like _id_ which specifies a unique ID for this component.
The property _interval_ specifies the time elapsed between two updations of
data. _n_interval_ refers to the number of intervals completed from the start
of the server.

    
    
    app.layout = html.Div(
        [    
            dcc.Graph(id = 'live-graph',
                      animate = True),
            dcc.Interval(
                id = 'graph-update',
                interval = 1000,
                n_intervals = 0
            ),
        ]
    )

Now let’s call the callback decorators

    
    
    @app.callback(
        Output('live-graph', 'figure'),
        [ Input('graph-update', 'n_intervals') ]
    )

Now let’s make the _update_graph_ method which takes in _n_intervals_ as
parameter. Let’s update X values sequentially, i.e., from 1 to 2 to 3 and so
on. Let’s update Y values to random values. Now let’s make a new _data_
variable and assign it to a plotly graph. Plotly graphs, by default, requires
you to set X and Y values with a list. Let’s specify the _mode_ to
_“lines+markers”_ which essentially means that Plotly is going to plot markers
first and then draw lines to it.

    
    
    def update_graph_scatter(n):
        X.append(X[-1]+1)
        Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
    
        data = plotly.graph_objs.Scatter(
                x=list(X),
                y=list(Y),
                name='Scatter',
                mode= 'lines+markers'
        )
    
        return {'data': [data],
                'layout' : go.Layout(xaxis=dict(
                        range=[min(X),max(X)]),yaxis = 
                        dict(range = [min(Y),max(Y)]),
                        )}

Finally, run the server.

    
    
    if __name__ == '__main__':
        app.run_server()

 **Complete Code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import dash

from dash.dependencies import Output, Input

import dash_core_components as dcc

import dash_html_components as html

import plotly

import random

import plotly.graph_objs as go

from collections import deque

 

X = deque(maxlen = 20)

X.append(1)

 

Y = deque(maxlen = 20)

Y.append(1)

 

app = dash.Dash(__name__)

 

app.layout = html.Div(

 [

 dcc.Graph(id = 'live-graph', animate = True),

 dcc.Interval(

 id = 'graph-update',

 interval = 1000,

 n_intervals = 0

 ),

 ]

)

 

@app.callback(

 Output('live-graph', 'figure'),

 [ Input('graph-update', 'n_intervals') ]

)

 

def update_graph_scatter(n):

 X.append(X[-1]+1)

 Y.append(Y[-1]+Y[-1] *
random.uniform(-0.1,0.1))

 

 data = plotly.graph_objs.Scatter(

 x=list(X),

 y=list(Y),

 name='Scatter',

 mode= 'lines+markers'

 )

 

 return {'data': [data],

 'layout' :
go.Layout(xaxis=dict(range=[min(X),max(X)]),yaxis =
dict(range = [min(Y),max(Y)]),)}

 

if __name__ == '__main__':

 app.run_server()  
  
---  
  
 __

 __

Open the browser and run the app on the local host and port 8050

    
    
    http://localhost:8050/

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200531123318/LiveGraphCropped.gif)

This is how dash can be used for live graph visualizations. In this article,
we have used it with random values generated by the computer. However, the
same can be done with data pulled from APIs or a database.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

