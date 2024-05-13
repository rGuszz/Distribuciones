import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objs as go
import scipy.stats as stats

def normal(media, sigma):
    eje_x = np.linspace(media-1000,media+1000,100000)
    pdf = (1/(np.sqrt(2*np.pi*sigma)))*(np.exp(-(((eje_x-media)**2/(2*sigma)))))
    graf = go.Line(x=eje_x,
                   y=pdf,
                   mode="lines",
                   line=dict(color="#71B3EA"),
                   legendgroup="Funcion",
                   showlegend=False,
                   name="Función de densidad")
    fig = go.Figure(data=graf)
    rueda = dict({"scrollZoom": True})
    fig.add_trace(go.Scatter(x=[-10000000000000,media-1000],
                             y=[0,0], mode="lines",
                             line=dict(color="#71B3EA"),
                             legendgroup="Funcion",
                             name="Función de densidad",
                             showlegend=False))
    fig.add_trace(go.Scatter(x=[media+1000,10000000000000],
                             y=[0,0], mode="lines",
                             line=dict(color="#71B3EA"),
                             legendgroup="Funcion",
                             name="Función de densidad",
                            showlegend=False))
    fig.update_layout(template=None, dragmode = "pan", autosize=False, width=500, height=350)
    if media == 0 and sigma == 1:
        fig.update_layout(xaxis=dict(zeroline=True, zerolinecolor='black'), yaxis=dict(zeroline=True, zerolinecolor='black'))
        fig.update_xaxes(range=[-4,4])
        return st.plotly_chart(fig, config=rueda, use_container_width=True)
    else: 
        fig.update_layout(xaxis=dict(zeroline=True, zerolinecolor='black'), yaxis=dict(zeroline=True, zerolinecolor='black'))
        fig.update_xaxes(range=[media-4,media+4])   
        return st.plotly_chart(fig, config=rueda, use_container_width=True)
    
def exponencial(lambdaa):
    x = np.linspace(0,2,1000)
    pdf = lambdaa*(np.exp(-lambdaa*x))
    plt.figure(figsize=(10,5))


