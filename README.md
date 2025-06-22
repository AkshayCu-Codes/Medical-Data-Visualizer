
# 🩺 Medical Data Visualizer

This project analyzes and visualizes medical examination data using `pandas`, `seaborn`, and `matplotlib`. It includes two key visualizations:

- 📊 **Categorical Plot:** Compares lifestyle and health features between patients with and without cardiovascular disease.
- 🔥 **Heat Map:** Displays correlations between all features after data cleaning.

---

## 📁 Files

- `medical_data_visualizer.py` — main script with all logic
- `main.py` — runs the script and tests
- `test_module.py` — unit tests provided by freeCodeCamp
- `medical_examination.csv` — dataset (patients and their medical records)
- `catplot.png` — saved categorical plot output
- `heatmap.png` — saved heatmap output

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

## ▶️ How to Run

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run project:**

   ```bash
   python3 main.py
   ```

3. **View output:**
   - `catplot.png`
   - `heatmap.png`

---

## 📚 Credits

Based on the [freeCodeCamp Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) certification project.
