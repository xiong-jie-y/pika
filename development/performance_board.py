import streamlit as st

def draw_performance(filename):
    st.write(filename)
    import json
    performance = json.load(open(filename, "r"))

    import plotly.graph_objects as go
    import numpy as np

    fig = go.Figure()
    for key, times in performance.items():
        fig.add_trace(go.Box(y=times, name=key))

    st.write(fig)

# draw_performance("multiprocess_performance.json")
# draw_performance("singleprocess_performance.json")
draw_performance("general_performance.json")