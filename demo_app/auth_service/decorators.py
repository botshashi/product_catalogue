
import jwt
from django.http import JsonResponse
from rest_framework import status
from django.conf import settings
from functools import wraps
from .models import User


# middleware to validate user authorization
def validate_jwt_token(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        token = request.headers.get('Authorization', None).split()[-1]

        if not token:
            return JsonResponse({'error': 'Authorization token not found.'}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('id', None)

            if user_id is not None:
                user = User.objects.using('default').get(user_id=user_id)
                request.user = user  # Attach the user object to the request for use in the view
                return view_func(request, *args, **kwargs)
            else:
                return JsonResponse({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    return _wrapped_view
