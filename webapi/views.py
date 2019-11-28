from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters
from django_filters import rest_framework as filter_drf
from django_filters import DateRangeFilter,DateFilter
from django_filters.rest_framework import DjangoFilterBackend

import requests
from django.views.decorators.csrf import csrf_exempt
import xlwt
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User

def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="baocao.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Danh sách văn bằng')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    font_title = xlwt.XFStyle()
    font_title.font.bold = True
    font_title.height = 200

    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    font_title.alignment = alignment

    columns = ['STT', 'Họ tên', 'Ngày sinh', 'Chứng minh thư', 'Loại bằng', 'Cơ sở đào tạo', 'Ngày cấp', 'Xếp loại']

    ws.write_merge(0, 0, 0, len(columns), 'Thống kê văn bằng từ %s đến %s' % (request.GET.get('start_date'), request.GET.get('end_date')), font_title)
    row_num += 3
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    if request.GET.get('loaivanbang') != 'false':
        loaivanbang = int(request.GET.get('loaivanbang'))
        rows = VanBang.objects.filter(ngaycapbang__range=[request.GET.get('start_date'), request.GET.get('end_date')],
                        loai_vanbang=loaivanbang)
    else:
        rows = VanBang.objects.filter(ngaycapbang__range=[request.GET.get('start_date'), request.GET.get('end_date')])
    index = 1
    for row in rows:
        key = ['index', 'hoten', 'ngaysinh', 'cmnd', 'loai_vanbang', 'cosodaotao', 'ngaycapbang', 'xeploai']
        data = dict({
            'index': str(index),
            'hoten': row.hoten,
            'ngaysinh': row.ngaysinh.strftime('%d-%m-%Y'),
            'cmnd': row.cmnd,
            'loai_vanbang': row.loai_vanbang.ten,
            'cosodaotao': row.cosodaotao.ten,
            'ngaycapbang': row.ngaycapbang.strftime('%d-%m-%Y'),
            'xeploai': row.get_xeploai_display(),
        })
        row_num += 1
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, data[key[col_num]], font_style)

    wb.save(response)
    return response


def index(request):
    return render(request, 'search.html', {
        'loaivanbang': LoaiVanBang.objects.all(),
        'cosodaotao': CoSoDaoTao.objects.all()
    })

def report(request):
    if request.user.pk:
        return render(request, 'report.html', {
            'loaivanbang': LoaiVanBang.objects.all(),
            'cosodaotao': CoSoDaoTao.objects.all()
        })
    return HttpResponse('No Access!')

@csrf_exempt
def verifying(request):
    if request.method == 'POST':
        url = "https://www.google.com/recaptcha/api/siteverify?response=%s&secret=6LcEBsUUAAAAACltC8JQCM9u4m6rZ6daJ_ClBWwc" % request.POST.get('response')
        payload = {}
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return HttpResponse(response, content_type="application/json")
    return HttpResponse('Error')


class VanBangFilter(filter_drf.FilterSet):
    start_date = DateFilter(field_name='ngaycapbang',lookup_expr=('gte')) 
    end_date = DateFilter(field_name='ngaycapbang',lookup_expr=('lte'))

    class Meta:
        model = VanBang
        fields = ['hoten', 'cmnd', 'cosodaotao', 'ngaycapbang', 'sohieu', 'loai_vanbang', 'start_date', 'end_date']

class VanBangList(generics.ListCreateAPIView):
    queryset = VanBang.objects.all()
    serializer_class = VanBangSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = VanBangFilter
    # filterset_fields = ['hoten', 'cmnd', 'cosodaotao', 'ngaycapbang', 'sohieu', 'loai_vanbang']


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
