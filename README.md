# ⚡ House Price Predictor (Linear Regression)

A sleek, easy-to-use web application that predicts house prices based on their size (square footage). It uses **Python (Flask)** for the backend and **Scikit-Learn** to run a Machine Learning model in real-time. It also includes an interactive dashboard to visualize the data.

---

## ✨ Features

*   **Instant Predictions:** Move the slider or type in a house size to see an immediate price estimate.
*   **Interactive Chart:** View a live scatter plot of the housing data and see exactly where your house falls on the model's trendline.
*   **Live Metrics:** Displays the exact math formula used by the model, along with its slope, intercept and $R^2$ accuracy score.
*   **Error Breakdown:** Shows a table comparing actual house prices vs. what the model predicted, color-coded by how close the guess was.

---

## 🚀 Tech Stack

*   **Backend:** Python, Flask
*   **Machine Learning:** Scikit-Learn (Linear Regression)
*   **Data Preparation:** Numpy, Pandas
*   **Frontend:** HTML5, CSS3 (Modern Dark Theme), JavaScript (ES6)
*   **Charts:** Chart.js

---

## 🛠️ Installation & Setup

Make sure you have Python installed on your computer.

### 1. Clone the Project
```bash
git clone [https://github.com/yourusername/house-price-predictor.git](https://github.com/yourusername/house-price-predictor.git)
```

### 2. Folder Structure
```bash
├── main.py
└── templates/
    ├── index.html
    └── chart.html
```

### 3. Install Requirements

Install the necessary Python libraries using pip:
```bash
pip install flask numpy pandas scikit-learn
```

### 4. Run the App

Start the flask server:
```bash
python main.py
```

Open your browser and copy paste the link to use the app.

---

## 📊 How it works

1. The app generates a fake dataset of 120 houses with sizes between 500 and 2,500 sq ft.
2. It calculates a realistic price using a base formula and adds some random noise to make it look like real-world data.
3. The Linear Regression model trains on 80% of this data to find the line of best fit.
4. When you give it a size, it plugs it into this classic formula to guess the price: Price = (Slope*Size) + Intercept
