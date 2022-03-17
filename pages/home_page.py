import streamlit as st


def display_home():
    st.header("Home Page")
    st.markdown("**Team Formation Tool, developed by Eva Yiwei Wu & Kiram Ben Aleya**")
    st.markdown("##")
    st.subheader("Why?")

    st.text("You may ask yourself why we are using an automated tool to form groups? Automated\ngroup formation "
            "ensures that everyone finds a group without stress, no matter how\nlong they have been at the university."
            " We can ensure that diverse skill sets and\nsubject expertise are present in each group. Further, you "
            "have the option to get\nto meet new people as well as teaming up with a best friend by selecting "
            "each\nother in the tool.")

    st.markdown("##")
    st.subheader("Privacy")

    st.text( "A note on privacy: we will only use your info to match you in groups, that’s it.\nThe professor cannot "
             "see your answers. Survey answers weill be anonymised and\ntreated with the upmost care. Further, (seen as"
             "this is only a prototype) any\npersonal data will be deleted 1 month after filling out the surveys.")

    st.markdown("##")
    st.subheader("Quiz")

    st.text("This tool considers basic personal information and personal preferences to match\nyou with your "
            "dream team. These group matching criteria are determined based on\nthe suggestions from your fellow "
            "students who took this class last year. The top\nmatching criteria they indicated are:\n\n"
            "1. Gender\n2. Preferred Teammate\n3. Age\n4. Educational Level\n5. Schedule\n6. Skill-set \n"
            "7. Major/Minor\n8. Experience: first/second attempt of the module")

    st.markdown("##")
    st.markdown("**Let’s start the team formation quiz by clicking on the button on the top\nof the page!**")