# app.py

from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")   # create index.html in templates folder

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get input data from form
        features = []
        for key in request.form.keys():
            features.append(request.form.get(key))
        
        # Convert to DataFrame (1 row)
        input_df = pd.DataFrame([features])

        # Convert numeric where possible
        for col in input_df.columns:
            try:
                input_df[col] = pd.to_numeric(input_df[col])
            except:
                pass

        # Encode categorical (label encoding style like training)
        for col in input_df.columns:
            if input_df[col].dtype == "object":
                input_df[col] = pd.factorize(input_df[col])[0]

        # Scale features
        input_scaled = scaler.transform(input_df)

        # Prediction
        prediction = model.predict(input_scaled)[0]

        result = "Customer is likely to Churn ❌" if prediction == 1 else "Customer will Stay ✅"

        return render_template("result.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
