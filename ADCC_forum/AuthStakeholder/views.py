from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *
from .serializers import *


# Create your views here.


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
