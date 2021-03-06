import matplotlib.pyplot as plt
import streamlit as st

from database_classes import Student
from database_functions import quiz_team_formation_is_answered, transform_schedule, add_team_formation_quiz_to_database, \
    sort_schedule, add_weights_to_database, is_survey_open, add_student_to_database, read_document_from_database, \
    add_points_to_database, add_participant
from helping_functions import none_all_or_weekdays, transform_ranking_to_weights, has_correct_form, locate_group, \
    condense_group, analyze_gad_igd
from pages.quizes.follow_up_survey import follow_up_survey
from pages.quizes.initial_feedback import initial_feedback


def display_team_formation_quiz(email, password):
    matriculation_id = st.text_input("Please enter your matriculation number (e.g. 17-939-083). Make sure to use the "
                                     "right format!")
    if matriculation_id:
        if has_correct_form(matriculation_id):
            st.markdown('##')
            col1, col2 = st.columns(2)
            col1.text('')
            col1.text('')
            col1.subheader("Please select your task")
            course = col2.selectbox('', ['None', 'CSCW FS 22', "CSCW FS 22 Initial Feedback",
                                         "CSCW FS 22 Follow-Up Feedback"])
            if course == 'None':
                st.text("Please select the survey you would like to answer.")
            elif course == 'CSCW FS 22' and is_survey_open(email, password) \
                    and not quiz_team_formation_is_answered(email, password, matriculation_id):
                st.markdown("##")
                st.subheader("Personal data")
                disable_submit = True
                col1, col2 = st.columns(2)
                col1.text('')
                col1.text('')
                col1.text("Please enter your first name.")
                first_name = col2.text_input("", key='first')
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text("Please enter your last name.")
                last_name = col2.text_input("", key='last')
                matriculation_number = matriculation_id
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text("Please select the gender option that\nbest describes you.")
                gender = col2.radio('', ['male', 'female', 'non binary'])
                col1.text('')
                col1.text('')
                col1.text("Please choose your current age.")
                age = col2.slider('', 16, 99)
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text("Are you currently enrolled in a\nbachelor or master program?")
                bachelor = col2.select_slider('', ['bachelor', 'master'])
                col1.text('')
                col1.text('')
                col1.text("Is this your first or second attempt\nat this course?")
                attempt = col2.select_slider('', ['first', 'second'])
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text("Is this course part of your major\nor minor?")
                major = col2.select_slider('', ['major', 'minor'])
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text("Do you have any prior experience\ncreating or editing videos?")
                experience = col2.select_slider('', ['no', 'yes'])
                col1.text('')
                col1.text('')
                col1.text(
                    "If you have a preferred teammate\nplease enter their\nmatriculation "
                    "number. (E.g. 17-939-083)")
                col1.markdown("**Important: This does not guarantee that\nyou will end up in the same team!**")
                teammate = col2.text_input("")
                if not teammate or not has_correct_form(teammate):
                    teammate = '0'

                st.markdown("##")
                st.subheader("Schedule")
                st.text(
                    "In the next step, we'd like to collect some information on your schedule. The\ntime slots "
                    "are meant to roughly indicate which days and times suit you best. If\nyou have no "
                    "preferences simply skip this section. Otherwise please discard the\ndefault value (by "
                    "clicking the small red x) and select ALL time slots that fit\nyour schedule. This step is "
                    "meant to simplify collaborative tasks. The algorithm\nwill try to consider your "
                    "schedule. However simply having a similar schedule to\nother students does not guarantee "
                    "that you will end up in the same group.")
                schedule_part1 = st.multiselect(
                    'I have time during the morning (roughly between 08.00 - 12.00) on:',
                    ['All', 'None', 'Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday',
                     'Sunday'], default=["All"])
                check_schedule_part1 = none_all_or_weekdays(schedule_part1)
                schedule_part2 = st.multiselect(
                    'I have time during the afternoon (roughly between 12.00 - 18.00) on:',
                    ['All', 'None', 'Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday',
                     'Sunday'], default=["All"])
                check_schedule_part2 = none_all_or_weekdays(schedule_part2)
                schedule_part3 = st.multiselect(
                    'I have time during the evening (roughly between 18.00 - 00.00) on:',
                    ['All', 'None', 'Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday',
                     'Sunday'], default=["All"])
                check_schedule_part3 = none_all_or_weekdays(schedule_part3)
                schedule_part1, schedule_part2, schedule_part3 = sort_schedule(schedule_part1, schedule_part2,
                                                                               schedule_part3)
                schedule = transform_schedule(schedule_part1, schedule_part2, schedule_part3)
                if not check_schedule_part1 or not check_schedule_part2 or not check_schedule_part3:
                    st.warning("Please check the schedule options you chose. If you chose None or All, "
                               "make sure no additional items are marked.")
                    disable_submit = True
                else:
                    disable_submit = False

                st.markdown("##")
                st.subheader("Personal preferences")
                st.text(
                    "This year, you have a voice in determining the weights the algorithm will apply\nfor each "
                    "of these criteria by indicating in the bottom of this quiz how important\nthese "
                    "criteria are for you.\n\nGive the criteria numerical weights based on importance. 1 - least "
                    "important,\n10 - most important. It is possible for different criteria to have\n"
                    "the same weight!")
                col1, col2 = st.columns(2)
                col1.text('')
                col1.text('')
                col1.text(
                    "Please rank the attribute GENDER based\non its importance to you regarding the\ngroup"
                    " formation process.")
                ranking_gender = col2.selectbox("", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key='ranking_gender')
                col1.text('')
                col1.text("Please rank the attribute AGE based on\nits importance to you regarding the\ngroup"
                          " formation process.")
                ranking_age = col2.selectbox("", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key='ranking_age')
                col1.text('')
                col2.text('')
                col2.text('')
                col1.text(
                    "Please rank the attribute EDUCATIONAL\nLEVEL (I.e. if you are a bachelor or\nmaster "
                    "student) based on its importance\nto you regarding the group formation\nprocess.")
                ranking_edu_level = col2.selectbox("", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key='ranking_edu_level')
                col1.text('')
                col2.text('')
                col2.text('')
                col2.text('')
                col1.text(
                    "Please rank the attribute MAJOR/MINOR\n(I.e. if this course is part of your\nmajor or "
                    "minor study program) based on\nits importance to you regarding the\ngroup formation "
                    "process.")
                ranking_major = col2.selectbox("", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key='ranking_major')
                col1.text('')
                col2.text('')
                col2.text('')
                col1.text(
                    "Please rank the attribute ATTEMPT (I.e.\nif this is your first or second attempt\nat "
                    "completing this course) based on its\nimportance to you regarding the group\nformation "
                    "process.")
                ranking_attempt = col2.selectbox("", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key='ranking_attempt')
                col1.text('')
                col2.text('')
                col2.text('')
                col2.text('')
                col1.text(
                    "Please rank the attribute TEAMMATE (I.e.\nthat you get to choose a teammate) based\non its"
                    "importance to you regarding the\ngroup formation process.")
                ranking_teammate = col2.selectbox("", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key='ranking_teammate')
                col1.text('')
                col2.text('')
                col2.text('')
                col1.text(
                    "Please rank the attribute EXPERIENCE\n(I.e. that your experience creating and\nediting"
                    "videos is considered) based on\nits importance to you regarding the\ngroup formation "
                    "process.")
                ranking_experience = col2.selectbox("", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key='ranking_experience')
                col1.text('')
                col2.text('')
                col2.text('')
                col2.text('')
                col1.text("Please rank the attribute SCHEDULE (I.e.\nyour schedule is considered) based on\nits"
                          "importance to you regarding the\ngroup formation process.")
                ranking_schedule = col2.selectbox("", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key='ranking_schedule')
                st.markdown("##")
                submit = st.checkbox('Submit', disabled=disable_submit)
                if submit:
                    student = \
                        Student(first_name, last_name, age, gender, bachelor, matriculation_number,
                                email).to_dict()
                    add_student_to_database(student, password, email, matriculation_id)
                    add_team_formation_quiz_to_database(first_name, last_name, age, experience, gender, bachelor,
                                                        major,
                                                        matriculation_number, teammate, schedule, email, attempt,
                                                        password,
                                                        matriculation_id)
                    weights, points = transform_ranking_to_weights(ranking_gender, ranking_age,
                                                                   ranking_experience,
                                                                   ranking_edu_level, ranking_major,
                                                                   ranking_attempt,
                                                                   ranking_teammate, ranking_schedule,
                                                                   matriculation_number)
                    add_weights_to_database(weights, password, email, matriculation_id)
                    add_points_to_database(points, password, email, matriculation_id)
                    add_participant(email, password, 'CSCW FS 22')
                    st.experimental_rerun()
            elif course == 'CSCW FS 22' and quiz_team_formation_is_answered(email, password, matriculation_id) \
                    and not is_survey_open(email, password):
                matriculation_number = matriculation_id
                group_configuration = read_document_from_database(email, password,
                                                                  collection=u'CSCW 22 GroupConfig',
                                                                  document='Test Config')
                group = locate_group(group_configuration, matriculation_number)
                if group:
                    st.markdown("##")
                    st.markdown("##")
                    message = 'Congratulations you are part of ' + group[0] + '!'
                    st.subheader(message)
                    amount_group_members = len(group[1]) - 1
                    message = 'The group you have been allocated to is made up of ' + \
                              "{}".format(amount_group_members) + ' people. Based on the weights\nselected by the ' \
                                                                  'teaching staff and the different dimensions ' \
                                                                  'considered your team\nis made up of: '
                    st.text(message)
                    group = condense_group(group[1])
                    teammate1, teammate1_data, teammate2, teammate2_data = None, None, None, None
                    teammate3, teammate3_data, teammate4, teammate4_data = None, None, None, None
                    data = None
                    for key, value in group.items():
                        if key == 'Team member 1':
                            teammate1 = value
                            teammate1_data = read_document_from_database(email, password, 'CSCW 22 Students',
                                                                         teammate1)
                        elif key == 'Team member 2':
                            teammate2 = value
                            teammate2_data = read_document_from_database(email, password, 'CSCW 22 Students',
                                                                         teammate2)
                        elif key == 'Team member 3':
                            teammate3 = value
                            teammate3_data = read_document_from_database(email, password, 'CSCW 22 Students',
                                                                         teammate3)
                        elif key == 'Team member 4':
                            teammate4 = value
                            teammate4_data = read_document_from_database(email, password, 'CSCW 22 Students',
                                                                         teammate4)
                        elif key == "Data":
                            data = value
                    if teammate1 and teammate1_data:
                        message = teammate1_data['First Name'] + " " + teammate1_data['Last Name'] + ", (" + \
                                  teammate1_data['Matriculation Number'].strip() + ", " + teammate1_data[
                                      'Email'] + ")"
                        st.text(message)
                    if teammate2 and teammate2_data:
                        message = teammate2_data['First Name'] + " " + teammate2_data['Last Name'] + ", (" + \
                                  teammate2_data['Matriculation Number'].strip() + ", " + teammate2_data[
                                      'Email'] + ")"
                        st.text(message)
                    if teammate3 and teammate3_data:
                        message = teammate3_data['First Name'] + " " + teammate3_data['Last Name'] + ", (" + \
                                  teammate3_data['Matriculation Number'].strip() + ", " + teammate3_data[
                                      'Email'] + ")"
                        st.text(message)
                    if teammate4 and teammate4_data:
                        message = teammate4_data['First Name'] + " " + teammate4_data['Last Name'] + ", (" + \
                                  teammate4_data['Matriculation Number'].strip() + ", " + teammate4_data[
                                      'Email'] + ")"
                        st.text(message)
                    if data:
                        st.markdown("##")
                        st.subheader("Why am I in this group?")
                        st.text("This tool incorporates personal preferences and assigns people into groups to\n"
                                "ensure diversity within the group and equality across groups.")
                        st.markdown("##")
                        st.subheader("How does my group compare to others?")
                        st.text("Group diversity score is calculated based on basic personal information such "
                                "as\ngender, study levels, major and skillset.")
                        message = 'Your group has an internal group distance of {:.2f}'.format(
                            data['igd']) + ' and a group average distance\nof {:.2f}.'.format(
                            data['gad']) + ' Below you can see two different visualizations of the distribution.'
                        st.text(message)

                    igd_list, gad_list = analyze_gad_igd(group_configuration)
                    if igd_list:
                        st.markdown("##")
                        x_coordinates = []

                        for index in range(len(group_configuration)):
                            x_coordinates.append(index + 1)
                        average_igd = sum(igd_list) / len(igd_list)
                        average_gad = sum(gad_list) / len(gad_list)

                        fig, ax = plt.subplots()
                        plt.hist(igd_list)
                        plt.xlabel("Internal Group Distance")
                        plt.axvline(average_igd, color='k', linestyle='-')
                        plt.axvline(data['igd'], color='r', linestyle='--')
                        plt.ylabel("Number of Groups")
                        plt.figlegend(['Average Group Diversity Score', 'Your Group Diversity Score'],
                                      loc='upper right')
                        st.pyplot(fig)

                        fig, ax = plt.subplots()
                        plt.hist(gad_list)
                        plt.xlabel("Group Average Distance")
                        plt.axvline(average_gad, color='k', linestyle='-')
                        plt.axvline(data['gad'], color='r', linestyle='--')
                        plt.ylabel("Number of Groups")
                        plt.figlegend(['Average GAD', 'Your Group-GAD'], loc='upper right')
                        st.pyplot(fig)
            elif course == 'CSCW FS 22' and not is_survey_open(email, password):
                st.markdown("##")
                st.warning("Sorry, this element is no longer available.")

            elif course == 'CSCW FS 22' and quiz_team_formation_is_answered(email, password, matriculation_id) \
                    and is_survey_open(email, password):
                st.warning("You have already participated in this survey.")

            elif course == "CSCW FS 22 Follow-Up Feedback":
                follow_up_survey(email, password, matriculation_id)
            elif course == "CSCW FS 22 Initial Feedback":
                if is_survey_open(email, password, document='CSCW FS 22 Initial Feedback'):
                    initial_feedback(email, password, matriculation_id)
                else:
                    st.warning("This survey has not been opened yet.")
        else:
            st.warning("Please make sure that you enter your matriculation number using the follwoing format: "
                       "xx-xxx-xxx")