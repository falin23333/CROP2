import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import main_text
import funciones
import model_performance
import predicion
# Título de la aplicaciónd


data = pd.read_csv("yield_df.csv")
data = data.drop(columns = "Unnamed: 0").copy()







# Título del Dashboard

main_text.imprime()
st.write("---")

predicion.prediction(data)
st.write("---")

st.title(f":red[👨🏽‍🌾💥 Crop Yield Analysis]")
area_seleccionada = st.select_slider("Select a Country (Area):", options=data["Area"].unique(), value=data["Area"].unique()[0])
funciones.graficarBarras_Area(data,area_seleccionada)

st.write("---")
st.title("🌽 Pesticide Application by Country🚜")
funciones.Pesticide(data)

st.write("---")
st.title("🌍 Global Agricultural Production Overview 📊")
item_seleccionado = st.radio("Select a Item:", options=data["Item"].unique(),horizontal=True ,index=0)
funciones.world_production_heatmap(data,item_seleccionado)


