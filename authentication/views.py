# authentication/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from firebase.firebase import add_student_to_firestore
<<<<<<< HEAD
from .otp_service import send_otp, verify_otp, check_contact_exists
=======
>>>>>>> de2f632cfe500c70e678ba15635cf77120f31139

@csrf_exempt  # This is to bypass CSRF token validation for testing
def submit_student_form(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            # Parse JSON data from the request
            data = json.loads(request.body)
        else:
            # Handle form data (if sent as form data)
            data = {
                'name': request.POST.get('name'),
                'college_name': request.POST.get('college_name'),
                'dob': request.POST.get('dob'),
                'register_number': request.POST.get('register_number'),
                'disability_type': request.POST.get('disability_type'),
                'exam_mode': request.POST.get('exam_mode'),
                'contact_number': request.POST.get('contact_number'),
            }

<<<<<<< HEAD
        # Check if the contact number is already registered
        contact_number = data.get('contact_number')
        if check_contact_exists(contact_number):
            return JsonResponse({'status': 'error', 'message': 'Contact number already registered.'})

        # Send OTP to the contact number
        otp_response = send_otp(contact_number)
        if otp_response["status"] == "otp_sent":
            # Return OTP sent confirmation if everything goes well
            return JsonResponse({'status': 'otp_sent', 'message': 'OTP sent successfully to the contact number.'})
        
        return JsonResponse({'status': 'error', 'message': 'Failed to send OTP.'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

# authentication/views.py

from django.http import JsonResponse
from .otp_service import send_otp

@csrf_exempt  # This is to bypass CSRF token validation for testing
def send_otp_view(request):
    if request.method == 'POST':
        # Get the contact_number from the request (assuming JSON body)
        data = json.loads(request.body)
        contact_number = data.get('contact_number')

        if not contact_number:
            return JsonResponse({'status': 'error', 'message': 'Contact number is required.'}, status=400)

        # Call the function to send OTP
        otp_response = send_otp(contact_number)

        if otp_response["status"] == "otp_sent":
            return JsonResponse({'status': 'otp_sent', 'message': 'OTP sent successfully.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to send OTP.'}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method. Use POST.'}, status=405)

@csrf_exempt
def verify_otp_view(request):
    if request.method == 'POST':
        # Parse the incoming JSON data
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = {
                'contact_number': request.POST.get('contact_number'),
                'otp': request.POST.get('otp'),
            }

        # Check if the required fields are present
        contact_number = data.get('contact_number')
        entered_otp = data.get('otp')

        if not contact_number or not entered_otp:
            return JsonResponse({'status': 'error', 'message': 'Contact number and OTP are required.'})

        # Proceed with the OTP verification logic
        otp_verification_response = verify_otp(contact_number, entered_otp)

        if otp_verification_response['status'] == 'success':
            # OTP is correct, now add the student to Firestore
            add_student_to_firestore(data)
            return JsonResponse({'status': 'success', 'message': 'OTP verified and student added successfully.'})
        
        return JsonResponse(otp_verification_response)

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
=======
        # Process the data and add it to Firebase
        add_student_to_firestore(data)

        return JsonResponse({'message': 'Student added successfully'})

    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
>>>>>>> de2f632cfe500c70e678ba15635cf77120f31139
