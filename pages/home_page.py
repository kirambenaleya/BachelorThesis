import streamlit as st


def display_home():
    st.header("Team Formation Algorithm")
    st.subheader("_developed by Eva Yiwei Wu & Kiram Ben Aleya_")

    st.subheader("What is the aim of this project?")

    st.text(
        "In this project we aim to develop a machine learning algorithm enabling a fair team\nallocation "
        "within a university setting. The algorithm has been based on XYZ and the\ndevelopment followed a "
        "value sensitive design approach proposed by XYZ.")

    st.subheader("How does our algorithm work?")

    st.text(
        "Input-values were determined in collaboration with our main stakeholders, the\nstudents themselves. "
        "Literature on team formation and algorithmic team allocation\nwas reviewed. In addition to the "
        "input-variables we also focus on transparency,\nwhich is why the entire code can be downloaded at: "
        "www.xyz.xyz. We also want the\nstudents to participate in the process by assigning different weights "
        "they consider\nappropriate to the input values. Students also have the possibility of choosing "
        "a\nteammate. In order to prevent cheating students can only choose a single teammate.\nFor the "
        "algorithm to consider your choice it must be reciprocal (meaning your\nteammate must also choose you).")
