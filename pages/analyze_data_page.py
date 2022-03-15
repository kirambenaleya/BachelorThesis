import streamlit as st
import pandas as pd


def display_analyze_data():
    disable_process_button = True
    st.header("Upload Your Dataset:")
    FILE_TYPES = ["csv"]
    uploaded_file = st.file_uploader(
        "Upload the file containing the student data. Only .csv files are accepted! "
        "Make sure to choose the right delimiter.",
        type=FILE_TYPES, accept_multiple_files=False)
    delimiter = st.radio(
        "How is your data delimited? Have a look at the preview below to make sure you selected the "
        "correct delimiter!", [';', ','])

    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        df = pd.read_csv(uploaded_file, sep=delimiter)
        st.write(df.head(10))
        with st.form(key='my_form'):
            if not df.empty:
                disable_process_button = False
            user_input = st.text_input(label='Enter a metric to analyze it: ')
            submit_button = st.form_submit_button(label='Enter')
        if user_input:
            key = user_input
            try:
                message = str(key + " distribution of your dataset.")
                st.subheader(message)
                key_distribution = pd.DataFrame(df[key].value_counts()).head(50)
                st.bar_chart(key_distribution)
            except KeyError:
                st.write("There is no key", key, "in your dataset. Make sure you chose the right delimiter "
                                                 "and you have checked the spelling.")