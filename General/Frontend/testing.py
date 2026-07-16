import plotly.graph_objects as go
import plotly.io

fig = dict({
    "layout": {
        "title":{"text":"Beispiel"
                 }
        }
    "data": [{
        "type":"bar",
        "x":[1,2,3]
        "y":[[42,1337,807]]
    }
    ]
})
pio.show(fig)