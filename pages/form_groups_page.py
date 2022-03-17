import pandas as pd
import streamlit as st

from AlgorithmTeamFormation.team_formation_algorithm import team_formation_algorithm
from database_functions import read_from_database, add_group_configuration, change_status_survey


@st.cache
def convert_df(data_frame):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return data_frame.to_csv(sep=',', index=0, index_label='index', encoding='utf-8-sig',
                             columns=['First Name', 'Last Name', 'Gender', 'Teammate', 'Age', 'Bachelor/Master',
                                      'Major/Minor', 'Attempt', 'Matriculation Number', 'Schedule', 'Experience'])


def display_form_groups(email, password):
    password_form_groups = st.text_input("Please enter your access code.", key='password_form_groups', type='password')
    if password_form_groups and password_form_groups == "AdminAccessCSCW2022":
        with st.expander('Open and close surveys.', expanded=False):
            st.markdown("##")
            open_close = st.radio('Would you like to open or close the survey?', ['open', 'close'])
            survey = st.text_input('Please enter the name of the survey.')
            st.markdown("##")
            send_data = st.checkbox('Submit')
            if send_data:
                change_status_survey(open_close, email, password, survey)
                text = str('The survey has been successfully ' + open_close + 'd.')
                st.success(text)
        with st.expander('Download the student data and display the computed weights.', expanded=False):
            data_students = read_from_database(email, password, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                                               collection=u'CSCW FS22 Answers')
            data_weights = read_from_database(email, password, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                                              collection=u'CSCW 22 Weights')
            data_points = read_from_database(email, password, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                                             collection=u'CSCW 22 Points')

            if data_students:
                df_students = pd.DataFrame(data_students)
                csv_students = convert_df(df_students)
                st.download_button(
                    label="Download student data as .csv",
                    data=csv_students,
                    file_name='students.csv',
                    mime='text/csv',
                )
            else:
                st.info("No student data is available yet.")

            # TODO: Display sum of all weights and decimals rounded off by 2
            if data_weights:
                pd.options.display.float_format = '{:.3f}'.format
                df1 = pd.DataFrame(data_weights)
                df2 = pd.DataFrame(data_points).select_dtypes(['number']).transpose()
                df1 = df1.mean(numeric_only=True).round(decimals=3).sort_index()
                df2 = df2.sum(axis=1, numeric_only=True).sort_index()
                df = pd.concat([df1, df2], axis=1)
                df = df.rename({df.columns[0]: 'Average Weights', df.columns[1]: 'Total Points'}, axis=1)
                df['Share'] = (df['Total Points'] / df['Total Points'].sum()).round(decimals=2)
                df['Share'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df['Share']], index=df.index)
                df = df.style.set_properties(**{'text-align': 'right'})
                st.header("Weights and Points Distribution")
                st.text("These are the average weights computed using the student data you gathered.")
                st.dataframe(df)
            else:
                st.info("No weights are currently available")

        with st.expander('Compute the group configuration', expanded=False):
            st.header("Group Formation")
            st.text("Please enter all relevant information. Please select the weights you would\nlike to use. The "
                    "higher the weight, the more important a dimension becomes.\nIf you don't select any weights the "
                    "following weights will be used [0.4, 0.3,\n0.1, 0.1, 0.1]. Once you have ensured that all "
                    "information is valid and you\nhave entered the absolute path of the file containing your "
                    "student data, you\nwill be able to select the delimiter and a button labeled 'process student "
                    "data'\nwill appear. Please take into consideration that only .csv files are "
                    "accepted\nas input files.")
            st.markdown("**IMPORTANT: The sum of all weights must be equal to 1.**")
            col1, col2 = st.columns(2)
            col1.text('')
            col1.text('')
            col1.text("Please choose the maximum number of\nstudents per group.")
            maximum_per_group = col2.slider("", 2, 10, key='maximum_per_group')
            col1.text('')
            col1.text('')
            col1.text("Please select the weight you would\nlike to assign to 'GENDER'.")
            weight_gender = col2.slider("", 0.00, 1.00, key='weight_gender')
            col1.text('')
            col1.text('')
            col1.text('')
            col1.text("Please select the weight you would\nlike to assign to 'EXPERIENCE'.")
            weight_experience = col2.slider("", 0.00, 1.00, key='weight_experience')
            col1.text('')
            col1.text('')
            col1.text("Please select the weight you would\nlike to assign to 'EDUCATIONAL LEVEL'.")
            col1.text('')
            col1.text('')
            col1.text('')
            weight_edu_level = col2.slider("", 0.00, 1.00, key='weight_edu_level')
            col1.text("Please select the weight you would\nlike to assign to 'MAJOR / MINOR'.")
            weight_major = col2.slider("", 0.00, 1.00, key='weight_major')
            col1.text('')
            col1.text('')
            col1.text("Please select the weight you would\nlike to assign to 'ATTEMPT'.")
            weight_attempt = col2.slider("", 0.00, 1.00, key='weight_attempt')
            st.markdown("##")

            disable_button = True
            path = st.text_input("Please enter the absolute path of the file containing the student data. ")
            if path:
                disable_button = False
                delimiter = st.radio("Please choose the correct delimiter.", [";", ","])
                process_button = st.button("Process student data", disabled=disable_button)
                if process_button:
                    if path[-4:] == ".csv":
                        if weight_experience == 0 and weight_attempt == 0 and weight_edu_level == 0 and \
                                weight_gender == 0 and weight_major == 0:
                            weights = None
                        else:
                            weights = [weight_gender, weight_experience, weight_edu_level, weight_major, weight_attempt]
                        group_config = team_formation_algorithm(delimiter, maximum_per_group, path, weights=weights)
                        add_group_configuration(group_config, password, email, 'Test Config')
                        st.success('The group configuration has been uploaded to the database and can now be viewed.')
                    else:
                        st.warning("Please ensure you are using a .csv file.")

    elif password_form_groups and password_form_groups != "AdminAccessCSCW2022":
        st.error("Incorrect password, please try again.")
