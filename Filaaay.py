

import pandas
dir(pandas)
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

wodf = pandas.read_excel("GISdata.xlsx",sheet_name ="cancercases")
wodf

cancercases = go.Bar(x=wodf["CancerType"], y=wodf["Number"],
                         marker = {"color": wodf["Number"],
                                   "colorscale" : "Jet"})

plot([cancercases])
    
titles = go.Layout(title = "Number of cancercases",
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="cases",
                        )
                    ),
                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",
                                                                )
                                                              )
                    )

fig =go.Figure(data=[cancercases], layout=titles)

plot(fig)
