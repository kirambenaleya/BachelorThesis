import streamlit as st

from database_classes import Feedback, InitialFeedback
from database_functions import add_feedback_to_database, add_initial_survey_to_database, \
    check_if_initial_survey_answered, add_participant


def initial_feedback(email, password, matriculation_id):
    if not check_if_initial_survey_answered(email, password, matriculation_id):
        assignment, importance, impact = None, None, None
        # TODO: Check if survey has already been answered and if it has, don't show it.
        # if not check_if_survey_answered(email, dictionary):
        st.markdown('##')
        st.subheader("Part One")
        st.text("")
        col1, col2 = st.columns(2)
        col1.text("")
        col1.text("")
        col1.text("I was satisfied with the team\nassigned to me.")
        col1.text("")
        satisfaction = col2.slider("1 = strongly disagree, 7 = strongly agree", 1, 7, key='satisfaction')
        col1.text("")
        col1.text("I am confident that my team will\nproduce a successful project outcome.")
        outcome = col2.slider("", 1, 7, key='outcome')
        col1.text("")
        col1.text("")
        col1.text("If you are given the option to request\na re-assignment of the teams, how\nlikely would you request for "
                  "a\nre-assignment?")
        reassignment = col2.slider("", 1, 7, key='reassignment')
        st.markdown('##')
        st.subheader("Part Two")
        col1, col2 = st.columns(2)
        col1.text('')
        col1.text('')
        col1.text(
            "What has been your experience with the\nteam-formation approach used in this\nhomework? ")
        experience = col2.slider('1 = very poor, 7 = excellent', 1, 7, key='experience')
        col1.text('')
        col1.text(
            "I would recommend repeating the approach\nto team formation I experienced in this\ncourse "
            "in the future.")
        recommendation = col2.slider('', 1, 7, key='recommendation')

        st.markdown("##")
        st.subheader("Part Three")
        col1, col2 = st.columns(2)
        col1.text('')
        col1.text('')
        col1.text("I consider the group formation process\nto be fair.")
        fairness = col2.slider("1 = very poor, 7 = excellent", 1, 7, key='fairness')
        col1.text('')
        col1.text('')
        col1.text('')
        col1.text('I have visibility into how the algorithm\ncreated groups.')
        visibility = col2.slider("", 1, 7, key='visibility')
        col1.text('')
        col1.text('')
        col1.text("I understand how the algorithm formed\ngroups. (E.g. which criteria was\nconsidered)")
        understanding = col2.slider("", 1, 7, key='understanding')
        col1.text('')
        col1.text('I think the team I was assigned to is\nequally capable to other teams at\n'
                  'tackling the creative challenge.')
        capability = col2.slider("", 1, 7, key='capability')
        col1.text('')
        col1.text("I think the team that was assigned to me\nis diverse.")
        diversity = col2.slider("", 1, 7, key='diversity')

        st.markdown("##")
        st.subheader("Part Four")
        col1, col2 = st.columns(2)
        col1.text('')
        col1.text('')
        col1.text("How easy (mentally) was it to use the\nalgorithmic team formation tool?")
        mental = col2.slider("1 = not at all, 7 = extremely", 1, 7, key='mental')
        col1.text('')
        col1.text('')
        col1.text('I feel that using the algorithmic team\nformation tool simplifies the process\nof finding a team.')
        simplicity = col2.slider("", 1, 7, key='simplicity')
        col1.text('')
        col1.text('')
        col1.text("What about the algorithmic team\nformation tool that delights you?")
        delight = col2.text_input("", key='delight')
        col1.text('')
        col1.text('')
        col1.text('What about the algorithmic team\nformation tool surprises you?')
        surprise = col2.text_input("", key='surprise')
        col1.text('')
        col1.text('')
        col1.text("What about the algorithmic team\nformation tool frustrates you?")
        frustration = col2.text_input("", key='frustration')
        col1.text('')
        col1.text('')
        col1.text("What functionality of the tool that\nyou have expected or hoped for\nis lacking?")
        lack = col2.text_input("", key='lack')
        col1.text('')
        col1.text("How do you think the tool can be better\ndesigned for you to adopt it in\nfuture courses?")
        design = col2.text_input("", key='design')

        st.markdown("##")
        st.subheader("Part Five")
        col1, col2 = st.columns(2)
        col1.text('')
        col1.text('')
        col1.text("Did you indicate a preferred teammate?")
        pref_teammate = col2.radio('', ['no', 'yes'], key='pref_teammate')
        if pref_teammate == 'yes':
            col1.text('')
            col1.text('')
            col1.text("Were you and your preferred teammate\nassigned into the same group? ")
            assignment = col2.radio('', ['yes', 'no'], key='assignment')
            col1.text('')
            col1.text('How important was it for you to have\nyour teammate preference fulfilled by\nthe algorithmic tool?')
            importance = col2.slider("1 = not at all, 7 = extremely", 1, 7, key='importance')
            col1.text('')
            col1.text("(How) Does the (un)fulfillment of the\nteammate preference impact your\nsatisfaction with the team "
                      "formation\ntool? Why?")
            impact = col2.text_input("", key='impact')

            st.markdown("##")
        st.subheader("Part Six")
        col1, col2 = st.columns(2)
        col1.text('')
        col1.text('')
        col1.text("I am satisfied with my team’s\ndiversity score.")
        diversity_score = col2.slider("1 = not at all, 7 = extremely", 1, 7, key='diversity_score')
        col1.text('')
        col1.text('')
        col1.text('How does the group diversity score\ninfluence your perception of the\nfairness regarding the '
                  'team formation?')
        influence = col2.text_input("", key='influence')
        col1.text('')
        col1.text("How do you think the group diversity\nscore will influence your team\nperformance and collaboration?")
        influence_grade = col2.text_input("", key='influence_grade')
        col1.text('')
        col1.text('How do you think the group diversity\nscore predicts the performance of your\nteam collaboration '
                  'and performance?')
        performance = col2.text_input("", key='performance')
        col1.text('')
        col1.text("To what extent and in what way do you\nthink your team grade will correlate\nwith your group’s "
                  "diversity score?")
        belief = col2.text_input("", key='belief')
        st.text('')
        if belief:
            st.text('Thanks for participating in this survey!')
            submit = st.checkbox('Submit', disabled=False)
            initial_survey = InitialFeedback(satisfaction, outcome, reassignment, experience, recommendation, fairness, visibility,
                                             understanding, capability, diversity, mental, simplicity, delight, surprise, frustration, lack,
                                             design, pref_teammate, assignment, importance, impact, diversity_score, influence, influence_grade,
                                             performance, belief, email)
            if submit:
                add_initial_survey_to_database(initial_survey, password, email, matriculation_id)
                add_participant(email, password, 'CSCW FS 22 Initial Feedback')
                st.success("Your answers have been saved. Thank you!")
                st.experimental_rerun()
    else:
        st.warning("You have already answered this survey. Thank you.")
