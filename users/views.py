from django.db.models import Q
from rest_framework import views, status
from rest_framework.response import Response

from users.models import CustomUser, JWTToken
from users.serializers import SignInSerializers


class SignIn(views.APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        print(username, password)
        user = CustomUser.objects.filter(Q(username=username) | Q(email=username) & Q(is_active=True) & Q(status=1))
        try:
            if user.exists():
                user = user[0]
                if user.check_password(password):
                    jwttoken = JWTToken.objects.createToken(user=user)
                    print(jwttoken.token, user)
                    serializers = SignInSerializers(user)
                    data = serializers.data
                    data['token'] = jwttoken.token
                    return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(400, status=status.HTTP_400_BAD_REQUEST)
        return Response(202, status=status.HTTP_200_OK)
