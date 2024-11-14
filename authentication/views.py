from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .otp_service import send_otp, verify_otp, check_contact_exists
from firebase.firebase import add_student_to_firestore

@csrf_exempt  # This bypasses CSRF token validation for testing
def submit_student_form(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
    
    # Parse JSON or form data
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
    
    # Check for required fields
    contact_number = data.get('contact_number')
    if not contact_number:
        return JsonResponse({'status': 'error', 'message': 'Contact number is required.'}, status=400)

    # Verify if contact number already exists
    if check_contact_exists(contact_number):
        return JsonResponse({'status': 'error', 'message': 'Contact number already registered.'})

    # Send OTP to the contact number
    otp_response = send_otp(contact_number)
    if otp_response["status"] == "otp_sent":
        return JsonResponse({'status': 'otp_sent', 'message': 'OTP sent successfully to the contact number.'})
    
    return JsonResponse({'status': 'error', 'message': 'Failed to send OTP.'})

@csrf_exempt  # This bypasses CSRF token validation for testing
def send_otp_view(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method. Use POST.'}, status=405)

    # Parse JSON data
    data = json.loads(request.body)
    contact_number = data.get('contact_number')
    
    # Validate presence of contact number
    if not contact_number:
        return JsonResponse({'status': 'error', 'message': 'Contact number is required.'}, status=400)

    # Send OTP to contact number
    otp_response = send_otp(contact_number)
    if otp_response["status"] == "otp_sent":
        return JsonResponse({'status': 'otp_sent', 'message': 'OTP sent successfully.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Failed to send OTP.'}, status=500)

@csrf_exempt  # This bypasses CSRF token validation for testing
def verify_otp_view(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

    # Parse JSON or form data
    if request.content_type == 'application/json':
        data = json.loads(request.body)
    else:
        data = {
            'contact_number': request.POST.get('contact_number'),
            'otp': request.POST.get('otp'),
        }
    
    # Validate presence of contact number and OTP
    contact_number = data.get('contact_number')
    entered_otp = data.get('otp')
    if not contact_number or not entered_otp:
        return JsonResponse({'status': 'error', 'message': 'Contact number and OTP are required.'}, status=400)

    # Verify OTP
    otp_verification_response = verify_otp(contact_number, entered_otp)
    if otp_verification_response['status'] == 'success':
        # OTP verified; add student to Firestore
        add_student_to_firestore(data)
        return JsonResponse({'status': 'success', 'message': 'OTP verified and student added successfully.'})
    
    return JsonResponse(otp_verification_response)
