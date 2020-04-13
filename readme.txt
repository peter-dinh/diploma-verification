Em chào thầy , hôm nay em xin trình bày bài thực hành số 2:

Project su dung: 

Ubuntu18.6 
Python3.6 
Django==2.2.6

**** Cai dat chuong trinh

Git Repo : git clone https://github.com/peter-dinh/diploma-verification.git

Tao moi truong cai dat thu vien $ virtualenv -p python3.6 env

Active moi truong $ source env/bin/activate

Cai dat thu vien $ pip install -r req.txt

Cai dat database $ python manage.py migrate

> Run project $ python manage.py runserver

Create Admin User $ python manage.py createsuperuser (*)




**** Chay Demo tinh nang

Test API. *** De test can dang nhap tai khoan khi tao super user (*)

+ Create Co so Dao tao.
+ Sua Thong tin 
+ Xoa record 

Tra cứu văn bằng:
Khong can dang nhap van tra cuu duoc van bang.

Gia su can tim kiem thong tin cua nguoi nay:

{
    "id": 365,
    "hoten": "Orin McAvey",
    "ngaysinh": "2000-04-25",
    "gioitinh": "1",
    "cmnd": "696384183",
    "cosodaotao": 10,
    "ngaycapbang": "2005-03-02",
    "sohieu": "5743424772",
    "chuyennganh": "Senior Cost Accountant",
    "xeploai": "3",
    "loai_vanbang": 4,
    "gioitinh_display": "Nam",
    "xeploai_display": "Giỏi",
    "cosodaotao_name": "Đại học Nông Nghiệp",
    "loai_vanbang_name": "Bằng tốt nghiệp thạc sĩ"
}

 Khi tra cuu : Loai van bang :"Bằng tốt nghiệp thạc sĩ", Co so dao tao : "Đại học Nông Nghiệp"
 va nam cap bang = 2005 
=> se tra ve ket qua :

* Lập báo cáo văn bằng
Chi co user dang nhap moi co quyen su dung.


Bai trinh bay cua em ket thuc tai day. Cam on thay da theo doi.
