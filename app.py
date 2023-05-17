# -*- coding: utf-8 -*-

"""
Created on Tue May 16 08:55:44 2023

@author: Portia Twumasi
"""

import numpy as np
import pickle
import streamlit as st

from tensorflow.keras.models import load_model
classifier = load_model('model.h5')

# pickle_in = open("classifier.pkl", "rb")
# classifier = pickle.load(pickle_in)


# @app.route('/')
def welcome():
    return "Welcome All"


# @app.route('/predict',methods=["Get"])
def predict_fraud(V4, V8, V10, V13, V14, V16, V21, V22, V23, V27):
    prediction = classifier.predict([[V4, V8, V10, V13, V14, V16, V21, V22, V23, V27]])
    return prediction


def main():
    st.title("Credit Card Fraud Detection System")
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;"> Credit Card Fraud Detection ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    V4 = st.number_input("V4 (values -6 and 20)")
    V8 = st.number_input("V8 (values between -73 and 20)")
    V10 = st.number_input("V10 (values between -25 and 25)")
    V13 = st.number_input("V13 (values -6 and 8)")
    V14 = st.number_input("V14 (values -20 and 12)")
    V16 = st.number_input("V16 (values -15 and 18)")
    V21 = st.number_input("V21 (values -35 and 30)")
    V22 = st.number_input("V22 (values -11 and 11)")
    V23 = st.number_input("V23 (values -45 and 25)")
    V27 = st.number_input("V27 (values -23 and 31)")

    # Code for Prediction
    result = ""
    if st.button("Detect Fraud"):
        result = predict_fraud(V4, V8, V10, V13, V14, V16, V21, V22, V23, V27)
        if result >= 0.9:
            result = "This is a fraudulent transaction"
            print(result)
        else:
            result = "This is a normal transaction "
            print(result)
        
    st.success(result)


if __name__ == '__main__':
    main()
