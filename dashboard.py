import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(
    page_title="AI Industrial Quality Prediction",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 AI-Based Industrial Process Quality Prediction")
st.write("AI-powered industrial machine quality monitoring dashboard")

data = pd.read_csv("industrial_data.csv")

X = data[["temperature", "pressure", "speed", "vibration"]]
y = data["quality"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

st.sidebar.header("Machine Parameters")

temperature = st.sidebar.number_input(
    "Temperature (°C)",
    min_value=0.0,
    max_value=150.0,
    value=75.0
)

pressure = st.sidebar.number_input(
    "Pressure (bar)",
    min_value=0.0,
    max_value=10.0,
    value=3.5
)

speed = st.sidebar.number_input(
    "Speed (RPM)",
    min_value=0.0,
    max_value=3000.0,
    value=1200.0
)

vibration = st.sidebar.number_input(
    "Vibration",
    min_value=0.0,
    max_value=10.0,
    value=0.8
)

new_data = pd.DataFrame({
    "temperature": [temperature],
    "pressure": [pressure],
    "speed": [speed],
    "vibration": [vibration]
})

prediction = model.predict(new_data)[0]

probability = model.predict_proba(new_data)[0]
confidence = max(probability) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Temperature", f"{temperature:.1f} °C")
col2.metric("Pressure", f"{pressure:.1f} bar")
col3.metric("Speed", f"{speed:.0f} RPM")
col4.metric("Vibration", f"{vibration:.2f}")

st.divider()

st.subheader("🤖 AI Prediction")

if prediction == "Good":
    st.success("🟢 GOOD QUALITY")
else:
    st.error("🔴 POOR QUALITY")

st.metric("Prediction Confidence", f"{confidence:.1f}%")

st.subheader("📊 Industrial Data")

st.dataframe(data, use_container_width=True)