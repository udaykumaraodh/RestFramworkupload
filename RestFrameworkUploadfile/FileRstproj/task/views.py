from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from task.models import UserFile,SingleUser
from task.serializers import UproSerializer,SingleSerializer
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import MultiPartRenderer,HTMLFormRenderer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET','POST'])
@authentication_classes([ JWTAuthentication])
@permission_classes([IsAuthenticated])
def upFiles(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            #um=UserFile.objects.all()
            id=request.user.id
            um=UserFile.objects.filter(user=id)

            print(um.values())
            ups=UproSerializer(um,many=True)

            print(ups.data)


            return Response(data=ups.data)

        if request.method=='POST':


            usr=request.user.id
            um=request.data


            um['user']=usr
            # print(img)
            # print(type(img))
            #
            # s1=str(img)
            # print(s1)
            # print(type(s1))

            # if ('jpg' in img) or ('jpeg' in img) or('png' in img)

            ups=UproSerializer(data=um)

            if ups.is_valid():
                print('hello')



                ups.save()
                return Response({'message':'Data created successfully...'})
            else:
                return Response(ups.errors)
        else:
            return Response({'message':'photo accepts only images'})



    else:
        return Response({'message':'No user logged in...'})



    #return None


@api_view(['GET','POST'])
#@renderer_classes([MultiPartRenderer,HTMLFormRenderer])
@parser_classes([MultiPartParser,FormParser])
@authentication_classes([ JWTAuthentication])
@permission_classes([IsAuthenticated])


def myFiles(request):

    if request.user.is_authenticated:

        if request.method == 'GET':
            #um=UserFile.objects.all()
            id=request.user.id
            su=SingleUser.objects.filter(user=id)

            print(su.values())
            print('----')
            si = SingleSerializer(su,many=True)

            print('$$')



            print('@@@')


            return JsonResponse(si.data,safe=False)



        if request.method=='POST':


            usr=request.user.id
            su=request.data
            multifile = request.FILES.getlist('docfiles')

            print(multifile)


            su['user']=usr

            #si=None



            for x in multifile:
                su['docfiles']=x



                print(su.values)

                si=SingleSerializer(data=su)

                if si.is_valid():
                    print('hello')
                    si.save()
                    print('saved')
                    message={'message':'Data created successfully...'}

                else:
                    message={'message':si.errors}

            return Response(message)


        # if request.method=='POST':
        #
        #
        #     usr=request.user.id
        #     su=request.data
        #     multifile = request.FILES.getlist('docfiles')
        #     # multifile=[x for x in request.FILES.dict().values()]
        #     print(multifile)
        #     #su.setlist('files',multifile)
        #
        #     su['user']=usr
        #     #su['docfiles']=multifile
        #
        #     si=SingleSerializer(data=su)
        #
        #     if si.is_valid():
        #         print('hello')
        #         si.save()
        #         return Response({'message':'Data created successfully...'})
        #     else:
        #         return Response(si.errors)
        #



    else:
        return Response({'message':'No user logged in...'})



