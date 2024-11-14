# firebase_auth.py

import firebase_admin
from firebase_admin import firestore

# Function to verify student data from Firebase Firestore
def verify_student(register_number, dob):
    db = firestore.client()  # Initialize Firestore
    try:
        # Assuming you have a collection called 'students' in Firestore
        student_ref = db.collection('students').document(register_number)
        student = student_ref.get()
        if student.exists:
            student_data = student.to_dict()
            # Check if the DOB matches
            if student_data.get('dob') == dob:
                return True
    except Exception as e:
        print(f"Error fetching data: {e}")
    return False
