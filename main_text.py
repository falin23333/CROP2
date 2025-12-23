import streamlit as st
from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def imprime():
    # Title for the analysis
    # Introducció

    st.title(":green[Welcome to our interactive dashboard where we explore the fascinating world of agricultural production!] 🌍✨")
    st.image("agricultura.jpg", caption="Agricultural Overview", use_column_width=False)

    with st.container():
    
        left, right = st.columns(2)
        with left:
            st.header("📊 Data Visualization")
            st.write("""
            - **World Map**: We've created a global map highlighting the volume of various agricultural products (Items) across different countries, showcasing regional disparities in production. 🌎🔍
            - **Boxplot**: This visualization measures the density of pesticide usage by country, allowing us to understand its impact on agricultural practices. 🌿📉
            - **Bar Chart**: Here, we present annual crop yields by item, giving insights into productivity trends over time. 📈🌱
            """)

            # Sección de Predicciones
            st.header("🔮 Predictions")
            st.write("""
            Using our advanced model, you can predict hectograms per hectare based on factors like:
            - 🌡️ Average Temperature
            - 🌧️ Pesticide Usage
            - 🌍 Country
            - 💧 Average Rainfall
            - ... and more!

            We employed the **Random Forest Regressor** to make these predictions, achieving impressive metrics:
            - **Mean Squared Error (MSE)**: 121,234,416.31
            - **Root Mean Squared Error (RMSE)**: 11,010.65
            - **Mean Absolute Error (MAE)**: 5,373.46
            - **R² Score**: 0.98 🎯
            """)

            # Sección de Pipeline
            st.header("🛠️ Pipeline")
            st.write("""
            Our robust pipeline includes:
            - **Standard Scaler** for continuous variables
            - **One-Hot Encoder** for categorical data
            - **Grid Search** for hyperparameter optimization, ensuring we find the best settings for our Random Forest model! 🔧🔍
            """)

            # Conclusión
            st.write("""
            Explore the insights and predictions, and let's unlock the potential of agricultural data together! 🚀🌾
            """)
            

            # General description of the dataset
            st.write("This dataset consists of **28,242 entries** with **seven columns**. The columns represent various features related to agricultural production and environmental factors across different countries (referred to as **'Area'**). Here's an overview of the columns:")

            

        with right:
            
            # Sección de Visualización de Datos
            
            # Column description
            st.subheader("📊 Column Descriptions")

            # Details for each column
            st.markdown("""
            - **🌍 Area (Country):** This column contains categorical data representing different countries or regions. It is an object type and **has no missing values**.
            - **🌾 Item (Agricultural Product):** This column lists the type of agricultural product. It is also stored as an object. The data here indicates what crop or item is being analyzed.
            - **📅 Year:** An integer column indicating the year for which the data is recorded. It covers a range of years and tracks the changes over time.
            - **📈 hg/ha_yield (Crop Yield):** Contains integer data representing crop yield in hectograms per hectare (**hg/ha**). This is a key performance indicator of agricultural productivity.
            - **🌧️ average_rain_fall_mm_per_year (Average Rainfall):** A float column measuring the average annual rainfall in millimeters for each country. Rainfall is a crucial factor affecting crop yields.
            - **🧪 pesticides_tonnes (Pesticides Used):** A float column representing the amount of pesticides used, measured in tonnes. The use of pesticides can impact crop yield, but excessive use may have environmental and health repercussions.
            - **🌡️ avg_temp (Average Temperature):** This column contains float data representing the average temperature in degrees Celsius for each country during the respective year. Temperature is another significant factor that influences agricultural productivity.
            """)
            

            










    