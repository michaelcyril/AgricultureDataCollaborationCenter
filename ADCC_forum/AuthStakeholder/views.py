import json
import random

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *
from .serializers import *
from BeemAfrica import Authorize, AirTime, OTP, SMS


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def LoginUser(request):
    phone = request.data['phone'][1:]
    username = "255" + phone
    try:
        user = User.objects.get(username=username)
        us = User.objects.values('first_name', 'username').get(username=username)
        Authorize('478040a68e5f755d',
                  'ZTVkMzUwYWI5NjMwYjM2Zjc0ZTY1ZGQ5ZmQzZWNjNTMwYzRkOTEyYWRlODdhNWIxYmExYmQxOGZkMGNiODdiYg==')
        SMS.send_sms('Ndugu mkulima code yako ni' + " " + us['first_name'], us['username'])
        return Response({'continue': True})

    except User.DoesNotExist:
        print(request.data)
        type = request.data['type']
        code = str(random.randint(0, 999999))
        farmer = {'username': username, 'password': code, 'first_name': code, 'type': type}
        print(farmer)
        user = UserSerializer(data=farmer)
        if user.is_valid():
            user.save()
            us = User.objects.values('first_name', 'username').get(username=username)
            Authorize('478040a68e5f755d',
                      'ZTVkMzUwYWI5NjMwYjM2Zjc0ZTY1ZGQ5ZmQzZWNjNTMwYzRkOTEyYWRlODdhNWIxYmExYmQxOGZkMGNiODdiYg==')
            SMS.send_sms('Ndugu mkulima code yako ni' + " " + us['first_name'], us['username'])
            return Response({'continue': True})
        return Response({'continue': False})


# {"phone": "0693331836", "type":"farmer"}


@api_view(['POST'])
@permission_classes([AllowAny])
def RegisterUser(request):
    data = request.data
    user_type = data['type']
    if user_type == 'farmer':
        try:
            user = User.objects.get(username=data['username'])
            if user.is_active:
                return Response({'message': 'username already exists'})
        except User.DoesNotExist:
            # user = User.objects.create(username=data['username'], first_name=data['first_name'],
            #                            last_name=data['last_name'], phone=data['phone'], email=data['email'],
            #                            type=data['type'], password=data['password'])
            user = UserSerializer(data=request.data)
            if user.is_valid():
                user.save()
                return Response({'message': 'successful saved'})
            return Response({'message': 'failed to save'})
    elif user_type == 'admin':
        try:
            user = User.objects.get(username=data['username'])
            if user.is_active:
                return Response({'message': 'username already exists'})
        except User.DoesNotExist:
            # user = User.objects.create(username=data['username'], phone=data['phone'], email=data['email'],
            #                            type=data['type'], password=data['password'])
            user = UserSerializer(data=request.data)
            if user.is_valid():
                user.save()
                return Response({'message': 'successful saved'})
            return Response({'message': 'failed to save'})


# {
#     "username": "agriculture",
#     "phone": "0693331836",
#     "email": "michaelcyril71@gmail.com",
#     "type": "admin",
#     "password": "123"
# }


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateProfile(request):
    type = User.objects.values('type').get(username=request.user)['type']
    if type == 'admin':
        user_id = User.objects.get(username=request.user)
        data = request.data
        w_id = data['wilaya_id']
        wilaya_id = Wilaya.objects.get(id=w_id)
        profile = AdminProfile.objects.create(user_id=user_id, institute_logo=data['institute_logo'],
                                              institute=data['institute'], wilaya_id=wilaya_id, type=data['type'])
        profile.save()
        return Response({'message': 'successfully creating profile'})
    else:
        return Response({'message': 'You are not authorized to create admin profile'})


# {
#     "institute_logo": "image.png",
#     "institute": "Ofisi ya kilimo wilaya",
#     "wilaya_id": 1,
#     "type": "agriculture"
# }

# This view is used only when we need to save mikoa and wilaya
from mtaa import tanzania


@api_view(['GET'])
@permission_classes([AllowAny])
def MkoaWilaya(request):
    print(tanzania)
    mikoa = [entry for entry in tanzania]
    for i in range(0, len(mikoa) - 1):
        tosave = Mkoa.objects.create(name=mikoa[i])
        tosave.save()
    print("mikoa saved")
    mikoa_again = Mkoa.objects.values('id', 'name').all()
    mikoa_list = [entry for entry in mikoa_again]
    data = []
    for ml in mikoa_list:
        dist = tanzania.get(ml['name']).districts
        mk = Mkoa.objects.get(id=ml['id'])
        districtss = [entry for entry in dist]
        dataD = []
        for z in range(0, len(districtss)):
            d = districtss[z]
            w_tosave = Wilaya.objects.create(mkoa_id=mk, name=d)
            w_tosave.save()
            x = Wilaya.objects.values('id', 'name', 'mkoa_id').get(name=districtss[z])
            dataD.append(x)
        data.append({'id': ml['id'], 'name': ml['name'], 'districts': dataD})
        print("saved district of " + ml['name'])
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserDetails(request):
    user = User.objects.values('id', 'first_name', 'last_name', 'username', 'phone', 'email', 'type').get(
        username=request.user)
    us = User.objects.get(username=request.user)
    # profile = AdminProfile.objects.values('id', 'user_id', 'institute_logo', 'institute', 'wilaya_id', 'type').all()

    try:
        profile = AdminProfile.objects.values('id', 'user_id', 'institute_logo', 'institute', 'wilaya_id', 'type').get(
            user_id=us)
        print(profile)
        wilaya = Wilaya.objects.values('id', 'name', 'mkoa_id').get(id=profile['wilaya_id'])
        mkoa = Mkoa.objects.values('id', 'name').get(id=wilaya['mkoa_id'])
    except AdminProfile.DoesNotExist:
        pass
    try:
        context = {
            'user': user,
            'profile': profile,
            'location': {'mkoa': mkoa, 'wilaya': wilaya}
        }

    except NameError:
        context = {
            'user': user
        }

    return Response(context)
