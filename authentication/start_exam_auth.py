# start_exam_auth.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import StudentLoginSerializer
from .firebase_auth import verify_student  # Import the Firebase verification function

@api_view(['POST'])
def start_exam_authentication(request):
    serializer = StudentLoginSerializer(data=request.data)
    if serializer.is_valid():
        register_number = serializer.validated_data['register_number']
        dob = serializer.validated_data['dob']

        # Use Firebase function to verify student data
        if verify_student(register_number, dob):
            return Response({"message": "Authentication successful. Start the exam!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid register number or date of birth."}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
