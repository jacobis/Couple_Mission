from django.contrib.auth.models import User
from django.core.validators import validate_email

from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    email = serializers.Field(source='username')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def validate_email(self, attrs, source):
        value = attrs[source]
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is exists")
        else:
            try:
                validate_email(value)
            except:
                raise serializers.ValidationError("Email is not normal")   

        return attrs