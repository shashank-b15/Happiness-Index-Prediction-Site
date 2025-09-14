


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
def predict_note_authentication(Levels, Environment, Competitive, Classes, Lab, Sports,
       Toilet, Sports_Competition, Students_per_class, Langugae,
       Timings, Meetings, Fests, Field_trips, Water, Mid_day_meal,
       Quality_of_food, Assessment, Region):
    
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
   
    prediction=classifier.predict([[Levels, Environment, Competitive, Classes, Lab, Sports,
       Toilet, Sports_Competition, Students_per_class, Langugae,
       Timings, Meetings, Fests, Field_trips, Water, Mid_day_meal,
       Quality_of_food, Assessment, Region]])
    print(prediction)
    return prediction



def main():
  
    st.title("Happyness Index Prediction System ml")
    html_temp = """
    <div style="background-color:red;padding:10px">
    <h2 style="color:#00FFFF;text-align:center;">Streamlit Happyness Index student System using  ML App </h2>
    </div>
    <div3>
    <img src="https://i.ibb.co/tbbcV31/0-4-BF6-h-Vx-RLO9-O-i-Q.jpg" alt="0-4-BF6-h-Vx-RLO9-O-i-Q" border="0" width="700" height="500">
    </div3>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Levels = st.text_input("1.What is the level of courses?	","Type Here")
    Environment = st.text_input("2.Type of environment in the school?","Type Here")
    Competitive = st.text_input("Competitive","Type Here")
    Classes = st.text_input("3.Does Teachers have competitive nature?","Type Here")
    Lab = st.text_input("4.What are the number of teaching classes per day?","Type Here")
    Sports = st.text_input("5.Are they providing enough facilities for laboratory?","Type Here")
    Toilet= st.text_input("6.How many hours are allocated to the sports?","Type Here")
    Sports_Competition	 = st.text_input("7.What is the condition of the toilets?	","Type Here")
    Students_per_class	 = st.text_input("Students_per_class	","Type Here")
    Langugae	 = st.text_input("8.Are there any sports competition in the school?","Type Here")
    Timings	 = st.text_input("9.How many students per class?","Type Here")
    Fests	 = st.text_input("10.In which language teachers communicate with the students?","Type Here")
    Field_trips	 = st.text_input("11.What are timings of the school?	","Type Here")
    Water	 = st.text_input("12.How frequent the parent’s teachers meeting are held?","Type Here")
    Mid_day_meal	 = st.text_input("Mid_day_meal","Type Here")
    Quality_of_food	 = st.text_input("Quality_of_food	","Type Here")
    Assessment	 = st.text_input("13.How frequently culture fests are organized in an year?	","Type Here")
    Region	 = st.text_input("14.How many field trips in a year?","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Levels, Environment, Competitive, Classes, Lab, Sports,
       Toilet, Sports_Competition, Students_per_class, Langugae,
       Timings, Meetings, Fests, Field_trips, Water, Mid_day_meal,
       Quality_of_food, Assessment, Region
       )
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
