#Exercise 7: Plotly Box plots

import plotly.graph_objects as go
import numpy as np

y0 = np.random.randn(50)
y1 = np.random.randn(50) + 1  
y2 = np.random.randn(50) + 2  

fig = go.Figure()

fig.add_trace(go.Box(y=y0, name='Sample A'))
fig.add_trace(go.Box(y=y1, name='Sample B'))
fig.add_trace(go.Box(y=y2, name='Sample C'))


fig.show()
