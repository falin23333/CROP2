
import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
import streamlit as st

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def plot_predictions_vs_actuals():
    """
    Plots the relationship between actual and predicted values and calculates evaluation metrics.

    Parameters:
    y_true (array-like): Actual values.
    y_pred (array-like): Predicted values by the Random Forest model.
    """
    data = pd.read_csv("yield_df.csv")
    data = data.drop(columns = "Unnamed: 0").copy()
    X= data.drop(columns = "hg/ha_yield")
    y = data["hg/ha_yield"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    with open('pipeline_xgb.pkl', 'rb') as file:
        model = pickle.load(file)
        
    
    y_pred = model.predict(X_test)
    # Calcular métricas de evaluacións
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Crear el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # línea 1:1
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Actual vs Predicted Values')
    plt.grid(True)

    # Mostrar las métricas en el gráfico
    plt.figtext(0.15, 0.85, f'MSE: {mse:.2f}', fontsize=12)
    plt.figtext(0.15, 0.80, f'RMSE: {rmse:.2f}', fontsize=12)
    plt.figtext(0.15, 0.75, f'MAE: {mae:.2f}', fontsize=12)
    plt.figtext(0.15, 0.70, f'R²: {r2:.2f}', fontsize=12)

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)

# Uso de la función
# y_true = [...]  # Tus valores reales
# y_pred = [...]  # Tus predicciones del modelo Random Forest



def plot_residuals():
    """
    Plots the residuals of the model predictions.

    Parameters:
    y_true (array-like): Actual values.
    y_pred (array-like): Predicted values by the model.
    """
    data = pd.read_csv("yield_df.csv")
    data = data.drop(columns = "Unnamed: 0").copy()
    X= data.drop(columns = "hg/ha_yield")
    y = data["hg/ha_yield"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    with open('pipeline_xgb.pkl', 'rb') as file:
        model = pickle.load(file)
        

    y_pred = model.predict(X_test)
    residuals = y_test - y_pred

    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals)
    plt.axhline(y=0, color='r', linestyle='--')  # Línea horizontal en 0
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title('Residuals vs Predicted Values')
    plt.grid(True)
    st.pyplot(plt)

