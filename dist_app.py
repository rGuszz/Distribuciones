import funciones as fc
import streamlit as st
import scipy.stats as stats

st.set_page_config(layout='wide')

titulo = st.container()
colu = st.container()
col1, col2 = st.columns(2)

with titulo:
    st.header("Distribuciones de probabilidad")
    distribu = st.selectbox("Selecciona la distribucion de tu elección",
                            options=["Normal", "Exponencial"])
    st.subheader(distribu)
    
with colu:    
    with col2:
        if distribu == "Normal":
            st.latex("\Large Parámetros")
            media = st.number_input("Introduce la media",
                                    value=0.00,
                                    step=0.01)
            sigma = st.number_input("Introduce la varianza",
                                    value=1.00,
                                    step=0.01)
            valor = st.number_input("Introduce el valor para calcular la función de distribución",
                                    value=0.00000,
                                    step=0.10000,
                                    format="%f")
            cdf = stats.norm.cdf(valor, loc=media, scale=sigma)
            st.latex(fr"X \sim N({media},{sigma})")
            st.latex(r'''
                     \large{f_X(x) = \frac{1}{\sqrt{2 \pi \sigma ^2}} \Large{e^{\frac{(x-\mu)^2}{2 \sigma ^2}}}}
                     ''')
            st.latex(fr'''
                    E(X) = {media}
                    ''')
            st.latex(fr'''
                    Var(X) = {sigma}
                    ''')
            st.latex(fr'''
                    F_X({valor}) = P(X \leq {valor}) = {cdf}
                    ''')
        elif distribu == "Exponencial":
            st.latex("\Large Parámetros")
            lambdaa = st.number_input("Introduce el parametro lambda",
                                    value=0.5,
                                    step=0.01)
            valor_exp = st.number_input("Introduce el valor para calcular la función de distribución",
                                    value=5.00000,
                                    step=0.10000,
                                    format="%f")
            cdf = stats.expon.cdf(valor_exp)
            st.latex(fr"X \sim exp({lambdaa})")
            st.latex(r'''
                     \large{f_X(x) = \lambda e^{-\lambda x}}
                     ''')
            st.latex(fr'''
                    E(X) = {1/lambdaa}
                    ''')
            st.latex(fr'''
                    Var(X) = {1/(lambdaa**2)}
                    ''')
            st.latex(fr'''
                    F_X({valor_exp}) = P(X \leq {valor_exp}) = {cdf}
                    ''')
            

    with col1:
        if distribu == "Normal":
            st.latex("\Large Gráfica")
            color_norm = st.color_picker("Elige el color de la gráfica", "#00f900")
            fc.normal(media,sigma,valor,color_norm)
        if distribu == "Exponencial":
            st.latex("\Large Gráfica")
            color_exp = st.color_picker("Elige el color de la gráfica", "#00f900")
            fc.exponencial(lambdaa,valor_exp,color_exp)