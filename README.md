# 📊 Customer Churn Prediction Web App

This project is a **Machine Learning-powered Web Application** that predicts whether a telecom customer is likely to **churn (leave the service)** or not.  
It is built with **Flask, Scikit-learn, and Joblib**, and deployed-ready with requirements for Heroku/Render.

---

## 🚀 Features
- 📂 Train a machine learning model on customer churn dataset  
- 🧠 Save and load trained models using **joblib**  
- 🌐 Web interface built with **Flask**  
- 🎨 Modern responsive UI with glassmorphism styling  
- 📊 Input customer details via a form and get churn prediction results instantly  

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS (Glassmorphism UI)  
- **Backend:** Python, Flask  
- **ML Model:** Scikit-learn (Logistic Regression / RandomForest etc.)  
- **Deployment:** Gunicorn + runtime environment  

---

## 📁 Project Structure
Customer-Churn-Prediction/
│── Dataset/
│ └── Customer-Churn.csv # Dataset used for training
│
│── static/ # Static assets (CSS, Images)
│ ├── style.css
│ ├── result.css
│ ├── tele1.png
│ ├── tele2.jpg
│ └── tele3.webp
│
│── templates/ # HTML templates
│ ├── index.html # Input form page
│ └── result.html # Prediction result page
│
│── app.py # Flask application
│── model_building.py # Model training and saving
│── model.joblib # Saved ML model
│── scaler.joblib # Saved data scaler
│── requirements.txt # Python dependencies
│── runtime.txt # Python runtime version
│── README.md # Project documentation


---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/customer-churn-prediction.git
   cd customer-churn-prediction

2 Create virtual environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

3 Install dependencies
pip install -r requirements.txt

4 Run the Flask app
python app.py

5 Open in browser:
http://127.0.0.1:5000/



📸 Screenshots
🏠 Input Form

(Add screenshot here)

📊 Prediction Result

(Add screenshot here)

