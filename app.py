import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Page config
st.set_page_config(page_title="Salary Prediction App", page_icon="💼", layout="centered")

# Title
st.title("💼 AI Salary Prediction System")

st.markdown("### 🔍 Predict your salary based on experience")
st.write("This AI model estimates your salary using a simple machine learning algorithm.")

# Dummy dataset
X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
y = np.array([15000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])

# Train model
model = LinearRegression()
model.fit(X, y)

# User input
exp = st.slider("📅 Years of Experience", 0.0, 10.0, 1.0)

# Prediction button
if st.button("💰 Predict Salary"):
    prediction = model.predict([[exp]])
    st.success(f"Estimated Salary: {int(prediction[0])} BDT")

# Extra UI
st.markdown("---")
st.info("📌 Note: This is a demo AI model for educational purposes.")

# Footer
st.markdown("👨‍💻 Developed by Md. Delowar Zahan (ID: 223002081)")