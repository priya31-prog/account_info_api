from rest_framework import serializers
from .models import AccountInfo, Address


class AccountInfoSerialize(serializers.ModelSerializer):
    user_name = serializers.CharField(source="userName")

    class Meta:
        model = AccountInfo
        fields = [
            "user_name",
            "userid",
            "phoneNumber",
            "profileImage",
            "email",
            "password",
        ]

        # DRF way of handling exception

    # def validate_userName(self, value):
    #     if AccountInfo.objects.filter(userName=value).exists():
    #         raise serializers.ValidationError("Username already exists")
    #     return value


class AddressSerialize(serializers.ModelSerializer):
    user_id = serializers.CharField(source="accountInfo_userid")

    class Meta:
        model = Address
        fields = [
            "user_id",
            "streetName",
            "addressLine1",
            "id",
            "pincode",
        ]
