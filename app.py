# importando as bibs
import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard — Anúncios de Veículos")

# lendo os dados
car_data = pd.read_csv('vehicles_us.csv')

# HISTOGRAMA
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Histograma do hodômetro dos veículos')
    fig = px.histogram(
        car_data,
        x="odometer",
        labels={
            "odometer": "Quilometragem (hodômetro)",
            "count": "Quantidade"
        },
        title="Distribuição da quilometragem"
    )
    st.plotly_chart(fig, use_container_width=True)


# SCATTER PLOT
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Relação entre quilometragem e preço')
    fig2 = px.scatter(
        car_data,
        x="odometer",
        y="price",
        labels={
            "odometer": "Quilometragem (hodômetro)",
            "price": "Preço (USD)"
        },
        title="Dispersão: Quilometragem vs Preço"
    )
    st.plotly_chart(fig2, use_container_width=True)


# BOXPLOT
boxplot_button = st.button('Criar boxplot de preço')

if boxplot_button:
    st.write('Distribuição de preços dos veículos')
    fig3 = px.box(
        car_data,
        y="price",
        labels={
            "price": "Preço (USD)"
        },
        title="Boxplot dos preços anunciados"
    )
    st.plotly_chart(fig3, use_container_width=True)
