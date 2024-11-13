# authentication/my_sms_service.py

def send_otp_sms(contact_number, otp):
    """
    Mock function to simulate sending an OTP via SMS.
    You can replace this with an actual API call to a service like Twilio, Nexmo, etc.
    """
    print(f"Sending OTP {otp} to {contact_number} via SMS...")
    # In real implementation, you'd call the SMS API here, like Twilio or Nexmo.
    return {"status": "success", "message": "OTP sent successfully."}
