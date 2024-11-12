from django.http import JsonResponse
from firebase.firebase import create_firebase_user, get_firebase_user



# Test Firebase connection by creating a user
def test_firebase_connection(request):
    # Replace with a test email and password
    email = 'testuser@example.com'
    password = 'TestPassword123'
    
    # Attempt to create a user in Firebase
    user = create_firebase_user(email, password)
    
    if isinstance(user, str):  # If an error occurred, return it
        return JsonResponse({'error': user}, status=400)
    else:
        return JsonResponse({'message': 'User created successfully!', 'uid': user.uid})
