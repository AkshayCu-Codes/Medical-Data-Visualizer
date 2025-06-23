import streamlit as st
from medical_data_visualizer import draw_cat_plot, draw_heat_map
import pandas as pd

# Set page config
st.set_page_config(
    page_title="🩺 Medical Data Visualizer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Intro Section
st.title("🩺 Medical Data Visualizer")
st.markdown("""
<style>
.intro-box {
    background-color: #1e1e1e;
    padding: 20px;
    border-left: 5px solid #4CAF50;
    border-radius: 6px;
    font-size: 16px;
    color: #f9f9f9;
}
</style>
<div class="intro-box">
    <strong>This Streamlit app visualizes medical examination data using:</strong><br><br>
    ✅ <strong>Categorical Plots:</strong> Show distributions of health and lifestyle features.<br>
    ✅ <strong>Correlation Heatmap:</strong> Explore relationships between medical variables.<br><br>
    📦 Built using <strong>pandas</strong>, <strong>seaborn</strong>, <strong>matplotlib</strong>, and <strong>Streamlit</strong>.
</div>
""", unsafe_allow_html=True)

st.divider()

# Load data once
@st.cache_data
def load_data():
    return pd.read_csv("medical_examination.csv")

df = load_data()

# Sidebar - Plot choice
st.sidebar.header("🔧 Plot Generator")
plot_type = st.sidebar.radio("Select a plot to generate:", ("Categorical Plot", "Correlation Heatmap"))

# Sidebar - Filters
st.sidebar.header("🧪 Filter Patients")
age_range = st.sidebar.slider("Select Age Range (years):", min_value=20, max_value=80, value=(30, 60))
smoker_option = st.sidebar.selectbox("Smoker Status", options=["All", "Smokers only", "Non-smokers"])
alcohol_option = st.sidebar.selectbox("Alcohol Intake", options=["All", "Drinkers only", "Non-drinkers"])
activity_option = st.sidebar.selectbox("Physical Activity", options=["All", "Active only", "Inactive only"])
cholesterol_option = st.sidebar.selectbox("Cholesterol Level", options=["All", "Normal", "Above Normal", "Well Above Normal"])

# Apply filters
filtered_df = df.copy()
filtered_df = filtered_df[(filtered_df['age'] / 365 >= age_range[0]) & (filtered_df['age'] / 365 <= age_range[1])]

if smoker_option == "Smokers only":
    filtered_df = filtered_df[filtered_df['smoke'] == 1]
elif smoker_option == "Non-smokers":
    filtered_df = filtered_df[filtered_df['smoke'] == 0]

if alcohol_option == "Drinkers only":
    filtered_df = filtered_df[filtered_df['alco'] == 1]
elif alcohol_option == "Non-drinkers":
    filtered_df = filtered_df[filtered_df['alco'] == 0]

if activity_option == "Active only":
    filtered_df = filtered_df[filtered_df['active'] == 1]
elif activity_option == "Inactive only":
    filtered_df = filtered_df[filtered_df['active'] == 0]

if cholesterol_option == "Normal":
    filtered_df = filtered_df[filtered_df['cholesterol'] == 1]
elif cholesterol_option == "Above Normal":
    filtered_df = filtered_df[filtered_df['cholesterol'] == 2]
elif cholesterol_option == "Well Above Normal":
    filtered_df = filtered_df[filtered_df['cholesterol'] == 3]

# Theme toggle
theme = st.sidebar.radio("Select theme:", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
    <style>
        body, .stApp { background-color: #111; color: white; }
        .stButton>button { background-color: #444; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Generate plot only when selected
if plot_type == "Categorical Plot":
    st.subheader("📊 Categorical Plot")
    draw_cat_plot()
    st.image("catplot.png", caption="Categorical Plot", use_container_width=True)

elif plot_type == "Correlation Heatmap":
    st.subheader("🔥 Correlation Heatmap")
    draw_heat_map()
    st.image("heatmap.png", caption="Correlation Heatmap", use_container_width=True)

# View data
st.divider()
with st.expander("🗃 View Filtered Medical Data"):
    st.dataframe(filtered_df.head(50))

# Summary section
st.divider()
st.subheader("📈 Summary Statistics of Filtered Data")
summary = filtered_df.describe()
st.write(summary)

# Dynamic insight paragraph
avg_sys = filtered_df['ap_hi'].mean()
avg_dia = filtered_df['ap_lo'].mean()
avg_weight = filtered_df['weight'].mean()
avg_chol = filtered_df['cholesterol'].mean()
n_patients = filtered_df.shape[0]

st.markdown(f"""
Based on the current filter selection (**{n_patients} patients**):
- **Avg. Systolic BP:** **{avg_sys:.1f} mmHg**
- **Avg. Diastolic BP:** **{avg_dia:.1f} mmHg**
- **Avg. Weight:** **{avg_weight:.1f} kg**
- **Avg. Cholesterol Level:** **{avg_chol:.2f}** (1 = normal, 2 = above normal, 3 = well above normal)

🩺 These figures help assess cardiovascular risk. Higher averages in BP or cholesterol can signal increased health risks in the selected group.
""")

# Footer with social icons
st.divider()
st.markdown("""
#### 📚 Reference
This project is part of the [freeCodeCamp Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) certification.

<p style='display: flex; align-items: center; gap: 10px;'>
  <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg' width='24'/>
  <a href='https://www.linkedin.com/in/akshay-c-0a7106134/' target='_blank'>LinkedIn</a>
</p>
<p style='display: flex; align-items: center; gap: 10px;'>
  <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg' width='24'/>
  <a href='https://github.com/AkshayCu-Codes' target='_blank'>GitHub</a>
</p>
""", unsafe_allow_html=True)
