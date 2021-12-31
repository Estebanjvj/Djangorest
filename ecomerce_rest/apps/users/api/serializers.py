from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # exclude

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    # Validación relacionada al nombre
    def validate_name(self, value):
        # custom validation
        if 'developer' in value:
            raise serializers.ValidationError('Error not develop')
        return value

    # Validación relacionada al correo
    def validate_email(self, value):
        # custom validate
        if value == '':
            raise serializers.ValidationError('No puede ir vacío')

        # if self.context['name'] in value:
        # if self.validate_name(self.context['name']) in value: # Forza la validacion de name para poder continuar con el código de abajo
        #     raise serializers.ValidationError('El email no puede contener el nombre')

        return value

    # validación no relacionada a ningun campo
    def validate(self, data):
        if data['name'] in data['email']:
            raise serializers.ValidationError('El email no puede contener el nombre')
        return data