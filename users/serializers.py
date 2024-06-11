from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


UserModel = get_user_model()


class ConfirmEmailSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=8)


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True, write_only=True)
    code = serializers.CharField(max_length=8)


class ConfirmPassword(serializers.Serializer):
    confirm_password = serializers.CharField(required=True, style={'input_type': 'password'})


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password], style={'input_type': 'password'})
    confirm_password = ConfirmPassword(write_only=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']['confirm_password']:
            print(data['confirm_password']['confirm_password'])
            raise serializers.ValidationError({"confirm_password": "Password and confirm password fields must match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username',  'phone_number', 'password', 'confirm_password', 'photo',
                  'birth_day', 'gender', 'affiliation')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'username', 'phone_number', 'date_joined', 'last_login', 'photo',
                  'birth_day', 'gender', 'affiliation')
        read_only_fields = ('date_joined', 'last_login')
        extra_kwargs = {
            'email': {'required': False},
        }