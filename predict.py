import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Dataset load karo
data = pd.read_csv("industrial_data.csv")

# Features aur target
X = data[["temperature", "pressure", "speed", "vibration"]]
y = data["quality"]

# AI model train karo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

print("===================================")
print(" AI INDUSTRIAL QUALITY PREDICTION")
print("===================================")

# User se machine data lena
temperature = float(input("Temperature (°C): "))
pressure = float(input("Pressure (bar): "))
speed = float(input("Speed (RPM): "))
vibration = float(input("Vibration: "))

# Prediction
new_data = pd.DataFrame({
    "temperature": [temperature],
    "pressure": [pressure],
    "speed": [speed],
    "vibration": [vibration]
})

prediction = model.predict(new_data)[0]

print("\nPredicted Quality:", prediction)

if prediction == "Good":
    print("Status: GOOD QUALITY")
else:
    print("Status: WARNING - POOR QUALITY")