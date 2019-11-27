from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

def index(request):
    return render(request, 'search.html', {
        'loaivanbang': LoaiVanBang.objects.all(),
        'cosodaotao': CoSoDaoTao.objects.all()
    })

def report(request):
    return render(request, 'report.html', {
        'loaivanbang': LoaiVanBang.objects.all(),
        'cosodaotao': CoSoDaoTao.objects.all()
    })


class VanBangList(generics.ListCreateAPIView):
    queryset = VanBang.objects.all()
    serializer_class = VanBangSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hoten', 'cmnd', 'cosodaotao', 'namcapbang', 'sohieu', 'loai_vanbang']


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.create(request, *args, **kwargs)

class VanBangDetail(generics.RetrieveUpdateDestroyAPIView):

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


class CoSoDaoTaoList(generics.ListCreateAPIView):
    queryset = CoSoDaoTao.objects.all()
    serializer_class = CoSoDaoTaoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['ten']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.create(request, *args, **kwargs)

class CoSoDaoTaoDetail(generics.RetrieveUpdateDestroyAPIView):
                    
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

class LoaiVanBangList(generics.ListCreateAPIView):
    queryset = LoaiVanBang.objects.all()
    serializer_class = LoaiVanBangSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['ten']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        permission_classes = [IsAdminUser]
        return self.create(request, *args, **kwargs)

class LoaiVanBangDetail(generics.RetrieveUpdateDestroyAPIView):
                    
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
