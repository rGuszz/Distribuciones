import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objs as go
import scipy.stats as stats

def normal(media, sigma, valor, color):
    eje_x = np.linspace(media-1000,media+1000,100000)
    eje_x_2 = np.linspace(media-1000,valor,100000)
    pdf = (1/(np.sqrt(2*np.pi*sigma)))*(np.exp(-(((eje_x-media)**2/(2*sigma)))))
    pdf_2 = (1/(np.sqrt(2*np.pi*sigma)))*(np.exp(-(((eje_x_2-media)**2/(2*sigma)))))
    graf = go.Line(x=eje_x,
                   y=pdf,
                   mode="lines",
                   line=dict(color=color),
                   legendgroup="Funcion",
                   showlegend=False,
                   name="Función de densidad")
    graf2 = go.Line(x=eje_x_2,
                   y=pdf_2,
                   mode="lines",
                   fill="tozeroy",
                   line=dict(color=color),
                   legendgroup="Funcion",
                   showlegend=False,
                   name="Función de densidad")
    fig = go.Figure(data=[graf, graf2])
    rueda = dict({"scrollZoom": True})
    fig.add_trace(go.Scatter(x=[-10000000000000,media-1000],
                             y=[0,0],
                             mode="lines",
                             line=dict(color=color),
                             legendgroup="Funcion",
                             name="Función de densidad",
                             showlegend=False))
    fig.add_trace(go.Scatter(x=[media+1000,10000000000000],
                             y=[0,0], mode="lines",
                             line=dict(color=color),
                             legendgroup="Funcion",
                             name="Función de densidad",
                             showlegend=False))
    fig.update_layout(template=None, dragmode = "pan")
    fig.update_layout(autosize=False,
                      width=800,
                      height=600)
    if media == 0 and sigma == 1:
        fig.update_layout(xaxis=dict(zeroline=True,
                                     zerolinecolor='black'),
                          yaxis=dict(zeroline=True,
                                     zerolinecolor='black'))
        fig.update_xaxes(range=[-4,4])
        return st.plotly_chart(fig, config=rueda)
    else: 
        fig.update_layout(xaxis=dict(zeroline=True,
                                     zerolinecolor='black'),
                          yaxis=dict(zeroline=True,
                                     zerolinecolor='black'))
        fig.update_xaxes(range=[media-4,media+4])  
        
     
        return st.plotly_chart(fig, config=rueda)
    
def exponencial(lambdaa, valor, color):
    x_exp = np.linspace(0.000001, 1000, 100000)
    x_exp_2 = np.linspace(0.000001, valor, 100000)
    y = lambdaa*np.exp(-lambdaa*x_exp)
    y_2 = lambdaa*np.exp(-lambdaa*x_exp_2)
    graf = go.Line(x=x_exp,
                   y=y,
                   mode="lines",
                   line=dict(color=color),
                   legendgroup="Funcion",
                   showlegend=False,
                   name="Función de densidad",
                   showlegend=False)
    graf_2 = go.Line(x=x_exp_2,
                   y=y_2,
                   mode="lines",
                   fill="tozeroy",
                   line=dict(color=color),
                   legendgroup="Funcion",
                   showlegend=False,
                   name="Función de densidad",
                   showlegend=False)
    fig = go.Figure(data=[graf,graf_2])
    fig.add_trace(go.Scatter(x=[1000,100000],
                             y=[0,0], mode="lines",
                             line=dict(color=color),
                             legendgroup="Funcion",
                             name="Función de densidad"),
                             showlegend=False)
    fig.update_layout(template=None, dragmode = "pan")
    fig.update_layout(autosize=False,
                      width=800,
                      height=600)
    rueda = dict({"scrollZoom": True})
    fig.update_layout(xaxis=dict(zeroline=True,
                                     zerolinecolor='black'),
                          yaxis=dict(zeroline=True,
                                     zerolinecolor='black'))
    v = stats.expon.ppf(0.99999, scale=1/lambdaa)
    fig.update_xaxes(range=[0,v])
    return st.plotly_chart(fig, config=rueda)


