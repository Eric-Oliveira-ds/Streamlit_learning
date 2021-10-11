import pandas as pd
import plotly.express as px 
import streamlit as st 

st.markdown('# Eric Oliveira App_Learning')
dados = pd.read_csv('dados/tips.csv')
st.dataframe(dados)

def filtrar():
    
    filtro = st.sidebar.selectbox('select a column!',['smoker',
                                                      'sex',
                                                      'day',
                                                      'time',
                                                      'size'])
    
    selecao = dados['total_bill'].groupby(dados[filtro])\
                                          .mean()\
                                          .to_frame()

    
    return st.write(selecao)

def plota_grafico(dados:pd.DataFrame, x:pd.Series, color:pd.Series):
    
    grafico = px.histogram(dados, x, color=color)
    st.title(x + ' for ' + color )
    st.plotly_chart(grafico, use_container_width=True)
    
    return None
    
# Chamando as funções criadas anteriormente
filtrar()

plota_grafico(dados, x='total_bill', color='sex')

plota_grafico(dados, x='sex', color='smoker')

plota_grafico(dados, x='total_bill', color='day')

plota_grafico(dados, x='total_bill', color='time')

plota_grafico(dados, x='size', color='sex')

















