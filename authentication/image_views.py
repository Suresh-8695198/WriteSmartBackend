# authentication/image_views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ImageUploadSerializer
from cloudinary.uploader import upload
from cloudinary_storage.storage import MediaCloudinaryStorage

@api_view(['POST'])
def upload_student_image(request):
    if request.method == 'POST':
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            # Get the uploaded image file
            image_file = serializer.validated_data['image']
            try:
                # Upload the image to Cloudinary
                upload_response = upload(image_file)
                # Return the image URL from Cloudinary
                return Response({"image_url": upload_response['url']}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
