import plotly.express as px
import streamlit as st





def graficarBarras_Area(data, area):
    
    # Agrupar por 'Area' y 'Item' calculando la mediaF de 'hg/ha_yield'
    data_group_Area = data.groupby(['Area', 'Item']).agg({'hg/ha_yield': 'mean'})
    data_group_Area.reset_index(inplace=True)
    
    # Crear gráfico de barras para un área específica
    fig = px.bar(
        data_group_Area[data_group_Area["Area"] == area], 
        x='Item', 
        y='hg/ha_yield', 
        title=f"{area} - Yield per Item", 
        labels={'hg/ha_yield': 'Yield (hg/ha)'},
        color_discrete_sequence=["green"]  # Color de las barras
    )
    fig.update_layout(width=500, height=300)
    data_filtrada = data[data['Area'] == area]

    # Crear gráfico de contornos de densidad
    fig2 = px.density_contour(
        data_filtrada, 
        x="hg/ha_yield", 
        y="Item", 
        color="Item", 
        title=f"Density Plot of hg/ha_yield for {area} by Item",
        marginal_x="histogram",
        marginal_y="histogram"
    )
    fig.update_layout(width=500, height=300)
    # Rellenar las áreas bajo las curvas
    fig2.update_traces( )

    # Mostrar el gráfico
    
    left, right = st.columns(2)

    # Mostrar gráficos en las dos columnas
    with left:
        st.subheader(f":blue[Yield MEAN per Item for {area}]")
        st.plotly_chart(fig)

    with right:
        st.subheader(f":blue[Density Plot of hg/ha_yield for {area}]")
        st.plotly_chart(fig2)

    

def world_production_heatmap(data,item):
    # Agrupar datos por área y artículo
    data_group_Area = data.groupby(['Area', 'Item']).agg({'hg/ha_yield': 'mean'})
    data_group_Area.reset_index(inplace=True)
    
    # Filtrar solo los datos del ítem seleccionado
    filtered_data = data_group_Area[data_group_Area["Item"] == item]
    
    # Comprobar si hay datos para el ítem seleccionado
    if filtered_data.empty:
        st.write("No hay datos disponibles para este ítem.")
        return
    
    # Crear el mapa de calor
    fig = px.choropleth(
        filtered_data,
        locations="Area",
        locationmode="country names",
        color="hg/ha_yield",
        hover_name="Area",
        color_continuous_scale=px.colors.sequential.Plasma,  # Escala de color más atractiva
        title=f"{item} Production by Country",
        labels={'hg/ha_yield': 'Yield (hg/ha)'}  # Etiqueta personalizada para el color
    )

    # Mejorar la visualización
    fig.update_geos(
        visible=False,  # Ocultar el fondo del mapa
        landcolor='lightgrey',  # Color de fondo de la tierra
        showocean=True,  # Mostrar océanos
        oceancolor='lightblue'  # Color del océano
    )
    
    # Actualizar el diseño del gráfico
    fig.update_layout(
        width=1200,
        height=600,
        margin={"r":0,"t":50,"l":0,"b":0},  # Ajustar márgenes
        title_x=0.5  # Centrar el título
    )
    
    # Mostrar el gráfico
    st.plotly_chart(fig)

def Pesticide(data):
   
    fig = px.box(data, 
             x='Area', 
             y='pesticides_tonnes', 
             title='Boxplot of Pesticides Used by Area', 
             labels={'pesticides_tonnes': 'Pesticides Used (tonnes)', 'Area': 'Country'},
             color='Area')  # Color opcional por área

    fig.update_layout(width=1100, height=700)
    st.plotly_chart(fig)