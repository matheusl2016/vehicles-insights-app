import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard — Anúncios de Veículos")

# lendo os dados
car_data = pd.read_csv('vehicles.csv')

# criando um botão para histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# criando um botão para dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão: odometer x price')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)

# criando um botão para Boxplot
boxplot_button = st.button('Criar boxplot de preço')

if boxplot_button:
    st.write('Criando um boxplot para a coluna price')
    fig3 = px.box(car_data, y="price")
    st.plotly_chart(fig3, use_container_width=True)