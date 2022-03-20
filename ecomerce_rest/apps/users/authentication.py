from datetime import timedelta, datetime
from django.utils import timezone
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.sessions.models import Session

class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds = 0)

    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            print('TOKEN EXpirado alv')
            return True
            # user = token.user # para volver a crear token
            '''token.delete()
            all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
            if all_sessions.exists():
                for sessions in all_sessions:
                    sessions_data = sessions.get_decoded()
                    if user.id == int(sessions_data.get('_auth_user_id')):
                        sessions.delete()'''
            # token = self.get_model().objects.create(user =user) # para volver a crear token
        return is_expired

    def authenticate_credentials(self, key):
        message,token, user = None, None, None
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user
        except self.get_model().DoesNotExist:
            # raise AuthenticationFailed('Token inválido.')
            message =  'Token inválido.'
        if token is not None:
            if not token.user.is_active:
                # raise AuthenticationFailed('Usuario no activo o eliminado.')
                message = 'Usuario no activo o eliminado.'
            is_expired = self.token_expire_handler(token)
            # print(is_expired)
            if is_expired:
                # raise AuthenticationFailed('Su token ha expirado.')
                message = 'Token expirado.'
                user = None
        return (user, token, message)