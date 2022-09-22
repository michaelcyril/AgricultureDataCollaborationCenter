from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *
from .serializers import *
from AuthStakeholder.models import User, Mkoa, Wilaya, AdminProfile


# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PostSoilView(request):
    admin_type = AdminProfile.objects.values('type').get(
        user_id=User.objects.get(username=request.user))['type']
    if admin_type == 'soil':
        user = User.objects.get(username=request.user)
        name = Soi.objects.get(id=request.data['soil_id'])
        wilaya = Wilaya.objects.get(id=request.data['wilaya_id'])
        images = request.data['images']
        soil_tosave = Soil.objects.create(name=name, wilaya_id=wilaya, created_by=user)
        soil_tosave.save()
        saved = Soil.objects.values('id').all
        soil = [entry for entry in saved]
        s1 = []
        for s in soil:
            s1.append(s['id'])
        saved_id = max(s1)
        a_soil = Soil.objects.get(id=saved_id)
        for img in images:
            imageSave = SoilImage.objects.create(image=img['image'], soil_id=a_soil)
            imageSave.save()
        return Response({'message': 'Soil successful saved'})
    return Response({'message': 'The user is not responsible to save this data'})


# {
#     "soil_id": 1,
#     "wilaya_id": 1,
#     "images": [{"image": "image2.png"}, {"image": "image3.png"}]
# }


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PostProductView(request):
    admin_type = AdminProfile.objects.values('type').get(
        user_id=User.objects.get(username=request.user))['type']
    if admin_type == 'agriculture':
        user = User.objects.get(username=request.user)
        name = Prod.objects.get(id=request.data['product_id'])
        wilaya = Wilaya.objects.get(id=request.data['wilaya_id'])
        images = request.data['images']
        product_tosave = Product.objects.create(name=name, wilaya_id=wilaya, created_by=user)
        product_tosave.save()
        saved = Product.objects.values('id').all
        product = [entry for entry in saved]
        p1 = []
        for s in product:
            p1.append(s['id'])
        saved_id = max(p1)
        a_product = Product.objects.get(id=saved_id)
        for img in images:
            imageSave = ProductImage.objects.create(image=img['image'], product_id=a_product)
            imageSave.save()
        return Response({'message': 'Product successful saved'})
    return Response({'message': 'The user is not responsible to save this data'})


# {
#     "product_id": 1,
#     "wilaya_id": 1,
#     "images": [{"image": "image2.png"}, {"image": "image3.png"}]
# }


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PostDeseaseView(request):
    admin_type = AdminProfile.objects.values('type').get(
        user_id=User.objects.get(username=request.user))['type']
    if admin_type == 'agriculture':
        user = User.objects.get(username=request.user)
        name = request.data['name']
        wilaya = Wilaya.objects.get(id=request.data['wilaya_id'])
        images = request.data['images']
        desease_tosave = Desease.objects.create(name=name, wilaya_id=wilaya, created_by=user)
        desease_tosave.save()
        saved = Desease.objects.values('id').all
        desease = [entry for entry in saved]
        d1 = []
        for s in desease:
            d1.append(s['id'])
        saved_id = max(d1)
        a_desease = Desease.objects.get(id=saved_id)
        for img in images:
            imageSave = SoilImage.objects.create(image=img['image'], desease_id=a_desease)
            imageSave.save()
        return Response({'message': 'Desease successful saved'})
    return Response({'message': 'The user is not responsible to save this data'})


# {
#     "name": "pestcide",
#     "wilaya_id": 1,
#     "images": [{"image": "image2.png"}, {"image": "image3.png"}]
# }


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def homeView(requests):
    mikoa = Mkoa.objects.values('id', 'name').all()
    data = [entry for entry in mikoa]
    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def getWilayaWithInfo(request):
    wilaya = Wilaya.objects.values('id', 'name', 'mkoa_id').filter(mkoa_id=request.data['id'])
    data = [entry for entry in wilaya]
    print(data)
    details = []
    for dat in data:
        info = []
        w_id = dat['id']
        print(w_id)
        # for disease
        try:
            des = Desease.objects.values('id', 'name', 'created_by', 'created_at').filter(wilaya_id=w_id)
            # print('for wilaya_id'+w_id+"  "+str(des))
            desease = [entry for entry in des]
            # print(desease)
            if len(desease) > 1:
                # des_id = desease[0]['id']
                desease1 = []
                for des1 in desease:
                    images = DeseaseImage.objects.values('id', 'image').filter(desease_id=des1['id'])
                    h = {'desease': des1, 'images': [entry for entry in images]}
                    desease1.append(h)
                    print(desease1)

                d = {'name': 'magonjwa', 'list': desease1}
            elif len(desease) == 1:
                images = DeseaseImage.objects.values('id', 'image').filter(desease_id=desease[0]['id'])
                desease1 = [{'desease': desease[0], 'images': [entry for entry in images]}]
                d = {'name': 'magonjwa', 'list': desease1}
                print(desease1)

            elif len(desease) == 0:
                pass

            try:
                print(d)
                info.append(d)
            except NameError:
                pass

        except Desease.DoesNotExist:
            pass

        d1 = {'wilaya': dat['name'], 'info': info}
        details.append(d1)
        # print(info)
    return Response(details)


# {"id":1}

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get


# you provide soil id and get the mikoa and wilaya which soil found
@api_view(['POST'])
@permission_classes([AllowAny])
def soilToWilaya(request):
    soil_id = request.data['id']
    soil_wilaya = Soil.objects.values('name', 'wilaya_id').filter(name=soil_id)
    data = [entry for entry in soil_wilaya]
    print(data)
    data1 = []
    mk_ids = []
    for x in data:
        w_id = x['wilaya_id']
        wilaya = Wilaya.objects.values('id', 'name', 'mkoa_id').get(id=w_id)
        mkoa = Mkoa.objects.values('id', 'name').get(id=wilaya['mkoa_id'])
        y = {'wilaya': wilaya['name'], 'mkoa': mkoa['name'], 'mkoa_id': mkoa['id']}
        mk_ids.append(mkoa['id'])
        print(mkoa['id'])
        data1.append(y)
    res = [*set(mk_ids)]
    print(res)
    print(mk_ids)
    data2 = []
    for x1 in res:
        mkoa_name = Mkoa.objects.values('name').get(id=x1)['name']
        data3 = []
        for x2 in data1:
            if x2['mkoa_id'] == x1:
                d = {'name': x2['wilaya']}
                data3.append(d)
        print(data3)
        d1 = {'mkoa': mkoa_name, 'wilaya': data3}
        data2.append(d1)

    return Response(data2)


# you provide product id and get the mikoa and wilaya which soil found
@api_view(['POST'])
@permission_classes([AllowAny])
def ProductToWilaya(request):
    product_id = request.data['id']
    product_wilaya = Product.objects.values('name', 'wilaya_id').filter(name=product_id)
    data = [entry for entry in product_wilaya]
    print(data)
    data1 = []
    mk_ids = []
    for x in data:
        w_id = x['wilaya_id']
        wilaya = Wilaya.objects.values('id', 'name', 'mkoa_id').get(id=w_id)
        mkoa = Mkoa.objects.values('id', 'name').get(id=wilaya['mkoa_id'])
        y = {'wilaya': wilaya['name'], 'mkoa': mkoa['name'], 'mkoa_id': mkoa['id']}
        mk_ids.append(mkoa['id'])
        print(mkoa['id'])
        data1.append(y)
    res = [*set(mk_ids)]
    print(res)
    print(mk_ids)
    data2 = []
    for x1 in res:
        mkoa_name = Mkoa.objects.values('name').get(id=x1)['name']
        data3 = []
        for x2 in data1:
            if x2['mkoa_id'] == x1:
                d = {'name': x2['wilaya']}
                data3.append(d)
        print(data3)
        d1 = {'mkoa': mkoa_name, 'wilaya': data3}
        data2.append(d1)

    return Response(data2)


# you provide desease id and get the mikoa and wilaya which soil found
@api_view(['POST'])
@permission_classes([AllowAny])
def DeseaseToWilaya(request):
    desease_id = request.data['id']
    desease_wilaya = Desease.objects.values('name', 'wilaya_id').filter(name=desease_id)
    data = [entry for entry in desease_wilaya]
    print(data)
    data1 = []
    mk_ids = []
    for x in data:
        w_id = x['wilaya_id']
        wilaya = Wilaya.objects.values('id', 'name', 'mkoa_id').get(id=w_id)
        mkoa = Mkoa.objects.values('id', 'name').get(id=wilaya['mkoa_id'])
        y = {'wilaya': wilaya['name'], 'mkoa': mkoa['name'], 'mkoa_id': mkoa['id']}
        mk_ids.append(mkoa['id'])
        print(mkoa['id'])
        data1.append(y)
    res = [*set(mk_ids)]
    print(res)
    print(mk_ids)
    data2 = []
    for x1 in res:
        mkoa_name = Mkoa.objects.values('name').get(id=x1)['name']
        data3 = []
        for x2 in data1:
            if x2['mkoa_id'] == x1:
                d = {'name': x2['wilaya']}
                data3.append(d)
        print(data3)
        d1 = {'mkoa': mkoa_name, 'wilaya': data3}
        data2.append(d1)

    return Response(data2)
