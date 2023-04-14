

# ---- IMPORT LIBRARIES ----
import streamlit as st
import pandas as pd
import numpy as np
import requests
import pickle
from sklearn.preprocessing import MinMaxScaler
scal=MinMaxScaler()

# option menu
from streamlit_option_menu import option_menu # pip install streamlit-option-menu

# images
from PIL import Image

# animations
from streamlit_lottie import st_lottie  # pip install streamlit-lottie


# open the model
loaded_model=pickle.load(open("final_model.pickle","rb"))

# browser title
st.set_page_config(page_title="Heart Attack Prediction App", page_icon=":hearts:", layout="centered")





# ---- LOAD IMAGES & ANIMATIONS ----
# load images
img_info1 = Image.open("images/info1.png")
img_info2 = Image.open("images/info2.png")
img_info3 = Image.open("images/info3.png")
img_info4 = Image.open("images/info4.png")
img_info5 = Image.open("images/info5.png")


# load lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

anim_1 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_veki9s25.json")
anim_2 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_VOPQPpD9SV.json")






# ---- OPTION MENU ----
with st.sidebar:
    selected = option_menu("Menu", ["App",  "About This App", "About Me", 'Contact'], 
        icons=['activity', 'info-circle', 'file-person', 'envelope'], menu_icon="cast", default_index=0)
    st.write("---")


# 1) App Section

if selected == 'App':
    with st.container(): #a container is just for organizing the code
        col1, col2 = st.columns(2)
        with col1:
            st.title("Heart Attack Prediction App")
            st.caption("This Web-App aims to identify the heart attack risk for people, based on their medical attributes.")
            st.write("---")
        with col2:
            st.image(img_info4)


        # ---- PREDICTION ----
        #Creating a function for Prediction
        def heartdisease_prediction (input_data):
        # changing the input data to a numpy array
            numpy_data= np.asarray(input_data)
        #Reshaping the numpy array as we are predicting for only on instance
            input_reshaped = numpy_data.reshape (1,-1)
            prediction = loaded_model.predict (input_reshaped)
            if (prediction[0] == 0):
                st.success ("Great! The probability of having a heart attack is low. ✅")
            else:
                st.error("Warning❗ The probability of having a heart attack is high.")

        #Getting the input data from the user
        st.subheader('Please fill in the details and click on the button below.')
        age=st.selectbox ("Age",range(1,121,1))
        sex = st.radio("Gender", ('Male', 'Female'))
        cp = st.selectbox('Chest Pain Type',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic")) 
        trestbps=st.selectbox('Resting Blood Pressure',range(1,500,1))
        restecg=st.selectbox('Resting Electrocardiographic Results',("Nothing to note","ST-T Wave abnormality","Possible or definite left ventricular hypertrophy"))
        chol=st.selectbox('Cholesterol Level in mg/dl',range(1,1000,1))
        fbs=st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes','No'])
        thalach=st.selectbox('Maximum Heart Rate Achieved',range(1,300,1))
        exang=st.selectbox('Exercise Induced Angina',["Yes","No"])
        oldpeak=st.number_input('Oldpeak')
        slope = st.selectbox('Heart Rate slope',("Upsloping: better heart rate with excercise(uncommon)","Flatsloping: minimal change(typical healthy heart)","Downsloping: signs of unhealthy heart"))
        ca=st.selectbox('Number of Major Vessels Colored by Flourosopy',range(0,5,1))
        thal=st.selectbox('Thalium Stress Result',range(1,4,1))

        if sex=="male":
            sex=1 
        else:
            sex=0


        if cp=="Typical angina":
            cp=0
        elif cp=="Atypical angina":
            cp=1
        elif cp=="Non-anginal pain":
            cp=2
        elif cp=="Asymptomatic":
            cp=3


        if exang=="Yes":
            exang=1
        elif exang=="No":
            exang=0


        if fbs=="Yes":
            fbs=1
        elif fbs=="No":
            fbs=0


        if slope=="Upsloping: better heart rate with excercise(uncommon)":
            slope=0
        elif slope=="Flatsloping: minimal change(typical healthy heart)":
            slope=1
        elif slope=="Downsloping: signs of unhealthy heart":
            slope=2 


        if thal=="fixed defect: used to be defect but ok now":
            thal=2
        elif thal=="reversable defect: no proper blood movement when excercising":
            thal=3
        elif thal=="normal":
            thal=1

        if restecg=="Nothing to note":
            restecg=0
        elif restecg=="ST-T Wave abnormality":
            restecg=1
        elif restecg=="Possible or definite left ventricular hypertrophy":
            restecg=2

            

        # code for Prediction
        diagnosis = " "
        # creating a button for Prediction
        if st.button ("Prediction"):
            diagnosis=heartdisease_prediction ([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])


    



# 2) About This App Section

if selected == 'About This App':
    st.title("About This App")
    st.write("---")
    st.image(img_info1)
    st.write("---")
    st.subheader("Steps of this project")
    st.image(img_info5)
    st.write("---")
    st.subheader("The aim of this project")
    st.write("This machine learning project aims to identify people's heart attack risk, based on their medical attributes.")
    st.write("The prediction model has an accuracy of 93%.")
    st.write("---")
    st.subheader("Who is this app for?")
    st.write("The goal of the Web-App is to help healthcare providers calculate heart attack risk.")
    st.write("---")
    st.subheader("Disclaimer!")
    st.write("This App is not intended as a substitute for a medical consultation or clinical assessment!")
    st.write("It is intended to assist professionals and is not a guide to potentially dangerous self-medication.")






# 3) About Me Section

if selected == 'About Me':
    st.title("About Me")
    st.write("---")

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write('<p style="font-size:36px; color:black;">Hi, I am Gözde!</p>', unsafe_allow_html=True)
            st.write('<p style="font-size:26px; color:grey;">A Data Scientist / Data Analyst from Hamburg-Germany.</p>', unsafe_allow_html=True)

        with right_column:
            st_lottie(anim_2, height=180, key="coding")

    
    
    st.write("I graduated with a bachelor's degree in Statistics and have 3 years of work experience.")
    st.write("In my previous jobs, I was responsible for analyzing, interpreting and visualizing data. But I did not have any programming skills.")
    st.write("I've always had a strong passion for improving my coding skills using Python and SQL, and I achieved this after attending an intensive Data Science Bootcamp at WBS Coding School, Berlin, Germany.")
    st.write("I developed this application as part of the final project for the Data Science Bootcamp.")
    st.write("---")

    
# 4) Contact Form Section
if selected == 'Contact':
    st.title("Contact")
    st.write("---")
    st.write('<p style="font-size:26px; color:grey;">Connect with me:</p>', unsafe_allow_html=True)
    st.write("[LinkedIn](https://www.linkedin.com/in/gozdebarin/) | [Github](https://github.com/gozdebarin) | [Tableau](https://public.tableau.com/app/profile/gozdebarin) | [Medium](https://medium.com/@gozdebarin) ")

    st.write("---")
    st.write('<p style="font-size:18px; color:grey;">If you have any questions or feedback, please fill out the contact form.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:18px; color:grey;">I will get in touch with you as soon as possible!</p>', unsafe_allow_html=True)

    
    contact_form = """
    <form action="https://formsubmit.co/gozdemadendere@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email address" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
            
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/style.css")
         
    





# ---- SIDEBAR SECTION ----

# sidebar background color
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #CE5959;
    }
</style>
""", unsafe_allow_html=True)