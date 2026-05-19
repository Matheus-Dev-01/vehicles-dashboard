import pandas as pd
import plotly.express as px
import streamlit as st

# carregar dados
df = pd.read_csv('vehicles_us.csv')

# cabecalho e descricao
st.header('Vehicles US — Dashboard de Anúncios de Veículos')

st.write(
    'Aplicativo simples para explorar o dataset de anúncios de venda '
    'de veículos usados nos Estados Unidos. Marque as opções abaixo '
    'para visualizar os gráficos.'
)

# checkbox: histograma do odometer
show_hist = st.checkbox('Mostrar histograma do odômetro')

if show_hist:
    st.write('Construindo histograma para a coluna *odometer*...')
    fig_hist = px.histogram(
        df,
        x='odometer',
        nbins=50,
        title='Distribuição do odômetro'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# checkbox: scatter plot odometer x price
show_scatter = st.checkbox('Mostrar gráfico de dispersão (odômetro x preço)')

if show_scatter:
    st.write('Construindo gráfico de dispersão *odometer* vs *price*...')
    fig_scatter = px.scatter(
        df,
        x='odometer',
        y='price',
        title='Odômetro x Preço'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
