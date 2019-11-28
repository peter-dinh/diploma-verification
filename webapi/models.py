from django.db import models

# Create your models here.

CHOICES_GENDER = (('1', 'Nam'), ('0', 'Nữ'))
CHOICES_RANK = (('0', 'Kém'), ('1', 'Trung Bình'), ('2', 'Khá'), ('3', 'Giỏi'), ('4', 'Xuất Sắc'))
class VanBang(models.Model):

    hoten = models.CharField(max_length=100)
    ngaysinh = models.DateField()
    gioitinh = models.CharField(max_length=1, choices=CHOICES_GENDER)
    cmnd = models.CharField(max_length=12)
    cosodaotao = models.ForeignKey('CoSoDaoTao', on_delete=models.CASCADE)
    ngaycapbang = models.DateField()
    sohieu = models.CharField(max_length=100)
    chuyennganh = models.CharField(max_length=100)
    xeploai = models.CharField(max_length=1, choices=CHOICES_RANK)
    loai_vanbang = models.ForeignKey('LoaiVanBang', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['sohieu']
        ordering = ['ngaycapbang']

    def __str__(self):
        return self.hoten

class CoSoDaoTao(models.Model):

    ten = models.CharField(max_length=200)
    diachi = models.CharField(max_length=1000)

    def __str__(self):
        return self.ten

class LoaiVanBang(models.Model):

    ten = models.CharField(max_length=200)

    def __str__(self):
        return self.ten