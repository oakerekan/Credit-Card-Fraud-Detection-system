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
    <h2 style="color:white;text-align:center;">Portia's Credit Card Fraud Detection ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    V4 = float(st.text_input("V4 ('Values -6 and 20')"))
    V8 = float(st.text_input("V8 ('Values between -73 and 20')"))
    V10 = float(st.text_input("V10 ('Values between -25 and 25')"))
    V13 = float(st.text_input("V13 ('Values -6 and 8')"))
    V14 = float(st.text_input("V14 ('Values -20 and 12')"))
    V16 = float(st.text_input("V16 ('Values -15 and 18')"))
    V21 = float(st.text_input("V21 ('Values -35 and 30')"))
    V22 = float(st.text_input("V22 ('Values -11 and 11')"))
    V23 = float(st.text_input("V23 ('Values -45 and 25')"))
    V27 = float(st.text_input("V27 ('Values -23 and 31')"))

    # Code for Prediction
    result = ""
    if st.button("Predict Fraud"):
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
