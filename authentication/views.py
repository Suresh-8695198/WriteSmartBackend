from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from firebase.firebase import add_student_to_firestore
from .otp_service import send_otp, verify_otp, check_contact_exists
from firebase.firebase import fetch_exam_questions

@csrf_exempt  # Bypass CSRF for testing (remove for production)
def submit_student_form(request):
    if request.method == 'POST':
        # Parse JSON data or form data based on the content type
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = {
                'name': request.POST.get('name'),
                'college_name': request.POST.get('college_name'),
                'dob': request.POST.get('dob'),
                'register_number': request.POST.get('register_number'),
                'disability_type': request.POST.get('disability_type'),
                'exam_mode': request.POST.get('exam_mode'),
                'contact_number': request.POST.get('contact_number'),
            }

        # Check if the contact number is already registered
        contact_number = data.get('contact_number')
        if check_contact_exists(contact_number):
            return JsonResponse({'status': 'error', 'message': 'Contact number already registered.'})

        # Send OTP to the contact number
        otp_response = send_otp(contact_number)
        if otp_response["status"] == "otp_sent":
            return JsonResponse({'status': 'otp_sent', 'message': 'OTP sent successfully to the contact number.'})
        
        return JsonResponse({'status': 'error', 'message': 'Failed to send OTP.'})

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt  # Bypass CSRF for testing (remove for production)
def send_otp_view(request):
    if request.method == 'POST':
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


@csrf_exempt  # Bypass CSRF for testing (remove for production)
def verify_otp_view(request):
    if request.method == 'POST':
        # Parse the incoming JSON data
        data = json.loads(request.body)

        # Check for required fields
        contact_number = data.get('contact_number')
        entered_otp = data.get('otp')

        if not contact_number or not entered_otp:
            return JsonResponse({'status': 'error', 'message': 'Contact number and OTP are required.'})

        # Proceed with OTP verification
        otp_verification_response = verify_otp(contact_number, entered_otp)

        if otp_verification_response['status'] == 'success':
            # OTP is correct, now add the student to Firestore
            add_student_to_firestore(data)
            return JsonResponse({'status': 'success', 'message': 'OTP verified and student added successfully.'})

        return JsonResponse(otp_verification_response)

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

# authentication/views.py


def get_exam_questions(request):
    try:
        # Fetch questions from Firebase
        questions = fetch_exam_questions()
        # Return questions in JSON format
        return JsonResponse({'status': 'success', 'data': questions}, status=200)
    except Exception as e:
        # Handle any errors
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
