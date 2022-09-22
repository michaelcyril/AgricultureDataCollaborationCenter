# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#
# # {'name':'mike', 'age':age}
# # class Desease(models.Model):
# #     choice = (("soil", "soil"), ("product", "product"),)
# #     name = models.CharField(max_length=100)
# #     wilaya_id = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
# #     of_product = models.ForeignKey(Product, on_delete=models.CASCADE, name=True, blank=True)
# #     of_soil = models.ForeignKey(Soil, on_delete=models.CASCADE, null=True, blank=True)
# #     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
# #     desease = models.CharField(max_length=20, choices=choice, null=False)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #
# #     def __str__(self):
# #         return self.name
#
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from .models import *
# from .serializers import *
# from AuthStakeholder.models import User, Mkoa, Wilaya, AdminProfile
#
#
# # Create your views here.
#
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def PostSoilView(request):
#     admin_type = AdminProfile.objects.values('type').get(
#         user_id=User.objects.get(username=request.user))['type']
#     if admin_type == 'soil':
#         user = User.objects.get(username=request.user)
#         name = Soi.objects.get(id=request.data['soil_id'])
#         wilaya = Wilaya.objects.get(id=request.data['wilaya_id'])
#         images = request.data['images']
#         soil_tosave = Soil.objects.create(name=name, wilaya_id=wilaya, created_by=user)
#         soil_tosave.save()
#         saved = Soil.objects.values('id').all
#         soil = [entry for entry in saved]
#         s1 = []
#         for s in soil:
#             s1.append(s['id'])
#         saved_id = max(s1)
#         a_soil = Soil.objects.get(id=saved_id)
#         for img in images:
#             imageSave = SoilImage.objects.create(image=img['image'], soil_id=a_soil)
#             imageSave.save()
#         return Response({'message': 'Soil successful saved'})
#     return Response({'message': 'The user is not responsible to save this data'})
#
#
# # {
# #     "soil_id": 1,
# #     "wilaya_id": 1,
# #     "images": [{"image": "image2.png"}, {"image": "image3.png"}]
# # }
#
#
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def PostProductView(request):
#     admin_type = AdminProfile.objects.values('type').get(
#         user_id=User.objects.get(username=request.user))['type']
#     if admin_type == 'agriculture':
#         user = User.objects.get(username=request.user)
#         name = Prod.objects.get(id=request.data['product_id'])
#         wilaya = Wilaya.objects.get(id=request.data['wilaya_id'])
#         images = request.data['images']
#         product_tosave = Product.objects.create(name=name, wilaya_id=wilaya, created_by=user)
#         product_tosave.save()
#         saved = Product.objects.values('id').all
#         product = [entry for entry in saved]
#         p1 = []
#         for s in product:
#             p1.append(s['id'])
#         saved_id = max(p1)
#         a_product = Product.objects.get(id=saved_id)
#         for img in images:
#             imageSave = ProductImage.objects.create(image=img['image'], product_id=a_product)
#             imageSave.save()
#         return Response({'message': 'Product successful saved'})
#     return Response({'message': 'The user is not responsible to save this data'})
#
#
# # {
# #     "product_id": 1,
# #     "wilaya_id": 1,
# #     "images": [{"image": "image2.png"}, {"image": "image3.png"}]
# # }
#
#
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def PostDeseaseView(request):
#     admin_type = AdminProfile.objects.values('type').get(
#         user_id=User.objects.get(username=request.user))['type']
#     if admin_type == 'agriculture':
#         user = User.objects.get(username=request.user)
#         name = request.data['name']
#         wilaya = Wilaya.objects.get(id=request.data['wilaya_id'])
#         images = request.data['images']
#         desease_tosave = Desease.objects.create(name=name, wilaya_id=wilaya, created_by=user)
#         desease_tosave.save()
#         saved = Desease.objects.values('id').all
#         desease = [entry for entry in saved]
#         d1 = []
#         for s in desease:
#             d1.append(s['id'])
#         saved_id = max(d1)
#         a_desease = Desease.objects.get(id=saved_id)
#         for img in images:
#             imageSave = SoilImage.objects.create(image=img['image'], desease_id=a_desease)
#             imageSave.save()
#         return Response({'message': 'Desease successful saved'})
#     return Response({'message': 'The user is not responsible to save this data'})
#
#
# # {
# #     "name": "pestcide",
# #     "wilaya_id": 1,
# #     "images": [{"image": "image2.png"}, {"image": "image3.png"}]
# # }
#
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def homeView(requests):
#     mikoa = Mkoa.objects.values('id', 'name').all()
#     data = [entry for entry in mikoa]
#     return Response(data)
#
#
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def getWilayaWithInfo(request):
#     wilaya = Wilaya.objects.values('id', 'name', 'mkoa_id').filter(mkoa_id=request.data['id'])
#     data = [entry for entry in wilaya]
#     print(data)
#     details = []
#     for dat in data:
#         info = []
#         w_id = dat['id']
#         print(w_id)
#         # for disease
#         try:
#             des = Desease.objects.values('id', 'name', 'created_by', 'created_at').filter(wilaya_id=w_id)
#             # print('for wilaya_id'+w_id+"  "+str(des))
#             desease = [entry for entry in des]
#             # print(desease)
#             if len(desease) > 1:
#                 # des_id = desease[0]['id']
#                 desease1 = []
#                 for des1 in desease:
#                     images = DeseaseImage.objects.values('id', 'image').filter(desease_id=des1['id'])
#                     h = {'desease': des1, 'images': [entry for entry in images]}
#                     desease1.append(h)
#                     print(desease1)
#
#                 d = {'name': 'magonjwa', 'list': desease1}
#             elif len(desease) == 1:
#                 images = DeseaseImage.objects.values('id', 'image').filter(desease_id=desease[0]['id'])
#                 desease1 = [{'desease': desease[0], 'images': [entry for entry in images]}]
#                 d = {'name': 'magonjwa', 'list': desease1}
#                 print(desease1)
#
#             elif len(desease) == 0:
#                 pass
#
#
#             try:
#                 info.append(d)
#             except NameError:
#                 pass
#
#         except Desease.DoesNotExist:
#             pass
#
#         # for product
#         try:
#             pro = Product.objects.values('id', 'name', 'created_by', 'created_at').filter(wilaya_id=w_id)
#             product = [entry for entry in pro]
#             # print(product)
#             if len(product) > 1:
#                 # des_id = desease[0]['id']
#                 product1 = []
#                 for pro1 in product:
#                     images = ProductImage.objects.values('id', 'image').filter(product_id=pro1['id'])
#                     h = {'mazao': pro1, 'images': [entry for entry in images]}
#                     product1.append(h)
#                     print(product1)
#
#                 d = {'name': 'mazao', 'list': product1}
#             elif len(product) == 1:
#                 images = ProductImage.objects.values('id', 'image').filter(product_id=product[0]['id'])
#                 product1 = [{'product': product[0], 'images': [entry for entry in images]}]
#                 d = {'name': 'mazao', 'list': product1}
#                 print(product1)
#
#             elif len(product) == 0:
#                 pass
#             # print(product1)
#             try:
#                 info.append(d)
#             except NameError:
#                 pass
#
#         except Product.DoesNotExist:
#             pass
#
#         # for soil
#         try:
#             soi = Soil.objects.values('id', 'name', 'created_by', 'created_at').filter(wilaya_id=w_id)
#             soil = [entry for entry in soi]
#             # print(soil)
#             if len(soil) > 1:
#                 # des_id = desease[0]['id']
#                 soil1 = []
#                 for soi1 in soil:
#                     images = SoilImage.objects.values('id', 'image').filter(soil_id=soi1['id'])
#                     h = {'soil': soi1, 'images': [entry for entry in images]}
#                     soil1.append(h)
#                     print(soil1)
#
#                 d = {'name': 'udongo', 'list': soil1}
#             elif len(soil) == 1:
#                 images = SoilImage.objects.values('id', 'image').filter(soil_id=soil[0]['id'])
#                 soil1 = [{'soil': soil[0], 'images': [entry for entry in images]}]
#                 d = {'name': 'udongo', 'list': soil1}
#                 print(soil1)
#
#             elif len(soil) == 0:
#                 pass
#             # print(soil1)
#
#             try:
#                 print(d)
#                 info.append(d)
#             except NameError:
#                 pass
#
#         except Soil.DoesNotExist:
#             pass
#
#         # try:
#         #     pro = Product.objects.values('id', 'name', 'created_by', 'created_at').filter(wilaya_id=w_id)
#         #     products = [entry for entry in pro]
#         #     d = {'name': 'mazao', 'list': products}
#         #     info.append(d)
#         # except Product.DoesNotExist:
#         #     pass
#         #
#         # try:
#         #     so = Soil.objects.values('id', 'name', 'created_by', 'created_at').filter(wilaya_id=w_id)
#         #     print(so)
#         #     soil = [entry for entry in so]
#         #     d = {'name': 'udongo', 'list': soil}
#         #     info.append(d)
#         # except Soil.DoesNotExist:
#         #     pass
#
#         d1 = {'wilaya': dat['name'], 'info': info}
#         details.append(d1)
#         # print(info)
#     return Response(details)
# # {"id":1}
#
# # @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# # def get
# from random import random
# import random
#
# l = [1, 2, 4, 2, 1, 4, 5]
# code = random.randint(0, 999999)
# print("Original List: ", l)
# res = [*set(l)]
# print("List after removing duplicate elements: ", code)

string = "Hhello world"
new_string = string[1:]
print(new_string)