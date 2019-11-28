from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('vanbang/', views.VanBangList.as_view()),
    path('vanbang/<int:pk>/', views.VanBangDetail.as_view()),
    path('loaivanbang/', views.LoaiVanBangList.as_view()),
    path('loaivanbang/<int:pk>/', views.LoaiVanBangDetail.as_view()),
    path('cosodaotao/', views.CoSoDaoTaoList.as_view()),
    path('cosodaotao/<int:pk>/', views.CoSoDaoTaoDetail.as_view()),

    path('export/xls/', views.export_xls, name='export_xls'),
    path('verifying/', views.verifying, name='verifying'),

]

urlpatterns = format_suffix_patterns(urlpatterns)