# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:00:29 2024

@author: darsh
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd

# Load the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Function for predictions
def breast_cancer_prediction(data):
    # Convert the dictionary into a pandas DataFrame
    input_df = pd.DataFrame(data, index=[0])

    # Use the trained model to make a prediction
    prediction = loaded_model.predict(input_df)

    if prediction[0] == 0:
        return "The Person does not have Breast Cancer."
    else:
        return "The Person has Breast Cancer."

def main():
    # Giving a title
    st.title('Breast Cancer Prediction')

    # Create sliders for each input feature
    radius1 = st.slider("Radius 1", min_value=6.981, max_value=28.110, value=10.0)
    texture1 = st.slider("Texture 1", min_value=9.710, max_value=39.280, value=20.0)
    perimeter1 = st.slider("Perimeter 1", min_value=43.790, max_value=188.500, value=100.0)
    area1 = st.slider("Area 1", min_value=143.500, max_value=2501.000, value=1000.0)
    smoothness1 = st.slider("Smoothness 1", min_value=0.052630, max_value=0.16340, value=0.1)
    compactness1 = st.slider("Compactness 1", min_value=0.019380, max_value=0.34540, value=0.1)
    concavity1 = st.slider("Concavity 1", min_value=0.000000, max_value=0.42680, value=0.1)
    concave_points1 = st.slider("Concave Points 1", min_value=0.000000, max_value=0.20120, value=0.1)
    symmetry1 = st.slider("Symmetry 1", min_value=0.106000, max_value=0.30400, value=0.2)

    radius2 = st.slider("Radius 2", min_value=0.111500, max_value=2.873, value=1.0)
    perimeter2 = st.slider("Perimeter 2", min_value=0.757000, max_value=21.980, value=10.0)
    area2 = st.slider("Area 2", min_value=6.802, max_value=542.200, value=100.0)
    compactness2 = st.slider("Compactness 2", min_value=0.002252, max_value=0.13540, value=0.05)
    concavity2 = st.slider("Concavity 2", min_value=0.000000, max_value=0.39600, value=0.1)
    concave_points2 = st.slider("Concave Points 2", min_value=0.000000, max_value=0.05279, value=0.01)

    radius3 = st.slider("Radius 3", min_value=7.930000, max_value=36.04000, value=20.0)
    texture3 = st.slider("Texture 3", min_value=12.020000, max_value=49.54000, value=30.0)
    perimeter3 = st.slider("Perimeter 3", min_value=50.410000, max_value=251.20000, value=100.0)
    area3 = st.slider("Area 3", min_value=185.200000, max_value=4254.00000, value=2000.0)
    smoothness3 = st.slider("Smoothness 3", min_value=0.071170, max_value=0.22260, value=0.1)
    compactness3 = st.slider("Compactness 3", min_value=0.027290, max_value=1.05800, value=0.1)
    concavity3 = st.slider("Concavity 3", min_value=0.000000, max_value=1.25200, value=0.1)
    concave_points3 = st.slider("Concave Points 3", min_value=0.000000, max_value=0.29100, value=0.1)
    symmetry3 = st.slider("Symmetry 3", min_value=0.156500, max_value=0.66380, value=0.2)
    fractal_dimension3 = st.slider("Fractal Dimension 3", min_value=0.055040, max_value=0.20750, value=0.1)

    # Prepare the data for prediction
    data = {
        "radius1": radius1,
        "texture1": texture1,
        "perimeter1": perimeter1,
        "area1": area1,
        "smoothness1": smoothness1,
        "compactness1": compactness1,
        "concavity1": concavity1,
        "concave_points1": concave_points1,
        "symmetry1": symmetry1,
        "radius2": radius2,
        "perimeter2": perimeter2,
        "area2": area2,
        "compactness2": compactness2,
        "concavity2": concavity2,
        "concave_points2": concave_points2,
        "radius3": radius3,
        "texture3": texture3,
        "perimeter3": perimeter3,
        "area3": area3,
        "smoothness3": smoothness3,
        "compactness3": compactness3,
        "concavity3": concavity3,
        "concave_points3": concave_points3,
        "symmetry3": symmetry3,
        "fractal_dimension3": fractal_dimension3
    }

    # Code for prediction
    diagnosis = ''

    # Creating button for prediction
    if st.button('Cancer Test Result'):
        diagnosis = breast_cancer_prediction(data)
        st.success(diagnosis)

if __name__ == '__main__':
    main()
