


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
def predict_note_authentication(Unnamed0, Quality, Teacher_Quality, Books, Classroom,
       Food, Homework, Understanding_subs, Meetings, Continue_school):
    
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
   
    prediction=classifier.predict([[Unnamed0, Quality, Teacher_Quality, Books, Classroom,
       Food, Homework, Understanding_subs, Meetings, Continue_school]])
    print(prediction)
    return prediction



def main():
  
    st.title("Happyness Index Prediction System ml")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:#00FFFF;text-align:center;">Streamlit Happyness Index parent System using  ML App </h2>
    </div>
    <br><br>
    <div3>
    <img src="https://i.ibb.co/tbbcV31/0-4-BF6-h-Vx-RLO9-O-i-Q.jpg" alt="0-4-BF6-h-Vx-RLO9-O-i-Q" border="0" width="700" height="500">
    </div3>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Unnamed0 = st.text_input("Unnamed0","Type Here")
    Quality = st.text_input("1.How is the quality of education?","Type Here")
    Teacher_Quality = st.text_input("2.Are the teachers well educated?","Type Here")
    Books = st.text_input("3.Did the school management provide books on time?","Type Here")
    Classroom = st.text_input("How are the classrooms maintained?","Type Here")
    Food = st.text_input("5.How is the quality of the food?","Type Here")
    Homework= st.text_input("6.Is the school giving too much work to your child?","Type Here")
    Understanding_subs	 = st.text_input("7.Does your child feel comfortable in understanding the subjects?	","Type Here")
    Meetings = st.text_input(" 8.How often do they conduct Parent-Teacher meetings?	","Type Here")
    Continue_school= st.text_input(" 9.Would you like to join your child in the same school next year?","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Unnamed0, Quality, Teacher_Quality, Books, Classroom,
       Food, Homework, Understanding_subs, Meetings, Continue_school
       )
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
