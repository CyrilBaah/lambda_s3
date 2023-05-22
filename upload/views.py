import os
import boto3
from rest_framework.views import APIView
from rest_framework.response import Response
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

class FileUploadAPIView(APIView):
    def post(self, request, format=None):
        if request.FILES.get('file'):
            file = request.FILES['file']
            aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
            aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
            aws_bucket_name = os.getenv('AWS_BUCKET_NAME')
            aws_bucket_region = os.getenv('AWS_BUCKET_REGION')

            s3 = boto3.client(
                's3',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=aws_bucket_region
            )

            try:
                s3.upload_fileobj(file, aws_bucket_name, file.name)
                # The file is saved to the bucket with its original name
                return Response({'success': True, 'message': 'File uploaded successfully.'})
            except Exception as e:
                return Response({'success': False, 'message': str(e)})
        
        return Response({'success': False, 'message': 'Invalid request.'})
