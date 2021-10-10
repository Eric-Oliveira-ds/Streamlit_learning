import seaborn as sns
import pandas as pd
import plotly.express as px 
import streamlit as st 

st.markdown('# Eric Oliveira App_Learning')
dados = sns.load_dataset('tips')
st.dataframe(dados)

def filtrar():
    
    filtro = st.sidebar.selectbox('select a column!',['sex',
                                                          'smoker',
                                                          'day',
                                                          'time',
                                                          'size'])
    
    selecao = dados['total_bill'].groupby(dados[filtro])\
                                          .mean()\
                                          .to_frame()

    
    return st.write(selecao)

def plota_grafico(dados:pd.DataFrame, x:pd.Series, color:str):
    
    grafico = px.histogram(dados, x, color=color)
    st.title(x.upper() + ' for ' + color.upper() )
    st.plotly_chart(grafico, use_container_width=True)
    
    return None
    
# Chamando as funções criadas anteriormente
filtrar()

plota_grafico(dados, x='total_bill', color='sex')

plota_grafico(dados, x='smoker', color='sex')

plota_grafico(dados, x='day', color='sex')

plota_grafico(dados, x='time', color='sex')

plota_grafico(dados, x='size', color='sex')

















