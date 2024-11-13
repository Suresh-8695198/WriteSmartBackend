# authentication/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from firebase.firebase import add_student_to_firestore

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

        # Process the data and add it to Firebase
        add_student_to_firestore(data)

        return JsonResponse({'message': 'Student added successfully'})

    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
