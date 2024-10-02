import streamlit as st

import pickle
import pandas as pd
from streamlit_lottie import st_lottie
import model_performance
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def prediction(df_train):
    cat_features = ["Area","Item"]
    num_features = ["Year","average_rain_fall_mm_per_year","pesticides_tonnes","avg_temp"]
    num_input = {}
    cat_input = {}

    with st.container():
        st.subheader(":red[🌍 Future Harvests: Yield Prediction Dashboard 🌱] :wave:")
        model_performance.plot_predictions_vs_actuals()
        model_performance.plot_residuals()
        left, right = st.columns(2)
        with left:
            for feature in cat_features:
                value = st.selectbox(f':blue[{feature}]', df_train[feature].unique(), key=feature)
                cat_input[feature] = value
            lottie_url = " https://lottie.host/0caf0142-8476-4755-bef1-4a166b67f6a3/vNFugFbq57.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json, height=200)

        with right:
            for feature in num_features:
                min_val = int(df_train[feature].min())
                max_val = int(df_train[feature].max())
                selected_value = st.slider(f':blue[{feature}]', min_value=min_val, max_value=max_val, value=min_val)
                num_input[feature] = selected_value
        
        # Add a button for prediction
        if st.button("Make Prediction", key="prediction_button"):
            user_input = {}
            user_input.update(num_input)
            user_input.update(cat_input)

            # Load the model from the file
            with open('pipeline_xgb.pkl', 'rb') as file:
                model = pickle.load(file)

            prediction = model.predict(pd.DataFrame(user_input, index=[0]))
           
            
            
            st.write(f"""
                     :blue[Crop Yield in hectograms per hectare :] 
                     {prediction}hg/ha  """)
            
    
