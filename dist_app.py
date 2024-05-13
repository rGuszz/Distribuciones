import funciones as fc
import streamlit as st

t = st.container()

with t:
    st.header("Normal")
    media = st.number_input("Introduce la media", min_value=-10000.00, max_value=10000.00, value=0.00, step=1.00)
    sigma = st.number_input("Introduce la varianza", min_value=0.1, max_value=10000.00, value=1.00, step=1.00)
    st.write("Gráfica de la función de distribución")
    fc.normal(media,sigma)

    st.write(f"La esperanza de la normal es $E(X) = {media}$")
    st.write(f"La varianza de la normal es $Var(X) = {sigma}$")

 
    
