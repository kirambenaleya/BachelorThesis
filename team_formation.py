import json

import requests
import streamlit as st
import pyrebase

from pages.download_page import display_download_page
from pages.home_page import display_home
from pages.team_formation_quiz_page import display_team_formation_quiz
from pages.analyze_data_page import display_analyze_data
from pages.settings_page import display_settings
from pages.form_groups_page import display_form_groups


st.set_page_config(
    page_title="Algorithmic Team Formation Tool",
    page_icon="https://img.icons8.com/external-kiranshastry-lineal-kiranshastry/64/000000/external-robot-artificial"
              "-intelligence-kiranshastry-lineal-kiranshastry.png",
    layout="centered"
)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Configuration Key
firebaseConfig = {
    'apiKey': "AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0",
    'authDomain': "bachelor-thesis-8464a.firebaseapp.com",
    'projectId': "bachelor-thesis-8464a",
    'databaseURL': "https://bachelor-thesis-8464a-default-rtdb.europe-west1.firebasedatabase.app/",
    'storageBucket': "bachelor-thesis-8464a.appspot.com",
    'messagingSenderId': "787218054350",
    'appId': "1:787218054350:web:1a877a9a5948625cda249f",
    'measurementId': "G-CWQKBRDBCK"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()

st.sidebar.title("Team Formation Algorithm")

# Authentication
choice = st.sidebar.selectbox('Login/Signup', ['Login', 'Sign up'])

email = st.sidebar.text_input("Please enter your email address")
password = st.sidebar.text_input("Please enter your password", type='password')
user = None
if choice == 'Sign up':
    submit = st.sidebar.button("Create my account")

    if submit:
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("Your account has been successfully created!")
            st.balloons()
            db.child(user['localId']).child("ID").set('localId')
            st.title('Welcome!')
            st.info("Login by selecting login from the dropdown menu and entering your data.")
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            st.error(error)

if choice == "Login":
    login = st.sidebar.checkbox('Login / Logout')
    if login:
        try:
            user = auth.sign_in_with_email_and_password(email, password)

            # Save the Id-Token and the Refresh-Token to the session state
            st.session_state['idToken'] = user['idToken']
            st.session_state['refreshToken'] = user['refreshToken']
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            st.error(error)
    if user:
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

        bio = st.radio('Jump to', ['Home', 'Team Formation Quiz', 'Form Groups', 'Analyze Data', 'Download Code',
                                   'Settings'])

        if bio == 'Settings':
            display_settings(db, user, storage)

        elif bio == 'Home':
            display_home()

        elif bio == 'Form Groups':
            display_form_groups(email, password)

        elif bio == 'Analyze Data':
            display_analyze_data()

        elif bio == 'Team Formation Quiz':
            display_team_formation_quiz(email, password)

        elif bio == 'Download Code':
            display_download_page()
