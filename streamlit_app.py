import streamlit as st
from edge_computing.soil import SoilSample, SoilAnalyzer

st.set_page_config(page_title="Soil Analysis MVP", layout="centered")
st.title("🌱 Soil Analysis Report Generator")

st.markdown("Enter soil parameters to generate a fertilizer recommendation report in Hindi.")

# Input fields
nitrogen = st.number_input("Nitrogen (mg/kg)", min_value=0.0, max_value=100.0, value=40.0)
phosphorus = st.number_input("Phosphorus (mg/kg)", min_value=0.0, max_value=100.0, value=30.0)
potassium = st.number_input("Potassium (mg/kg)", min_value=0.0, max_value=100.0, value=35.0)
ph = st.number_input("pH", min_value=3.0, max_value=10.0, value=6.5)
organic_carbon = st.number_input("Organic Carbon (%)", min_value=0.0, max_value=10.0, value=1.5)

if st.button("Generate Report"):
    sample = SoilSample(nitrogen, phosphorus, potassium, ph, organic_carbon)
    analyzer = SoilAnalyzer()
    result = analyzer.analyze(sample)

    st.subheader("📄 Hindi Report")
    st.write(result["hindi_report"])

    st.subheader("📊 Recommendation Score")
    st.write(f"{result['recommendation']:.2f}")
