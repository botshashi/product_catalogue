from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User
import jwt
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
@csrf_exempt
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Basic email validation
        if not email:
            return JsonResponse({'error': 'email cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                validate_email(email)
            except ValidationError:
                return JsonResponse({'error': 'Invalid email address.'}, status=status.HTTP_400_BAD_REQUEST)

        # Basic user validation
        if not username:
            return JsonResponse({'error': 'username cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        if not password:
            return JsonResponse({'error': 'password cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        if not first_name:
            return JsonResponse({'error': 'first_name cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Additional validation
            if User.objects.using('default').filter(email=email).exists():
                return JsonResponse({'error': 'Email is already in use.'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.using('default').filter(username=username).exists():
                return JsonResponse({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

            hashed_password = make_password(password)
            user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=hashed_password)
            user.save(using='default')
            return JsonResponse({'message': 'User successfully registered.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)

        if user and check_password(password, user.password):
            token = jwt.encode({'id': user.id}, settings.SECRET_KEY, algorithm='HS256')
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)