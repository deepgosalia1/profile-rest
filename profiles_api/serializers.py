from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Ser. a name field, for testing the API Post"""
    name =  serializers.CharField(max_length = 10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password' : {
                'write_only':True, # cannot be read by any get/post request
                'style':{ 'input_type':'password' }
            }
        }
    
    def create(self, validated_data):
        """ OVerriding model serializer's original create with our own create function
            as we want password to be displayed and stored cryptically and not in plain text"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}, 'created_on':{'read_only':True}}