# app.py
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import streamlit as st
from dill import load
from sklearn.preprocessing import MinMaxScaler

# Load the trained K-Means model
with open("k_means.pkl", "rb") as file:
    loaded_model = load(file)

# Define the cluster prediction function
def Cluster_prediction(input_data):
    input_data = np.array(input_data, dtype=float).reshape(1, -1)
    scaler = MinMaxScaler()
    input_data_scaled = scaler.fit_transform(input_data)
    prediction = loaded_model.predict(input_data_scaled)

    if prediction[0] == 0:
        return "DEVELOPED COUNTRY", "green"
    elif prediction[0] == 1:
        return "UNDER DEVELOPED COUNTRY", "red"
    else:
        return "DEVELOPING COUNTRY", "blue"

# Streamlit App
def main():
    st.set_page_config(page_title="Country Development Predictor", page_icon="🌍", layout="wide")

    st.markdown(
        "<h1 style='color:green;'>Predicting the State of Development of a Country</h1>",
        unsafe_allow_html=True
    )
    st.markdown("<h4 style='color:blue;'>Enter the values below to predict the country's development status</h4>", unsafe_allow_html=True)

    st.sidebar.header("Input Parameters")
    st.sidebar.markdown("<h5 style='color:red;'>Please fill in all fields to avoid errors</h5>", unsafe_allow_html=True)

    # Sidebar inputs
    Birth_Rate = st.sidebar.number_input('Birth Rate (0.000 - 1.000)', step=0.001, format="%.3f")
    Business_Tax_Rate = st.sidebar.number_input('Business Tax Rate (%)')
    CO2_Emissions = st.sidebar.number_input('CO2 Emissions')
    Days_to_Start_Business = st.sidebar.number_input('Days to Start Business')
    Energy_Usage = st.sidebar.number_input('Energy Usage')
    GDP = st.sidebar.number_input('Total GDP ($)')
    Health_Exp_GDP = st.sidebar.number_input('Health Exp % GDP') / 100
    Health_Exp_Capita = st.sidebar.number_input('Health Exp/Capita ($)')
    Hours_to_do_Tax = st.sidebar.number_input('Hours to do Tax')
    Infant_Mortality_Rate = st.sidebar.number_input('Infant Mortality Rate (0.000 - 1.000)', step=0.001, format="%.3f")
    Internet_Usage = st.sidebar.number_input('Internet Usage')
    Lending_Interest = st.sidebar.number_input('Lending Interest (%)')
    Life_Expectancy_Female = st.sidebar.number_input('Life Expectancy Female (years)')
    Life_Expectancy_Male = st.sidebar.number_input('Life Expectancy Male (years)')
    Mobile_Phone_Usage = st.sidebar.number_input('Mobile Phone Usage')
    Population_0_14 = st.sidebar.number_input('Population 0-14 (%)') / 100
    Population_15_64 = st.sidebar.number_input('Population 15-64 (%)') / 100
    Population_65_and_above = st.sidebar.number_input('Population 65+ (%)') / 100
    Population_Total = st.sidebar.number_input('Total Population')
    Population_Urban = st.sidebar.number_input('Urban Population (%)') / 100
    Tourism_Inbound = st.sidebar.number_input('Tourism Inbound ($)')
    Tourism_Outbound = st.sidebar.number_input('Tourism Outbound ($)')

    # Prepare dataframe to show entered values
    data = {
        'Birth rate': Birth_Rate,
        'Business tax rate': Business_Tax_Rate,
        'CO2 Emissions': CO2_Emissions,
        'Days to start business': Days_to_Start_Business,
        'Energy usage': Energy_Usage,
        'GDP': GDP,
        'Health Exp % in GDP': Health_Exp_GDP,
        'Health exp/capita': Health_Exp_Capita,
        'Hours to do Tax': Hours_to_do_Tax,
        'Infant Mortality Rate': Infant_Mortality_Rate,
        'Internet usage': Internet_Usage,
        'Lending interest': Lending_Interest,
        'Life expectancy female': Life_Expectancy_Female,
        'Life expectancy male': Life_Expectancy_Male,
        'Mobile phone usage': Mobile_Phone_Usage,
        'Population%(0-14)': Population_0_14,
        'Population%(15-64)': Population_15_64,
        'Population% 65+': Population_65_and_above,
        'Total Population': Population_Total,
        'Urban Population %': Population_Urban,
        'Tourism Inbound': Tourism_Inbound,
        'Tourism Outbound': Tourism_Outbound
    }

    st.write("### Entered Data Preview")
    st.dataframe(pd.DataFrame(data, index=["Values"]).T, width=600, height=800)

    # Predict button
    if st.button("Predict Development Status"):
        input_features = [[
            Birth_Rate, Business_Tax_Rate, CO2_Emissions, Days_to_Start_Business, Energy_Usage, GDP,
            Health_Exp_GDP, Health_Exp_Capita, Hours_to_do_Tax, Infant_Mortality_Rate, Internet_Usage,
            Lending_Interest, Life_Expectancy_Female, Life_Expectancy_Male, Mobile_Phone_Usage,
            Population_0_14, Population_15_64, Population_65_and_above, Population_Total,
            Population_Urban, Tourism_Inbound, Tourism_Outbound
        ]]

        result, color = Cluster_prediction(input_features)
        st.markdown(f"<h3>This is a <span style='color:{color};'>{result}</span></h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
