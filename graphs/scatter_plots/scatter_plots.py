import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
                    x=random_x, 
                    y=random_y, 
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='rgb(0,0,153)',
                        symbol='pentagon',
                        line={'width':10}
                    ))]

layout = go.Layout(
    title='Scatter Plot', 
    xaxis={'title':'X Axis'}, 
    yaxis=dict(title='Y Axis'), 
    hovermode='closest'
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='./graphs/scatter_plots/scatter.html')
