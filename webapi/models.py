from django.db import models

# Create your models here.

CHOICES_GENDER = (('1', 'Men'), ('0', 'Female'))
CHOICES_RANK = (('0', 'Kem'), ('1', 'Trung Binh'), ('2', 'Kha'), ('3', 'Gioi'), ('4', 'Xuat Xac'))
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