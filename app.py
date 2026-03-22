import streamlit as st
import pandas as pd
import joblib
import os
import gdown

# Google Drive File ID
FILE_ID = "1e6t2JoFLCgEOo-ELAobxY4oSgsL_8j23"
MODEL_PATH = "model.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        try:
            url = f"https://drive.google.com/uc?id={FILE_ID}"
            gdown.download(url, MODEL_PATH, quiet=False)
        except Exception as e:
            st.error(f"Download failed: {e}")
            return None
    return joblib.load(MODEL_PATH)

model = load_model()

if model is None:
    st.stop()

# UI
st.title("⚡ Energy Consumption Predictor")

voltage = st.number_input("Voltage", value=240.0)
intensity = st.number_input("Global Intensity", value=10.0)
sub1 = st.number_input("Sub Metering 1", value=1.0)
sub2 = st.number_input("Sub Metering 2", value=0.0)
sub3 = st.number_input("Sub Metering 3", value=17.0)
reactive = st.number_input("Global Reactive Power", value=0.2)
hour = st.slider("Hour", 0, 23, 14)
day = st.slider("Day", 1, 31, 21)
month = st.slider("Month", 1, 12, 3)

if st.button("Predict"):
    data = pd.DataFrame([{
        'Voltage': voltage,
        'Global_intensity': intensity,
        'Sub_metering_1': sub1,
        'Sub_metering_2': sub2,
        'Sub_metering_3': sub3,
        'Global_reactive_power': reactive,
        'hour': hour,
        'day': day,
        'month': month
    }])

    prediction = model.predict(data)

    st.success(f"⚡ Predicted Energy Consumption: {prediction[0]}")

    if prediction[0] > 3:
        st.warning("⚠️ High energy usage!")
    else:
        st.info("✅ Energy usage is normal")