from rest_framework import serializers
from task.models import UserFile,SingleUser
from django.contrib.auth import get_user

class UproSerializer(serializers.ModelSerializer):


    class Meta:
        model=UserFile
        fields='__all__'



class SingleSerializer(serializers.ModelSerializer):
    class Meta:
        model=SingleUser
        fields=['user','docfiles']



        #fields=['photo','resume','idproof','user']




















    # def save(self):
    #     user =  self.context['request'].user
    #     print(user)


        # def get_uid(self, request):
        #     userid = self.request.user.id
        #     print(userid)
        #
        #     return userid
        #


# user=get_user
    # print(user)
    #
    # def __int__(self):
    #     user = self.context['request'].user
    #     print(user)