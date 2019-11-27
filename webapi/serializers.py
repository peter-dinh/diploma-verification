from rest_framework import serializers
from webapi.models import *


class CoSoDaoTaoSerializer(serializers.Serializer):
    ten = serializers.CharField(max_length=200)
    diachi = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return CoSoDaoTao.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ten = validated_data.get('ten', instance.ten)
        instance.diachi = validated_data.get('diachi', instance.diachi)
        instance.save()
        return instance

class LoaiVanBangSerializer(serializers.Serializer):

    ten = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return LoaiVanBang.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ten = validated_data.get('ten', instance.ten)
        instance.save()
        return instance
        
class VanBangSerializers(serializers.Serializer):
    hoten = serializers.CharField(allow_blank=True, max_length=100)
    ngaysinh = serializers.DateField()
    gioitinh = serializers.ChoiceField(choices=CHOICES_GENDER)
    cmnd = serializers.CharField(max_length=12)
    cosodaotao = CoSoDaoTaoSerializer(required=True)
    ngaycapbang = serializers.DateField()
    sohieu = serializers.CharField(max_length=100)
    chuyennganh = serializers.CharField(max_length=100)
    xeploai = serializers.ChoiceField(choices=CHOICES_RANK)
    loai_vanbang = LoaiVanBangSerializer(required=True)

    def create(self, validated_data):
        return VanBang.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
