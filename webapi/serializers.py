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
    class Meta:
        model = VanBang
        fields = ('id', 'hoten', 'ngaysinh', 'gioitinh', 'cmnd', 'cosodaotao', 'namcapbang',
            'sohieu', 'chuyennganh', 'xeploai', 'loai_vanbang')
