


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Salary, Learning, Infra, Experience, School, Activity_based,
       English):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[Salary, Learning, Infra, Experience, School, Activity_based,
       English]])
    print(prediction)
    return prediction



def main():
  
    st.title("Happyness Index Prediction System ml")
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:#00FFFF;text-align:center;">Streamlit Happyness Index Prediction System ML App </h2>
    </div>
    <div3>
    <img src="https://i.ibb.co/tbbcV31/0-4-BF6-h-Vx-RLO9-O-i-Q.jpg" alt="0-4-BF6-h-Vx-RLO9-O-i-Q" border="0" width="700" height="500">
    </div3>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Salary = st.text_input("1.Is salary being given on time?	","Type Here")
    Learning = st.text_input("2.What about the teaching and learning process?","Type Here")
    Infra = st.text_input(" 3.How is the infrastructure?","Type Here")
    Experience = st.text_input("4.Teaching experience ","Type Here")
    School = st.text_input("5.How long have you been working in the same school?","Type Here")
    Activity_based = st.text_input(" 6.Is teaching done on activity based?","Type Here")
    English= st.text_input("7.How well can students speak and understand English?","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Salary, Learning, Infra, Experience, School, Activity_based,
       English
       )
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
