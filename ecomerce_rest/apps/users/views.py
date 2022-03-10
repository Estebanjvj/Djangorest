from datetime import datetime
from django.contrib.sessions.models import Session

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView

from apps.users.api.serializers import UserTokenSerializer

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context= {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'user': user_serializer.data,
                        'token':token.key,
                        'msg': f'Bienvenido {user.name}'
                    }, status=status.HTTP_200_OK)
                else:
                    # Este código cierra todas las sesiones aunque no hayan sido abiertas con este código,
                    # Como el ADMIN de Django
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for sessions in all_sessions:
                            sessions_data = sessions.get_decoded()
                            if user.id == int(sessions_data.get('_auth_user_id')):
                                sessions.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'user': user_serializer.data,
                        'token': token.key,
                        'msg': f'Bienvenido nuevamente {user.name}'
                    }, status=status.HTTP_200_OK)

                    # Si quieres que cuando vuelva a intentar iniciar sesión lo vote:
                    #return Response({
                    #    'msg': f'El usuario: {user.name} ya ha iniciado sesión'
                    #}, status=status.HTTP_409_CONFLICT)
            else:
                return Response({'msg': f'{user} No está autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'msg': 'Nombre de usuario o contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):

    def get(self, request, *args, **kwargs):
        try:
            r_token = request.GET.get('token')
            token = Token.objects.filter(key = r_token).first()
            if token:
                user = token.user

                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for sessions in all_sessions:
                        sessions_data = sessions.get_decoded()
                        if user.id == int(sessions_data.get('_auth_user_id')):
                            sessions.delete()
                token.delete()

                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado.'
                return Response({
                    'msg': 'Sesión cerrada',
                    'token_message': token_message,
                    'session_message': session_message
                }, status=status.HTTP_200_OK)
            return Response({'msg': 'No se encontraron credenciales'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'msg': 'No se encontró token'}, status=status.HTTP_409_CONFLICT)