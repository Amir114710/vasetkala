from rest_framework import serializers

from account.models import User

class AccountSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField()
    password = serializers.CharField(required=False)

    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        password = validated_data['password']
        User.objects.get_or_create(phone_number=phone_number , password=password)
        user = User.objects.get(phone_number=phone_number)
        return user
    
    # def validate_username(self , value):
    #     for user in User.objects.all():
    #         if value == user.username:
    #             raise serializers.ValidationError('your username already existed')
    #     return value