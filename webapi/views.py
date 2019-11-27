from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class VanBangList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = VanBang.objects.all()
    serializer_class = VanBangSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.create(request, *args, **kwargs)

class VanBangDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = VanBang.objects.all()
    serializer_class = VanBangSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.destroy(request, *args, **kwargs)


class CoSoDaoTaoList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = CoSoDaoTao.objects.all()
    serializer_class = CoSoDaoTaoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.create(request, *args, **kwargs)

class CoSoDaoTaoDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
                    
    queryset = CoSoDaoTao.objects.all()
    serializer_class = CoSoDaoTaoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.destroy(request, *args, **kwargs)

class LoaiVanBangList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = LoaiVanBang.objects.all()
    serializer_class = LoaiVanBangSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.create(request, *args, **kwargs)

class LoaiVanBangDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
                    
    queryset = LoaiVanBang.objects.all()
    serializer_class = LoaiVanBangSerializer

    def get(self, request, *args, **kwargs):
        queryset = LoaiVanBang.objects.get(pk=self.kwargs.get('pk'))
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.destroy(request, *args, **kwargs)
