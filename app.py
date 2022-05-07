import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

st.write("# Classificação de Iris")
st.write("## Exemplo com comprimentos de pétala e sépala")

st.sidebar.write('### Parâmetros')
com_sepala = st.sidebar.slider("Comprimento da sépala", 4.0, 8.0, 5.8, 0.1)
comp_petala = st.sidebar.slider("Comprimento da pétala", 0.9, 7.0, 3.8, 0.1)

arquivo = open("objetos.pkl", "rb")
ss, dtc = pickle.load(arquivo)
arquivo.close()

estrutura = {'comp_sepala': comp_sepala,
             'comp_petala' : comp_petala}

df = pd.DataFrame(estrutura, index = [0])
st.write(df)
