import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Example: Load your dataset (replace with your actual dataset)
# For illustration, I'm creating a dummy dataset
data = {
    'feature1': [0.1, 0.2, 0.3, 0.4, 0.5],
    'feature2': [0.2, 0.3, 0.4, 0.5, 0.6],
    'feature3': [0.3, 0.4, 0.5, 0.6, 0.7],
    'feature4': [0.4, 0.5, 0.6, 0.7, 0.8],
    'label': [1, 0, 1, 0, 1]  # 1 = Fraud, 0 = Not fraud
}
df = pd.DataFrame(data)

# Split the dataset into features and labels
X = df.drop('label', axis=1)  # Features
y = df['label']  # Labels (fraud or not fraud)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Save the trained model using pickle
with open('fraud_detection_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("Model saved as 'fraud_detection_model.pkl'")
