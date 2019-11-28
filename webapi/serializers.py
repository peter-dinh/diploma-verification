from rest_framework import serializers
from webapi.models import *

CHOICES_GENDER = (('1', 'Men'), ('0', 'Female'))
CHOICES_RANK = (('0', 'Kem'), ('1', 'Trung Binh'), ('2', 'Kha'), ('3', 'Gioi'), ('4', 'Xuat Xac'))

class CoSoDaoTaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoSoDaoTao
        fields = ('id', 'ten', 'diachi')

class LoaiVanBangSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoaiVanBang
        fields = ('id', 'ten')


class VanBangSerializers(serializers.ModelSerializer):
    gioitinh = serializers.ChoiceField(choices=CHOICES_GENDER, source='get_gioitinh_display')
    xeploai = serializers.ChoiceField(choices=CHOICES_RANK, source='get_xeploai_display')

    class Meta:
        model = VanBang
        fields = ('id', 'hoten', 'ngaysinh', 'gioitinh', 'cmnd', 'cosodaotao', 'ngaycapbang',
            'sohieu', 'chuyennganh', 'xeploai', 'loai_vanbang')