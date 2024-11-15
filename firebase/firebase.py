import firebase_admin
from firebase_admin import credentials, firestore


# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase\\firebase-admin-sdk.json")
try:
    firebase_admin.get_app()
except ValueError:
    # Initialize the Firebase app only if it hasn't been initialized already
    firebase_admin.initialize_app(credentials.Certificate(cred), name='app1')
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
# firebase/firebase.py

# Initialize Firebase app
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase\\firebase-admin-sdk.json")
    firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Function to fetch exam questions from Firestore
def fetch_exam_questions():
    questions = []
    # Reference to the Firestore collection where exam questions are stored
    questions_ref = db.collection('exam_questions')
    docs = questions_ref.stream()

    # Loop through documents in the collection
    for doc in docs:
        question_data = doc.to_dict()
        questions.append({
            'id': doc.id,
            'question': question_data.get('question', ''),
            'marks': question_data.get('marks', 0),
            'type': question_data.get('type', 'written')
        })
    
    return questions



def update_exam_answer(doc_id, answer):
    """
    Update the answer for a specific question in Firestore.
    """
    try:
        question_ref = db.collection('exam_questions').document(doc_id)
        
        # Check if the document exists
        if not question_ref.get().exists:
            raise ValueError(f"No document found with ID: {doc_id}")
        
        # Update the document with the answer field
        question_ref.update({'answer': answer})
        print(f"Answer successfully updated for doc_id: {doc_id}")
    except Exception as e:
        print(f"Error in update_exam_answer: {e}")
        raise


