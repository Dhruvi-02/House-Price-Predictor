from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

app = Flask(__name__)

# Data Preparation
np.random.seed(100)
sizes = np.random.randint(500,2500,size=120)
other = np.random.normal(0,15,size=120)
prices = (0.16*sizes + 50) + other

df = pd.DataFrame({
    'size' : sizes,
    'price' : prices.round(2)
})

X = df[['size']].values 
y = df['price'].values

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model Training 
model = LinearRegression()
model.fit(X_train, y_train)

# Showing homepage when user visits the main link
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chart.html')
def chart_page():
    return render_template('chart.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Receive input from the UI
    user_input = request.json.get('size')
    size_array = np.array([[float(user_input)]])
    
    # Predicting using Scikit-Learn
    prediction = model.predict(size_array)[0]
    
    # Returning everything the UI needs
    return jsonify({
        'price': round(float(prediction), 2),
        'slope': round(float(model.coef_[0]), 4),
        'intercept': round(float(model.intercept_), 2),
        'r2_score': round(float(model.score(X_test,y_test)),3)
    })

@app.route('/get_data')
def get_data():
    return jsonify({
        'sizes': df['size'].tolist(),
        'prices': df['price'].tolist(),
        'slope': float(model.coef_[0]),
        'intercept': float(model.intercept_),
        'r2_score': round(float(model.score(X_test,y_test)),3)
    })

if __name__ == '__main__':
    app.run(debug=True)


