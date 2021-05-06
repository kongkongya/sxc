# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carousel(models.Model):
    id = models.IntegerField(primary_key=True)
    imgsrc = models.CharField(db_column='imgSrc', max_length=50)  # Field name made lowercase.
    imgurl = models.CharField(db_column='imgUrl', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'carousel'


class Catelist(models.Model):
    id = models.IntegerField(primary_key=True)
    cateimg = models.CharField(db_column='cateImg', max_length=200)  # Field name made lowercase.
    catename = models.CharField(db_column='cateName', max_length=10)  # Field name made lowercase.
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catelist'


class City(models.Model):
    cityname = models.CharField(db_column='cityName', max_length=20)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
    pagein = models.CharField(db_column='pageIn', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Coupon(models.Model):
    couponname = models.CharField(db_column='couponName', max_length=20)  # Field name made lowercase.
    couponprice = models.CharField(db_column='couponPrice', max_length=20)  # Field name made lowercase.
    starttime = models.TimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime')  # Field name made lowercase.
    partgoods = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'coupon'


class Coupongoods(models.Model):
    couponid = models.IntegerField(db_column='couponId')  # Field name made lowercase.
    goodid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupongoods'


class Feedback(models.Model):
    navid = models.IntegerField(db_column='navId')  # Field name made lowercase.
    backmsg = models.TextField(db_column='backMsg')  # Field name made lowercase.
    backimg = models.CharField(db_column='backImg', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'feedback'


class Feedbacknav(models.Model):
    pid = models.IntegerField()
    level = models.IntegerField()
    parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
    cateid = models.IntegerField(db_column='cateId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedbacknav'


class Goodimg(models.Model):
    goodid = models.IntegerField()
    goodimgurl = models.CharField(db_column='goodImgUrl', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodimg'


class Goodslist(models.Model):
    cateid = models.IntegerField(db_column='cateId')  # Field name made lowercase.
    goodsimg = models.CharField(db_column='goodsImg', max_length=200)  # Field name made lowercase.
    goodsname = models.CharField(db_column='goodsName', max_length=30)  # Field name made lowercase.
    weight = models.CharField(max_length=10)
    package = models.CharField(max_length=10)
    nowprice = models.DecimalField(db_column='nowPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    discountprice = models.DecimalField(db_column='discountPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    warn = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'goodslist'


class Magnav(models.Model):
    title = models.CharField(max_length=50)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'magnav'


class Msg(models.Model):
    typeid = models.IntegerField()
    msgtitle = models.CharField(db_column='msgTitle', max_length=50)  # Field name made lowercase.
    msgtime = models.CharField(db_column='msgTime', max_length=50)  # Field name made lowercase.
    msgtype = models.CharField(db_column='msgType', max_length=10)  # Field name made lowercase.
    msgauthor = models.CharField(db_column='msgAuthor', max_length=20)  # Field name made lowercase.
    msgdetail = models.TextField(db_column='msgDetail')  # Field name made lowercase.
    videosrc = models.CharField(db_column='videoSrc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'msg'


class Msgimg(models.Model):
    msgid = models.IntegerField()
    imgsrc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msgimg'


class Order(models.Model):
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    ordernum = models.CharField(db_column='orderNum', max_length=50)  # Field name made lowercase.
    totalprice = models.IntegerField(db_column='totalPrice')  # Field name made lowercase.
    ordertime = models.TimeField(db_column='orderTime')  # Field name made lowercase.
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order'


class Orderdetail(models.Model):
    orderid = models.IntegerField(db_column='orderId')  # Field name made lowercase.
    price = models.IntegerField()
    productid = models.IntegerField(db_column='productId')  # Field name made lowercase.
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orderdetail'


class Productdetail(models.Model):
    goodid = models.IntegerField(db_column='goodId')  # Field name made lowercase.
    count = models.IntegerField()
    provice = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    area = models.CharField(max_length=10)
    detail = models.TextField()

    class Meta:
        managed = False
        db_table = 'productdetail'


class Provice(models.Model):
    provice = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'provice'


class Stall(models.Model):
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    starttime = models.TimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime')  # Field name made lowercase.
    stallname = models.CharField(db_column='stallName', max_length=50)  # Field name made lowercase.
    market = models.CharField(max_length=100)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stall'


class Storetransfer(models.Model):
    cityid = models.IntegerField()
    storetitle = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    tip = models.CharField(max_length=10)
    rent = models.CharField(max_length=50)
    area = models.CharField(max_length=10)
    detail = models.TextField()

    class Meta:
        managed = False
        db_table = 'storetransfer'


class Storetransferimg(models.Model):
    storeid = models.IntegerField()
    imgsrc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storetransferimg'


class Sxcinfo(models.Model):
    useragreement = models.TextField(db_column='userAgreement')  # Field name made lowercase.
    aptitudeimg = models.CharField(db_column='aptitudeImg', max_length=50)  # Field name made lowercase.
    servicewx = models.CharField(db_column='serviceWX', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sxcinfo'


class Usedcoupon(models.Model):
    userid = models.IntegerField()
    couponid = models.IntegerField(db_column='couponId')  # Field name made lowercase.
    ordernum = models.CharField(db_column='orderNum', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usedcoupon'


class User(models.Model):
    openid = models.CharField(max_length=50)
    nickname = models.CharField(db_column='nickName', max_length=30)  # Field name made lowercase.
    sex = models.IntegerField()
    phonenum = models.CharField(db_column='phoneNum', max_length=11)  # Field name made lowercase.
    money = models.CharField(max_length=10)
    newuser = models.IntegerField(db_column='newUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Userdetail(models.Model):
    userid = models.IntegerField()
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    type = models.CharField(max_length=50, blank=True, null=True)
    stall = models.IntegerField(blank=True, null=True)
    carnum = models.CharField(db_column='carNum', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userdetail'
