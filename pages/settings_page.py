import streamlit as st


def display_settings(db, user, storage):
    # Check for image
    n_image = db.child(user['localId']).child("Image").get().val()
    if n_image is not None:
        Image = db.child(user['localId']).child("Image").get()
        for img in Image.each():
            img_choice = img.val()
            # st.write(img_choice)
        st.image(img_choice)
        exp = st.expander('Change Bio and Image')
        with exp:
            newImgPath = st.text_input("Enter the full path of your profile picture")
            upload_new = st.button('Upload')
            if upload_new:
                uid = user['localId']
                fireb_upload = storage.child(uid).put(newImgPath, user['idToken'])
                a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
                db.child(user['localId']).child("Image").push(a_imgdata_url)
                st.success("Successfully updated!")
    else:
        st.info("No profile picture yet")
        newImgPath = st.text_input("Enter the full path of your profile picture")
        upload_new = st.button('Upload')
        if upload_new:
            uid = user['localId']
            fireb_upload = storage.child(uid).put(newImgPath, user['idToken'])
            a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
            db.child(user['localId']).child("Image").push(a_imgdata_url)
            st.success("Successfully updated!")
