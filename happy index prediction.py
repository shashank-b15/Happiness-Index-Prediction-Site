

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/shash/happyness index prediction/student.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/shash/happyness index prediction/parent.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/shash/happyness index prediction/teacher.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Happy index prediction using ml',
                          
                          [ 'Home',
                            'student prediction',
                           'parent prediction',
                           'teacher prediction',
                            'describtion',
                            'chat graph'],
                          default_index=0)

# Diabetes Prediction Page
if (selected == 'Home'):
    
    # page title
    st.title('Home page')

    st.image("images (2).jpg")
    
  
    
# Diabetes Prediction Page
if (selected == 'student prediction'):
    
    # page title
    st.title('student prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Levels = st.text_input('Levels')
        
    with col2:
        Environment = st.text_input('Environment ')
    
    with col3:
        Competitive = st.text_input('Competitive')
    
    with col1:
        Classes	 = st.text_input('Classes')
    
    with col2:
        Lab = st.text_input('Lab ')
    
    with col3:
        Sports = st.text_input('Sports ')
    
    with col1:
        Toilet	 = st.text_input('Toilet')
    
    with col2:
        Sports_Competition = st.text_input('Sports_Competition')

    with col3:
        Students_per_class = st.text_input('Students_per_class')
    
    with col1:
        Langugae = st.text_input('Langugae')
    
    with col2:
        Timings	 = st.text_input('Timings')

    with col3:
        Meetings = st.text_input(' Meetings ')
    
    with col1:
        Fests		 = st.text_input(' Fests	')

    with col2:
        Field_trips  = st.text_input(' Field_trips  ')
    
    with col3:
        Water = st.text_input('Water')

    with col1:
        Mid_day_meal = st.text_input('Mid_day_meal')
    
    with col2:
        Quality_of_food	= st.text_input('Quality_of_food')
    
    with col3:
        Assessment = st.text_input('Assessment')

    with col1:
        Region = st.text_input(' Region')
    
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('student Result'):
        diab_prediction = diabetes_model.predict([[Levels, Environment, Competitive, Classes, Lab, Sports,
        Toilet, Sports_Competition, Students_per_class, Langugae,
        Timings, Meetings, Fests, Field_trips, Water, Mid_day_meal,
        Quality_of_food, Assessment, Region]])

        st.success('The output is {}'.format(diab_prediction ))
        
        
        
# Heart Disease Prediction Page
if (selected == 'parent prediction'):
    
    # page title
    st.title('parent prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Unnamed0 = st.text_input('Unnamed0')
        
    with col2:
        Quality = st.text_input('Quality ')
        
    with col3:
        Teacher_Quality = st.text_input('Teacher_Quality')
        
    with col1:
        Books = st.text_input('Books')
        
    with col2:
        Classroom	 = st.text_input('Classroom')
        
    with col3:
        Food = st.text_input('Food ')
        
    with col1:
        Homework = st.text_input('Homework')
        
    with col2:
        Understanding_subs = st.text_input('Understanding_subs')
        
    with col3:
        Meetings	 = st.text_input('Meetings')
        
    with col1:
        Continue_school = st.text_input('Continue_school')
        
    
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Parent Result'):
        heart_prediction = heart_disease_model.predict([[Unnamed0, Quality, Teacher_Quality, Books, Classroom,
        Food, Homework, Understanding_subs, Meetings, Continue_school,
       ]])                          
        
        
        st.success('The output is {}'.format(heart_prediction ))
    
    

# Parkinson's Prediction Page
if (selected == "teacher prediction"):
    
    # page title
    st.title("teacher prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        Salary	 = st.text_input('Salary')
        
    with col2:
        Learning = st.text_input(' Learning')
        
    with col3:
        Infra	 = st.text_input('Infra')
        
    with col4:
        Experience = st.text_input('Experience')
        
    with col5:
        School = st.text_input('School')
        
    with col1:
        Activity_based = st.text_input('Activity_based')
        
    with col2:
        English = st.text_input(' English')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Teacher result"):
        parkinsons_prediction = parkinsons_model.predict([[Salary, Learning, Infra, Experience, School, Activity_based,
        English]])                          
        
        st.success('The output is {}'.format(parkinsons_prediction ))

# describtion
if (selected == 'describtion'):
    
    # page title
    st.title('describtion')

# describtion
if (selected == 'chat graph'):
    
    # page title
    st.title('chat graph')

if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")




