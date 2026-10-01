import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# CSV file read karna
data = pd.read_csv("industrial_data.csv")

# Input features
X = data[["temperature", "pressure", "speed", "vibration"]]

# Target/output
y = data["quality"]

# Data ko training aur testing mein divide karna
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# AI model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Model ko train karna
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("AI Model trained successfully!")
print("Model Accuracy:", round(accuracy * 100, 2), "%")