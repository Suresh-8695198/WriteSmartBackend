import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase\\firebase-admin-sdk.json")
try:
    firebase_admin.get_app()
except ValueError:
    # Initialize the Firebase app only if it hasn't been initialized already
    firebase_admin.initialize_app(credentials.Certificate(cred), name='app1')

from firebase_admin import firestore


# Firestore client
db = firestore.client()
def add_student_to_firestore(student_data):
    """
    Add student data to Firestore
    :param student_data: Dictionary containing student data
    :return: Firestore document reference
    """
    student_ref = db.collection('students').add(student_data)
    return student_ref

def get_student_by_register_number(register_number):
    """
    Fetch student data by register number
    :param register_number: The student's register number
    :return: student data or None if not found
    """
    students_ref = db.collection('students')
    query = students_ref.where('register_number', '==', register_number).get()

    if query:
        return query[0].to_dict()
    return None
