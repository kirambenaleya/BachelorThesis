from database_classes import Feedback, PeerReview, Demographics
import streamlit as st

from database_functions import is_survey_open, add_peer_review_to_database, add_participant, \
    check_if_survey_answered, add_follow_up_feedback_to_database, add_demographics_to_database


def follow_up_survey(email, password, matriculation_id):
    if is_survey_open(email, password, document='CSCW FS 22 Follow-Up Feedback'):
        if not check_if_survey_answered(email, password, matriculation_id, 'CSCW FS 22 Follow-Up Feedback'):
            recommendation_instead = None
            fairness_reason = None
            visibility_reason = None
            understanding_reason = None
            capability_reason = None
            diversity_reason = None
            st.markdown('##')
            st.subheader("Part One")
            st.text("")
            col1, col2 = st.columns(2)
            col1.text("")
            col1.text("")
            col1.text("I was satisfied with the team\nassigned to me.")
            col1.text("")
            satisfaction = col2.slider("1 = strongly disagree, 7 = strongly agree", 1, 7, 4, key='satisfaction')
            col1.text("")
            col1.text("I think my team has produced a\nsuccessful project outcome.")
            outcome = col2.slider("", 1, 7, 4, key='outcome')
            col1.text("")
            col1.text("Now that you have completed your\ncollaboration with the team assigned\nto you, how important "
                      "was it for you\nto have your teammate preference\nfulfilled by the algorithmic tool? ")
            col1.text("")
            fulfillment = col2.slider("1 = not at all, 7 = extremely important", 1, 7, 4, key='fulfillment')
            col1.text("")
            col1.text("Now that you have completed your\ncollaboration with the team assigned\nto you, how does the ("
                      "un)fulfillment\nof the teammate preference impact your\nsatisfaction with the team formation\n"
                      "tool? Why?")
            col1.text("")
            col2.text("")
            col2.text("")
            importance_fulfillment = col2.text_area("", key='importance_fulfillment')
            col1.text("")
            st.markdown('##')
            st.subheader("Part Two")
            col1, col2 = st.columns(2)
            col1.text('')
            col1.text('')
            col1.text(
                "What has been your experience with the\nteam-formation approach used in this\nhomework? ")
            experience = col2.slider('1 = very poor, 7 = excellent', 1, 7, 4, key='experience')
            col1.text('')
            col1.text(
                "I would recommend repeating the approach\nto team formation I experienced in this\ncourse "
                "in the future.")
            recommendation = col2.slider('', 1, 7, 4, key='recommendation')
            if recommendation <= 3:
                col1.text('')
                col1.text(
                    "What alternative (e.g. self selection,\ndiscussion forum, random allocation)\nwould you prefer and "
                    "why would you not\nrecommend repeating this approach?")
                recommendation_instead = col2.text_area("", key='recommendation_instead')

            st.markdown("##")
            st.subheader("Part Three")
            col1, col2 = st.columns(2)
            col1.text('')
            col1.text('')
            col1.text("I consider the group formation process\nto be fair.")
            fairness = col2.slider("1 = very poor, 7 = excellent", 1, 7, 4, key='fairness')
            if fairness <= 3:
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text("Please elaborate on why you think\nthe process was not fair.")
                fairness_reason = col2.text_area("", key='fairness_reason')
                col1.text('')
                col1.text('')
                st.text("")
                col1, col2 = st.columns(2)
            col1.text('')
            col1.text('')
            col1.text('')
            col1.text('I have visibility into how the algorithm\ncreated groups.')
            visibility = col2.slider("", 1, 7, 4, key='visibility')
            if visibility <= 3:
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text("How could this be improved?")
                visibility_reason = col2.text_area("", key='visibility_reason')
                col1.text('')
                col1.text('')
                col1.text('')
                st.text("")
                col1, col2 = st.columns(2)
            col1.text('')
            col1.text('')
            col1.text(
                "I understand how the algorithm formed\ngroups. (E.g. which criteria was\nconsidered)")
            understanding = col2.slider("", 1, 7, 4, key='understanding')
            if understanding <= 3:
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text("What didn’t you understand?\nHow can this be improved?")
                understanding_reason = col2.text_area("", key='understanding_reason')
                col1.text('')
                col1.text('')
                st.text("")
                col1, col2 = st.columns(2)
            col1.text('')
            col1.text('I think the team I was assigned to is\nequally capable at tackling the creative\n'
                      'challenge compared to other teams.')
            capability = col2.slider("", 1, 7, 4, key='capability')
            if capability <= 3:
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text("In which aspects do you think it\nwasn’t equal compared to other teams? ")
                capability_reason = col2.text_area("", key='capability_reason')
                col1.text('')
                col1.text('')
                col1.text('')
                st.text("")
                col1, col2 = st.columns(2)
            col1.text('')
            col1.text("I think the team that was assigned to me\nis diverse.")
            diversity = col2.slider("", 1, 7, 4, key='diversity')
            if diversity <= 3:
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text('')
                col1.text("In which aspects do you wish it to\nbe more diverse?  ")
                diversity_reason = col2.text_area("", key='diversity_reason')

            st.markdown("##")
            st.subheader("Part Four")
            col1, col2 = st.columns(2)
            col1.text('')
            col1.text('')
            col1.text("If you take into consideration that this\nis the first prototype of the algorithmic\nteam "
                      "formation tool and the focus doesn’t\nyet lie on the UI / usability, how would\nyou rate your "
                      "overall experience?")
            col2.text('')
            col2.text('')
            overall_prototype = col2.slider("1 = very poor, 7 = excellent", 1, 7, 4, key='overall_prototype')
            col1.text('')
            col2.text('')
            st.text("Which of the following improvements would have been helpful to you? (Select all\nthat apply)")
            improvements = st.multiselect("", ["A step-by-step guide in the user interface",
                                               "A step-by-step walk-through in form of a live demo",
                                               "Clearer specifications regarding the weights",
                                               "A personalized explanation on why and how you were grouped",
                                               "A clear explanation of how the teammate functionality works"],
                                          key='improvements')
            col1, col2 = st.columns(2)
            col1.text('')
            col1.text('')
            col1.text("Please note any further ideas you have\nto improve the tool")
            further_improvements = col2.text_area("", key='further_improvements')

            st.markdown("##")
            st.subheader("Part Five")
            st.text('')
            st.text('')
            st.text("Why aee you asking me this? - We'd like to assess team diversity.")
            col1, col2 = st.columns(2)
            col1.text('')
            col1.text('')
            col1.text('Are you a big picture or detail-oriented\nperson?')
            orientation = col2.select_slider("", ['big picture', 'detail'], key='orientation')
            col1.text('')
            col1.text('')
            col1.text('')
            col1.text('Are you a morning or evening person?')
            wake_up = col2.select_slider("", ['morning', 'evening'], key='wake_up')
            col1.text('')
            col1.text('')
            col1.text('')
            col1.text('')
            col1.text('What is your nationality?')
            nationality = col2.text_input("", key='nationality')
            col1.text('')
            col1.text('')
            col1.text('')
            col1.text('What is your leadership preference?')
            leader = col2.select_slider("", ['leader', 'follower'], key='leader')
            col1.text('')
            col1.text('')
            col1.text('')
            col1.text('')
            col2.text('')
            col1.text("How much effort are you willing to put\ninto this course? "
                      "\nDon't worry the professor will not see\nthis :)")
            effort = col2.slider("1 = none, 7 = as much as possible", 1, 7, 4, key='effort')
            col1.text('')
            col1.text('')
            col1.text('')
            col2.text('')
            col1.text("How good is your english?")
            english = col2.slider("1 = poor, 7 = proficient", 1, 7, 4, key='english')
            col1.text('')
            col1.text('')
            col1.text('')
            col1.text("How good is your german?")
            german = col2.slider("", 1, 7, 4, key='german')

            st.markdown("##")
            st.subheader("Peer Review")
            st.text(
                "This evaluation will be totally anonymous and results will not be shared directly\nwith any members "
                "of your team.")
            col1, col2 = st.columns(2)
            col1.text('')
            col1.text('')
            col1.text("Please enter the full name (e.g. Max\nMusterman) of the first member.")
            name_teammate1 = col2.text_input('Teammate Number 1', key='name_teammate1')
            col1.text('')
            col1.text('')
            col1.text("Please rate their performance and\nthe workload distribution.")
            performance_teammate1 = col2.slider('', 1, 7, 4, key='performance_teammate1')

            col1.text('')
            col1.text('')
            col1.text('')
            col1.text("Please enter the full name of the\nsecond member.")
            name_teammate2 = col2.text_input('Teammate Number 2', key='name_teammate2')
            col1.text('')
            col1.text('')
            col1.text("Please rate their performance and\nthe workload distribution.")
            performance_teammate2 = col2.slider('', 1, 7, 4, key='performance_teammate2')

            col1.text('')
            col1.text('')
            col1.text('')
            col1.text("Please enter the full name of the\nthird member.")
            name_teammate3 = col2.text_input('Teammate Number 3', key='name_teammate3')
            col1.text('')
            col1.text('')
            col1.text("Please rate their performance and\nthe workload distribution.")
            performance_teammate3 = col2.slider('', 1, 7, 4, key='performance_teammate3')

            col1.text('')
            col1.text('')
            col1.text("IF your team had four members,\nplease enter the full name of the\nfourth member.")
            name_teammate4 = col2.text_input('Teammate Number 4', key='name_teammate4')
            col1.text('')
            col1.text("Please rate their performance and\nthe workload distribution.")
            performance_teammate4 = col2.slider('', 1, 7, 4, key='performance_teammate4')
            st.markdown("##")
            if name_teammate1 and performance_teammate1 and name_teammate2 and performance_teammate2 and name_teammate3 \
                    and performance_teammate3:
                submit = st.checkbox('Submit', disabled=False)
                if submit:
                    feedback = Feedback(satisfaction, outcome, experience, recommendation, fairness, visibility,
                                        understanding, capability, diversity, fulfillment, importance_fulfillment,
                                        recommendation_instead,
                                        fairness_reason, visibility_reason, understanding_reason, capability_reason,
                                        diversity_reason,
                                        overall_prototype, improvements, further_improvements)
                    peer_review = PeerReview(name_teammate1, performance_teammate1, name_teammate2,
                                             performance_teammate2,
                                             name_teammate3, performance_teammate3, name_teammate4,
                                             performance_teammate4,
                                             email)
                    demographics = Demographics(orientation, wake_up, nationality, leader, effort, english,
                                                german)
                    add_demographics_to_database(demographics, password, email, matriculation_id)
                    add_follow_up_feedback_to_database(feedback, password, email, matriculation_id)
                    add_peer_review_to_database(peer_review, password, email, matriculation_id)
                    add_participant(email, password, 'CSCW FS 22 Follow-Up Feedback')
                    st.experimental_rerun()
        elif check_if_survey_answered(email, password, matriculation_id, 'CSCW FS 22 Follow-Up Feedback'):
            st.success("Thank you for participating in this survey!")
    else:
        st.warning("This survey has not been opened yet.")
