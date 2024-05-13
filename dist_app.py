import funciones as fc
import streamlit as st

t = st.container()

with t:
    st.header("Distribución Normal")
    st.write("$\large Parámetros:$ $\mu \in \R, \sigma > 0$")
    st.write("$\large Notación:$ $X$ ~ $N(\mu,\sigma ^2)$")
    media = st.number_input("Introduce la media", min_value=-10000.00, max_value=10000.00, value=0.00, step=1.00)
    sigma = st.number_input("Introduce la varianza", min_value=0.1, max_value=10000.00, value=1.00, step=1.00)
    st.write("Gráfica de la función de distribución")
    fc.normal(media,sigma)

    st.write(f"Si X es la varibale aleatoria tal que $X$ ~ $N({media},{sigma})$")
    st.write(f"$\large Esperanza:$ U+1D53xC $(X) = {media}$")
    st.write(f"$\large Varianza:$ $Var(X) = {sigma}$")

 
    
