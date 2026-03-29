# 📊 CSV Analyzer

An interactive Streamlit-based web app to analyze any CSV dataset automatically.  
This tool performs data cleaning, visualization, and generates insights without manual effort.

---

## 🌐 Live Demo

🚀 **Try the app here:**  
👉https://csvanalyzerinsights.streamlit.app/#insights

---

## 🚀 Features

- 📁 Upload any CSV file  
- 🔍 Automatic column classification (categorical & numerical)  
- ⚠️ Missing value detection  
- 📈 Statistical summary of dataset  
- 📊 Visualizations:  
  - Count plots (categorical)  
  - Histograms (numerical)  
  - Boxplots (bivariate analysis)  
- 🔥 Correlation heatmap  
- 💡 Automatic insights generation based on correlation  
- 🎯 Removes useless columns like IDs automatically  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Streamlit  

---

## 📦 Installation

1. Clone the repository:

git clone https://github.com/codebyprathamesh/CSV-Analyzer-Streamlit.git

2. Install dependencies:

pip install -r requirements.txt  

3. Run the app:

streamlit run app.py  

---

## 🧠 How It Works

- The app reads the uploaded CSV file  
- Automatically detects categorical and numerical columns  
- Removes ID-like columns (columns with all unique values)  
- Generates visualizations for better understanding  
- Computes correlation between numerical features  
- Generates insights based on strong relationships  

---

## 💡 Example Insights

- Fare increases survival probability  
- Petal length strongly affects petal width  
- Price increases with parking availability  

---

## 📌 Use Cases

- Quick dataset understanding  
- Exploratory Data Analysis (EDA)  
- Beginner-friendly ML data exploration  
- Data preprocessing before modeling  

---

## ⚠️ Note

Some datasets may contain extreme outliers or weak correlations, which can affect visualizations and insights. This reflects real-world data behavior.

---

## 🙌 Acknowledgements

Thanks to the open-source Python ecosystem and learning resources that helped in building this project.

---

## 📬 Contact

If you liked this project or have suggestions, feel free to connect!
