import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  # Or whichever model you're using

# Load dataset
data = pd.read_csv('dataset/water_potability.csv')

# Define features and target variable
X = data[['ph', 'Turbidity', 'Solids', 'Conductivity']]  # Ensure correct column names
y = data['Potability']  # Update based on your dataset

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Ensure the 'model' directory exists
model_dir = "model"
os.makedirs(model_dir, exist_ok=True)

# Save trained model
joblib.dump(model, os.path.join(model_dir, "water_quality_model.pkl"))
print("Model trained and saved successfully!")
