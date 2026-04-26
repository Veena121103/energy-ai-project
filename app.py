import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Title
st.title("⚡ Energy Consumption Predictor")
st.write("Enter the values below to predict energy consumption")

# Inputs
voltage = st.number_input("Voltage", value=240.0)
sub1 = st.number_input("Sub Metering 1", value=1.0)
sub2 = st.number_input("Sub Metering 2", value=0.0)
sub3 = st.number_input("Sub Metering 3", value=17.0)
grp = st.number_input("Global Reactive Power", value=0.2)

hour = st.slider("Hour", 0, 23, 12)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)

# Create input dataframe (IMPORTANT: order must match training)
data = pd.DataFrame({
    'Voltage': [voltage],
    'Sub_metering_1': [sub1],
    'Sub_metering_2': [sub2],
    'Sub_metering_3': [sub3],
    'Global_reactive_power': [grp],
    'hour': [hour],
    'day': [day],
    'month': [month]
})

# Predict
if st.button("Predict"):
    prediction = model.predict(data)
    value = prediction[0]

    st.subheader(f"⚡ Predicted Energy Consumption: {value:.3f}")

    # DATA-DRIVEN THRESHOLDS
    if value < 1.4:
        st.success("✅ Low energy usage")
    elif value < 6.4:
        st.info("👍 Normal energy usage")
    else:
        st.warning("⚠️ High energy usage detected!")

    # Optional info
    st.caption("Thresholds based on dataset distribution (Q1=1.4, Q3=6.4)")