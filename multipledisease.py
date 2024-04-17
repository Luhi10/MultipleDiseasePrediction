import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/hp\Desktop/project/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/hp\Desktop/project/saved models/heart_disease_model.sav','rb'))

parkinsonss_model = pickle.load(open('C:/Users/hp\Desktop/project/saved models/parkinsons_model.sav','rb'))

bc_model = pickle.load(open('C:/Users/hp\Desktop/project/saved models/cancer_model.sav','rb'))

#side Bar

with st.sidebar:
    selected = option_menu('Prediction Menu ',
                          
                          ['About','Diabetes Prediction',
                           'Heart Disease Prediction','Parkinsons Prediction','Breast Cancer Prediction'],
                          icons=['pen','activity','heart','person','gender-female'],
                          default_index=0)
    

# Define login and registration functions
def login():
    st.title("MULTIPLE DISEASE PREDICTION")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    register_button = st.button("Register")
    login_button = st.button("Login")

    if register_button:
        if not username or not password:
            st.error("Please fill in all fields.")
            return False
        st.session_state.user_credentials = {username: password}
        st.success("Registration successful! Please login.")

    if login_button:
        if username in st.session_state.user_credentials and st.session_state.user_credentials[username] == password:
            st.success(f"Welcome, {username}!")
            st.session_state.logged_in = True
            return True
        else:
            st.warning("Invalid username or password")
            return False

# Check if the user is logged in
if not st.session_state.get("logged_in"):
    if login():
        st.experimental_rerun()



# About Page

if st.session_state.get("logged_in") and selected == 'About':
    
    st.markdown("# ABOUT")


# Display introduction text

    st.write("""**WELCOME TO MULTIPLE DISEASE PREDICTION SYSTEM !**""")
    st.write(""" This is a Multiple Disease Prediction System where users can predict the likelihood of different diseases based on various input features.""")
    st.write("""This project addresses the need for accurate disease prediction using machine learning techniques, allowing for early detection and intervention.""")


# Accuracy data
    accuracy_data = {
    "Disease Name": ["Heart Disease", "Diabetes", "Parkinson's Disease", "Breast Cancer"],
    "Training Accuracy": [0.8512396694214877, 0.7833876221498371, 0.8717948717948718, 1.0],
    "Test Accuracy": [0.819672131147541, 0.7727272727272727, 0.8717948717948718, 0.956140350877193]
}

# Display Accuracy table
    st.write("**Accuracy Values:**")
    accuracy_df = pd.DataFrame(accuracy_data)
    st.table(accuracy_df)
 
# Display dataset links
    st.write("""
    **Dataset Links:**
    - [Diabetes Kaggle Dataset](https://www.kaggle.com/datasets/jhskaggle/diabetescsv)
    - [Heart Disease Kaggle Dataset](https://www.kaggle.com/datasets/arezaei81/heartcsv)
    - [Parkinson's Disease Kaggle Dataset](https://www.kaggle.com/datasets/sagarbapodara/parkinson-csv)
    - [Breast Cancer Kaggle Dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)""")


# Diabetes Prediction Page

elif st.session_state.get("logged_in") and selected == 'Diabetes Prediction':
    
#add title
    st.title('DIABETES PREDICTION')

    
# getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
# code for Prediction

    diab_diagnosis = ''
    
# creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    

# Heart Disease Prediction Page

if selected == 'Heart Disease Prediction':

    # page title
    
    st.title('HEART DISEASE PREDICTION')

# Getting the input data from the user

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

# code for Prediction
    
    heart_diagnosis = ''

# creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)    
   
    
   
    
# Parkinson's Prediction Page

elif st.session_state.get("logged_in") and selected == 'Parkinsons Prediction':
    
    # page title
    
    st.title('PARKINSONS PREDICTION')
    


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

# code for Prediction
    
    parkinsons_diagnosis = ''

# creating a button for Prediction    
    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsonss_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    
   # breastCancer Prediction Page
    
elif st.session_state.get("logged_in") and selected == 'Breast Cancer Prediction':
    st.title('BREAST CANCER PREDICTION')

# Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.text_input('Radius Mean')

    with col2:
        texture_mean = st.text_input('Texture Mean')

    with col3:
        perimeter_mean = st.text_input('Perimeter Mean')

    with col1:
        area_mean = st.text_input('Area Mean')

    with col2:
        smoothness_mean = st.text_input('Smoothness Mean')

    with col3:
        compactness_mean = st.text_input('Compactness Mean')

    with col1:
        concavity_mean = st.text_input('Concavity Mean')

    with col2:
        concave_points_mean = st.text_input('Concave Points Mean')

    with col3:
        symmetry_mean = st.text_input('Symmetry Mean')

    with col1:
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean')

    with col2:
        radius_se = st.text_input('Radius SE')

    with col3:
        texture_se = st.text_input('Texture SE')

    with col1:
        perimeter_se = st.text_input('Perimeter SE')

    with col2:
        area_se = st.text_input('Area SE')

    with col3:
        smoothness_se = st.text_input('Smoothness SE')

    with col1:
        compactness_se = st.text_input('Compactness SE')

    with col2:
        concavity_se = st.text_input('Concavity SE')

    with col3:
        concave_points_se = st.text_input('Concave Points SE')

    with col1:
        symmetry_se = st.text_input('Symmetry SE')

    with col2:
        fractal_dimension_se = st.text_input('Fractal Dimension SE')

    with col3:
        radius_worst = st.text_input('Radius Worst')

    with col1:
        texture_worst = st.text_input('Texture Worst')

    with col2:
        perimeter_worst = st.text_input('Perimeter Worst')

    with col3:
        area_worst = st.text_input('Area Worst')

    with col1:
        smoothness_worst = st.text_input('Smoothness Worst')

    with col2:
        compactness_worst = st.text_input('Compactness Worst')

    with col3:
        concavity_worst = st.text_input('Concavity Worst')

    with col1:
        concave_points_worst = st.text_input('Concave Points Worst')

    with col2:
        symmetry_worst = st.text_input('Symmetry Worst')

    with col3:
        fractal_dimension_worst = st.text_input('Fractal Dimension Worst')
        

    # Code for Prediction
    bc_diagnosis = ''
    

    # Creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        user_input = [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst,  concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]
        
        user_input = [float(x) for x in user_input]

        bc_prediction = bc_model.predict([user_input])

        if bc_prediction[0] == 1:
            bc_diagnosis = "The tumor is Malignant (Cancerous)."
        else:
            bc_diagnosis = "The tumor is Benign (Non-Cancerous)."

    st.success(bc_diagnosis)
    
    
#styling

def set_bg_from_url(url, opacity=1):
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem;">
                <b style="color: #004165;">Made by luhi M</b>
                &nbsp;
            </p>
        </div>
    </footer>
"""
    st.markdown(footer, unsafe_allow_html=True)

# Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
                color: black;
            }}
            h1, h2, h3, h4, h5, h6, .stTextInput > label, .stMarkdown > p, .stMarkdown > ul > li {{
                font-weight: bold;
                color: #004165; /* Dark blue */
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image from URL
set_bg_from_url("https://images.everydayhealth.com/homepage/health-topics-2.jpg?w=768", opacity=0.925)