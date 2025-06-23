# 🩺 Medical Data Visualizer

This project analyzes and visualizes medical examination data using **pandas**, **seaborn**, **matplotlib**, and **Streamlit**. It provides an interactive web interface to explore health indicators and cardiovascular risk factors.

[![Streamlit App](https://img.shields.io/badge/Live%20App-Medical%20Visualizer-4CAF50?logo=streamlit&logoColor=white)](https://medical-data-visualizer-app.streamlit.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Akshay%20CU-blue?logo=linkedin)](https://www.linkedin.com/in/akshay-c-0a7106134/)
[![GitHub](https://img.shields.io/badge/GitHub-AkshayCu--Codes-black?logo=github)](https://github.com/AkshayCu-Codes)

---

## 🌐 Live App

Click here to explore the deployed app:  
🔗 **[https://medical-data-visualizer-app.streamlit.app/](https://medical-data-visualizer-app.streamlit.app/)**

---

## 📊 Visualizations

- **Categorical Plot:** Compares lifestyle and health features between patients with and without cardiovascular disease.
- **Correlation Heatmap:** Displays correlations between various medical examination features.

---

## 📁 Files

| File                      | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| `medical_data_visualizer.py` | Main script for data processing and plotting                  |
| `main.py`                 | Runs `medical_data_visualizer.py` locally and executes tests  |
| `app.py`                  | Streamlit app entry point for deployment                      |
| `test_module.py`          | Unit tests (freeCodeCamp provided)                            |
| `medical_examination.csv` | Input dataset containing patient records                      |
| `catplot.png`             | Output image of the categorical plot                          |
| `heatmap.png`             | Output image of the correlation heatmap                       |

---

## 🧪 Features Visualized

- `cholesterol`
- `gluc`
- `smoke`
- `alco`
- `active`
- `overweight`
- `cardio` (target variable)

---

## ▶️ How to Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run project
```bash
python3 main.py
```

### 3. View generated plots
- `catplot.png`
- `heatmap.png`

---

## 📚 Credits

This project is part of the  
🎓 [freeCodeCamp - Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) Certification.
