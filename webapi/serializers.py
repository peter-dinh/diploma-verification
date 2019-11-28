from rest_framework import serializers
from webapi.models import *


class CoSoDaoTaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoSoDaoTao
        fields = ('id', 'ten', 'diachi')

class LoaiVanBangSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoaiVanBang
        fields = ('id', 'ten')


class VanBangSerializers(serializers.ModelSerializer):
    gioitinh = serializers.SerializerMethodField()
    xeploai = serializers.SerializerMethodField()

    class Meta:
        model = VanBang
        fields = ('id', 'hoten', 'ngaysinh', 'gioitinh', 'cmnd', 'cosodaotao', 'ngaycapbang',
            'sohieu', 'chuyennganh', 'xeploai', 'loai_vanbang')

    def get_gioitinh(self,obj):
        return obj.get_gioitinh_display()
    def get_xeploai(self,obj):
        return obj.get_xeploai_display()