import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Train demo model
X = np.array([[10,5,3],[20,7,2],[15,6,4],[30,9,5]])
y = np.array([100,150,120,200])

model = RandomForestRegressor()
model.fit(X,y)

st.title("Coal Demand Forecast App")

feature1 = st.number_input("Feature 1", value=10)
feature2 = st.number_input("Feature 2", value=5)
feature3 = st.number_input("Feature 3", value=3)

if st.button("Predict"):

    input_data = pd.DataFrame([[feature1,feature2,feature3]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Coal Demand: {prediction[0]:.2f}")
