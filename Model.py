

import streamlit as st
import pickle 
import numpy as np

st.title('Flower Classification App')

with open('model.pkl', 'rb') as f:
    lr_model = pickle.load(f)

sepal_length = st.slider('Enter sepal length',0,10,1)
sepal_width = st.slider('Enter sepal width',0,10,1)      
petal_length = st.slider('Enter petal length',0,10,1)
petal_width = st.slider('Enter petal width',0,10,1)

if st.button('Predict'):
    pred= lr_model.predict(np.array([[sepal_length,sepal_width,petal_length,petal_width]]))
    st.write("The Flower is :", pred[0])