import streamlit as st
import pandas as pd
import joblib

# Load model (LOCAL small model)
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# Title
st.title("⚡ Energy Consumption Predictor")

st.write("Enter the values below to predict energy consumption")

# Inputs
voltage = st.number_input("Voltage", value=240.0)
sub1 = st.number_input("Sub Metering 1", value=1.0)
sub2 = st.number_input("Sub Metering 2", value=0.0)
sub3 = st.number_input("Sub Metering 3", value=17.0)
reactive = st.number_input("Global Reactive Power", value=0.2)

hour = st.slider("Hour", 0, 23, 14)
day = st.slider("Day", 1, 31, 21)
month = st.slider("Month", 1, 12, 3)

# Predict
if st.button("Predict"):
    try:
        data = pd.DataFrame([{
            'Voltage': voltage,
            'Sub_metering_1': sub1,
            'Sub_metering_2': sub2,
            'Sub_metering_3': sub3,
            'Global_reactive_power': reactive,
            'hour': hour,
            'day': day,
            'month': month
        }])

        prediction = model.predict(data)

        st.success(f"⚡ Predicted Energy Consumption: {prediction[0]:.3f}")

        # Simple interpretation
        if prediction[0] > 3:
            st.warning("⚠️ High energy usage detected!")
        else:
            st.info("✅ Energy usage is normal")

    except Exception as e:
        st.error(f"❌ Error: {e}")