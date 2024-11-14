import random
import time
from google.cloud import firestore
from google.oauth2.service_account import Credentials  # Correct import for service account credentials
from .my_sms_service import send_otp_sms  # Replace with actual SMS service

# Explicitly load credentials
creds = Credentials.from_service_account_file(
    'firebase\\firebase-admin-sdk.json')  # Update the path to your service account file

# Initialize Firestore with the explicit credentials
db = firestore.Client(credentials=creds)

# Function to generate a 6-digit OTP
def generate_otp():
    return random.randint(100000, 999999)

# Function to check if the contact number is already registered in the database
def check_contact_exists(contact_number):
    # Query Firestore to check if the contact number already exists
    docs = db.collection('students').where('contact_number', '==', contact_number).stream()
    return any(docs)

# Function to send OTP and store it in Firestore temporarily
def send_otp(contact_number):
    otp = generate_otp()
    
    # Send OTP via SMS using your service (e.g., Twilio, Nexmo)
    send_otp_sms(contact_number, otp)  # Replace with actual SMS sending logic
    
    otp_data = {
        "otp": otp,
        "timestamp": int(time.time())  # Store timestamp when OTP was created
    }
    
    # Store OTP in Firestore with the contact number as the document ID
    db.collection('otp_verifications').document(contact_number).set(otp_data)
    return {"status": "otp_sent", "message": "OTP has been sent to the contact number."}

# Function to verify OTP entered by the user
def verify_otp(contact_number, entered_otp):
    otp_doc = db.collection('otp_verifications').document(contact_number).get()
    
    if not otp_doc.exists:
        return {"status": "error", "message": "OTP not found or expired."}

    otp_data = otp_doc.to_dict()
    
    # Check OTP expiration (e.g., valid for 5 minutes)
    if time.time() - otp_data["timestamp"] > 300:
        return {"status": "error", "message": "OTP expired."}

    # Verify OTP
    if otp_data["otp"] == int(entered_otp):
        # Clean up OTP after successful verification
        db.collection('otp_verifications').document(contact_number).delete()
        return {"status": "success", "message": "OTP verified successfully."}

    return {"status": "error", "message": "Incorrect OTP."}
