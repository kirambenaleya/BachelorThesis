import json
import requests
import streamlit

from requests.exceptions import HTTPError
from google.oauth2.credentials import Credentials
from google.cloud.firestore import Client

from database_classes import Survey

FIREBASE_REST_API = "https://identitytoolkit.googleapis.com/v1/accounts"


def sign_in_with_email_and_password(api_key, email, password):
    request_url = "%s:signInWithPassword?key=%s" % (FIREBASE_REST_API, api_key)
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})

    req = requests.post(request_url, headers=headers, data=data)
    # Check for errors
    try:
        req.raise_for_status()
    except HTTPError as e:
        raise HTTPError(e, req.text)
    streamlit.session_state['idToken'] = req.json()['idToken']
    streamlit.session_state['refreshToken'] = req.json()['refreshToken']

    return req.json()


def check_for_creds(email, password, api_key):
    if streamlit.session_state['idToken'] and streamlit.session_state['refreshToken']:
        creds = Credentials(streamlit.session_state['idToken'], streamlit.session_state['refreshToken'])
        print("Creds used without logging in again.")
    else:
        response = sign_in_with_email_and_password(api_key, email, password)
        creds = Credentials(response['idToken'], response['refreshToken'])
    return creds


def add_team_formation_quiz_to_database(first_name, last_name, age, experience, gender, bachelor, major,
                                        matriculation_number,
                                        teammate, schedule, email, attempt, password, document,
                                        api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                                        collection=u'CSCW FS22 Answers'):
    creds = check_for_creds(email, password, api_key)

    # Use the raw firestore grpc client instead of building one through firebase_admin
    db = Client('bachelor-thesis-8464a', creds)

    # Et voila!
    # You are now connected to your firestore database and authenticated with the selected firebase user.
    # All your firestore security rules now apply on this connection and it will behave like a normal client
    survey = Survey(first_name, last_name, age, experience, gender, bachelor, major, matriculation_number, teammate,
                    schedule, email, attempt)

    db.collection(collection).document(document).set(survey.to_dict(), merge=True)


def add_weights_to_database(weights, password, email, document, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                            collection=u'CSCW 22 Weights'):
    creds = check_for_creds(email, password, api_key)
    db = Client('bachelor-thesis-8464a', creds)
    db.collection(collection).document(document).set(weights.to_dict(), merge=True)


def add_points_to_database(points, password, email, document, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                           collection=u'CSCW 22 Points'):
    creds = check_for_creds(email, password, api_key)
    db = Client('bachelor-thesis-8464a', creds)
    db.collection(collection).document(document).set(points.to_dict(), merge=True)


def add_initial_survey_to_database(initial_survey, password, email, document,
                                   api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                                   collection=u'CSCW FS 22 Initial Survey'):
    creds = check_for_creds(email, password, api_key)
    db = Client('bachelor-thesis-8464a', creds)
    db.collection(collection).document(document).set(initial_survey.to_dict(), merge=True)


def add_feedback_to_database(feedback, password, email, document, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                             collection=u'CSCW 22 Feedback'):
    creds = check_for_creds(email, password, api_key)
    db = Client('bachelor-thesis-8464a', creds)
    db.collection(collection).document(document).set(feedback.to_dict(), merge=True)


def add_peer_review_to_database(review, password, email, document, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                                collection=u'CSCW 22 Peer Review'):
    creds = check_for_creds(email, password, api_key)
    db = Client('bachelor-thesis-8464a', creds)
    db.collection(collection).document(document).set(review.to_dict(), merge=True)


def add_group_configuration(group_config, password, email, document, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                            collection=u'CSCW 22 GroupConfig'):
    creds = check_for_creds(email, password, api_key)
    db = Client('bachelor-thesis-8464a', creds)
    db.collection(collection).document(document).set(group_config, merge=True)


def add_student_to_database(student, password, email, document, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                            collection=u'CSCW 22 Students'):
    creds = check_for_creds(email, password, api_key)
    db = Client('bachelor-thesis-8464a', creds)
    db.collection(collection).document(document).set(student, merge=True)


def read_document_from_database(email, password, collection, document,
                                api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0'):
    creds = check_for_creds(email, password, api_key)

    # Use the raw firestore grpc client instead of building one through firebase_admin
    db = Client("bachelor-thesis-8464a", creds)

    # Et voila!
    # You are now connected to your firestore database and authenticated with the selected firebase user.
    # All your firestore security rules now apply on this connection and it will behave like a normal client

    doc_ref = db.collection(collection).document(document)

    doc = doc_ref.get()
    dictionary = doc.to_dict()
    if doc.exists:
        print(u'Document data has been returned!')
        return dictionary
    else:
        print(u'No such document!')
        return None


def read_from_database(email, password, collection, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0'):
    creds = check_for_creds(email, password, api_key)

    # Use the raw firestore grpc client instead of building one through firebase_admin
    db = Client("bachelor-thesis-8464a", creds)

    # Et voila!
    # You are now connected to your firestore database and authenticated with the selected firebase user.
    # All your firestore security rules now apply on this connection and it will behave like a normal client

    doc_ref = db.collection(collection)

    doc = doc_ref.get()
    list_of_dicts = []
    for document in doc:
        list_of_dicts.append(document.to_dict())
    if list_of_dicts:
        print(u'Document data has been returned!')
        return list_of_dicts
    else:
        print(u'No such document!')
        return None


def quiz_team_formation_is_answered(email, password, matriculation_id):
    data = read_document_from_database(email, password, collection=u'CSCW FS22 Answers', document=matriculation_id)
    if not data:
        return False
    else:
        return True


def add_participant(email, password, document):
    data = read_document_from_database(email, password, collection=u'Course Data',
                                       document=document)
    participants = 0
    if data:
        participants = data['participants']
    participants += 1
    creds = check_for_creds(email, password, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0')
    db = Client('bachelor-thesis-8464a', creds)
    db.collection(u'Course Data').document(document).set({'participants': participants}, merge=True)
    return None


def check_if_initial_survey_answered(email, password, matriculation_id):
    data = read_document_from_database(email, password, collection='CSCW FS 22 Initial Survey',
                                       document=matriculation_id)
    if not data:
        return False
    else:
        return True


def is_survey_open(email, password, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                   collection=u'Course Data', document=u'CSCW FS 22'):
    dictionary = read_document_from_database(email, password, api_key=api_key, collection=collection, document=document)
    if not dictionary:
        return False
    else:
        return dictionary['open']


def change_status_survey(open_close, email, password, document, api_key='AIzaSyCFtM8x4XgSRg1qTjMLLqgx380UGV_T9L0',
                         collection=u'Course Data'):
    creds = check_for_creds(email, password, api_key)
    db = Client('bachelor-thesis-8464a', creds)
    if open_close == 'open':
        open_close = True
    else:
        open_close = False
    db.collection(collection).document(document).set({'open': open_close}, merge=True)


def sort_schedule(schedule_part1, schedule_part2, schedule_part3):
    options = ['All', 'None', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if schedule_part1:
        schedule_part1 = sorted(schedule_part1, key=options.index)
    if schedule_part2:
        schedule_part2 = sorted(schedule_part2, key=options.index)
    if schedule_part3:
        schedule_part3 = sorted(schedule_part3, key=options.index)
    return schedule_part1, schedule_part2, schedule_part3


def transform_schedule(schedule_part1, schedule_part2, schedule_part3):
    schedule = ''
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    schedule_wip = schedule_part1 + schedule_part2 + schedule_part3
    for index, element in enumerate(schedule_wip[:-1]):
        if element == 'None':
            schedule += '-------'
        elif element == 'All':
            schedule += '+++++++'
        elif element != 'Monday' and (
                index == 0 or schedule_wip[index - 1] in ['All', 'None']):
            schedule += weekdays.index(schedule_wip[index]) * '-'
            schedule += '+'
            current_index = weekdays.index(schedule_wip[index])
            try:
                next_index = weekdays.index(schedule_wip[index + 1])
            except ValueError:
                next_index = 7
            if current_index >= next_index:
                difference = (6 - current_index) + next_index
            else:
                difference = (next_index - current_index) - 1
            schedule += difference * '-'
        else:
            schedule += '+'
            current_index = weekdays.index(schedule_wip[index])
            try:
                next_index = weekdays.index(schedule_wip[index + 1])
            except ValueError:
                next_index = 7
            if current_index >= next_index:
                difference = (6 - current_index) + next_index
            else:
                difference = (next_index - current_index) - 1
            schedule += difference * '-'
    if schedule_wip[-1] == 'None':
        schedule += '-------'
    elif schedule_wip[-1] == 'All':
        schedule += '+++++++'
    else:
        if len(schedule) <= 14:
            schedule += weekdays.index(schedule_wip[-1]) * '-'
        schedule += '+'
        difference = 6 - weekdays.index(schedule_wip[-1])
        schedule += difference * '-'
    return schedule
