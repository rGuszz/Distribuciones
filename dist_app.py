import funciones as fc
import streamlit as st

t = st.container()

with t:
    st.header("Normal")
    media = st.number_input("Introduce la media", min_value=-10000.00, max_value=10000.00, value=0.00, step=0.01)
    sigma = st.number_input("Introduce la varianza", min_value=0.1, max_value=10000.00, value=1.00, step=0.01)
    fc.normal(media,sigma)
    