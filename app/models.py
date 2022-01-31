from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_type = models.CharField(default = 1, max_length = 100)

class Checkin(models.Model):
    id = models.AutoField(primary_key=True)
    nId_person = models.IntegerField(blank=True,null=True)
    check_in = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class UserType(models.Model):
    id = models.AutoField(primary_key=True)
    user_type_name = models.CharField(max_length=225)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

# Table Dhama AllTables
class TableAll(models.Model):

# value to be insert into the database
    Male = 'ชาย'
    Female = 'หญิง'
    Boy = 'ด.ช'
    Girl = 'ด.ญ'

# value that will be apppend on the select option   
    gender = [
        (Male, 'ชาย'),
        (Female, 'หญิง'),
        (Boy, 'ด.ช'),
        (Girl, 'ด.ญ'),
    ]
# value to be insert into the database
    Level1 = 'เตี่ยนฉวนซือ'
    Level2 = 'เจี่ยงซือ'
    Level3 = 'ถันจู่'
    Level4 = 'เจี่ยงเอี๋ยน'
    Level5 = 'พุทธบริกร'

# value that will be apppend on the select option   
    level = [
        (Level1, 'เตี่ยนฉวนซือ'),
        (Level2, 'เจี่ยงซือ'),
        (Level3, 'ถันจู่'),
        (Level4, 'เจี่ยงเอี๋ยน'),
        (Level5, 'พุทธบริกร'),
    ]
# value to be insert into the database
    edu1 = 'ป.เอก'
    edu2 = 'ป.โท'
    edu3 = 'ป.ตรี'
    edu4 = 'ปวส'
    edu5 = 'ปวท'
    edu6 = 'ปวช'
    edu7 = 'มัธยม'
    edu8 = 'ประถม'
    edu9 = 'อนุบาล'
    edu10 = 'ไม่ได้เรียน'
    edu11 = 'ไม่แจ้ง'

# value that will be apppend on the select option   
    edu = [
        (edu1, 'ป.เอก'),
        (edu2, 'ป.โท'),
        (edu3, 'ป.ตรี'),
        (edu4, 'ปวส'),
        (edu5, 'ปวท'),
        (edu6, 'ปวช'),
        (edu7, 'มัธยม'),
        (edu8, 'ประถม'),
        (edu9, 'อนุบาล'),
        (edu10, 'ไม่ได้เรียน'),
        (edu11, 'ไม่แจ้ง'),
    ]
# value to be insert into the database
    career1 = 'เกษตรกร'
    career2 = 'เกษียณ'
    career3 = 'ขายอาหารเจ'
    career4 = 'ข้าราชการบำนาญ'
    career5 = 'ครู/อาจารย์'
    career6 = 'ค้าขาย'
    career7 = 'ธนาคาร'
    career8 = 'แพทย์/พยาบาล'
    career9 = 'ตำรวจ/ทหาร'
    career10 = 'ธุรกิจส่วนตัว/อิสระ'
    career11 = 'พนักงานบริษัท'
    career12 = 'พนักงานรัฐวิสาหกิจ'
    career13 = 'พ่อบ้าน'
    career14 = 'แม่บ้าน'
    career15 = 'รับจ้าง'
    career16 = 'รับราชการ'
    career17 = 'นักเรียน'
    career18 = 'นักศึกษา'
    career19 = 'อื่นๆ'

# value that will be apppend on the select option   
    career = [
        (career1, 'เกษตรกร'),
        (career2, 'เกษียณ'),
        (career3, 'ขายอาหารเจ'),
        (career4, 'ข้าราชการบำนาญ'),
        (career5, 'ครู/อาจารย์'),
        (career6, 'ค้าขาย'),
        (career7, 'ธนาคาร'),
        (career8, 'แพทย์/พยาบาล'),
        (career9, 'ตำรวจ/ทหาร'),
        (career10, 'ธุรกิจส่วนตัว/อิสระ'),
        (career11, 'พนักงานบริษัท'),
        (career12, 'พนักงานรัฐวิสาหกิจ'),
        (career13, 'พ่อบ้าน'),
        (career14, 'แม่บ้าน'),
        (career15, 'รับจ้าง'),
        (career16, 'รับราชการ'),
        (career17, 'นักเรียน'),
        (career18, 'นักศึกษา'),
        (career19, 'อื่นๆ'),
    ]
# value to be insert into the database
    pro1 = 'จางเหวินฟ่ง'
    pro2 = 'จางชุ่ยเหวิน'
    pro3 = 'เฉินจวิ้นสยง'
    pro4 = 'หลี่ซิ่วอวี้'
    pro5 = 'สวีลี่หย่ง'

# value that will be apppend on the select option   
    pro = [
        (pro1, 'จางเหวินฟ่ง'),
        (pro2, 'จางชุ่ยเหวิน'),
        (pro3, 'เฉินจวิ้นสยง'),
        (pro4, 'หลี่ซิ่วอวี้'),
        (pro5, 'สวีลี่หย่ง'),
    ]

    nId_person = models.CharField(verbose_name='รหัส', max_length=100)
    cGender = models.CharField(verbose_name='เพศ',max_length=19,choices=gender,default=Male)
    cFname = models.CharField(verbose_name='ชื่อ-นามสกุล',max_length=100)
    nAge = models.IntegerField(verbose_name='อายุ',blank=True,null=True)
    cLevel = models.CharField(verbose_name='ธรรมวุฒิ',max_length = 100,choices=level,default=Level5)
    cEdu = models.CharField(verbose_name='การศึกษา',max_length = 100,choices=edu,default=edu11)
    cCareer = models.CharField(verbose_name='อาชีพ',max_length = 100,choices=career,default=career19)
    cRoom = models.CharField(verbose_name='พุทธสถาน',max_length = 100, blank = True, null = True)
    cRoom_c = models.CharField(verbose_name='พุทธสถาน(จีน)',max_length = 100, blank = True, null = True)
    cPro = models.CharField(verbose_name='อ.ถ่ายทอดเบิกธรรม',max_length = 100,choices=pro,default=pro5)
    cPro_c = models.CharField(verbose_name='อ.ถ่ายทอดเบิกธรรม(จีน)',max_length = 100, blank = True, null = True)
    cDate_c = models.CharField(verbose_name='วันรับธรรมะ(ภาษาจีน)',max_length = 100, blank = True, null = True)
    cDate_dc = models.CharField(verbose_name='วันรับธรรมะ(จีน)',max_length = 100, blank = True, null = True)
    cTdate = models.CharField(verbose_name='วันรับธรรมะ(ไทย)',max_length = 100, blank = True, null = True)
    dDate = models.DateField(verbose_name='วันรับธรรมะ',blank = True, null = True)
    cRec = models.CharField(verbose_name='อ.แนะนำ',max_length = 100, blank = True, null = True)
    cSup = models.CharField(verbose_name='อ.รับรอง',max_length = 100, blank = True, null = True)
    cAddress = models.CharField(verbose_name='ที่อยู่',max_length = 100, blank = True, null = True)
    cMtel = models.CharField(verbose_name='โทรศัพท์มือถือ',max_length = 100, blank = True, null = True)
    cHtel = models.CharField(verbose_name='โทรศัพท์บ้าน',max_length = 100, blank = True, null = True)
    cName = models.CharField(verbose_name='ชื่อจีน',max_length=100,blank=True,null=True)
    c3dd = models.CharField(max_length = 100, blank = True, null = True)
    c3dl = models.CharField(max_length = 100, blank = True, null = True)
    cMd = models.CharField(max_length = 100, blank = True, null = True)
    cMl = models.CharField(max_length = 100, blank = True, null = True)
    cSd = models.CharField(max_length = 100, blank = True, null = True)
    cSl = models.CharField(max_length = 100, blank = True, null = True)
    cJd = models.CharField(max_length = 100, blank = True, null = True)
    cJl = models.CharField(max_length = 100, blank = True, null = True)
    cPt1 = models.CharField(max_length = 3, blank = True, null = True)
    cPt2 = models.CharField(max_length = 3, blank = True, null = True)
    cPt3 = models.CharField(max_length = 3, blank = True, null = True)
    cPt4 = models.CharField(max_length = 3, blank = True, null = True)
    cPt5 = models.CharField(max_length = 3, blank = True, null = True)
    cPt6 = models.CharField(max_length = 3, blank = True, null = True)
    cCd = models.CharField(max_length = 100, blank = True, null = True)
    cCl = models.CharField(max_length = 100, blank = True, null = True)
    cCp = models.CharField(max_length = 100, blank = True, null = True)
    cUd = models.CharField(max_length = 100, blank = True, null = True)
    cUl = models.CharField(max_length = 100, blank = True, null = True)
    cUp = models.CharField(max_length = 100, blank = True, null = True)
    cRd = models.CharField(max_length = 100, blank = True, null = True)
    cRl = models.CharField(max_length = 100, blank = True, null = True)
    cRp = models.CharField(max_length = 100, blank = True, null = True)
    cPd = models.CharField(max_length = 100, blank = True, null = True)
    cPl = models.CharField(max_length = 100, blank = True, null = True)
    cPp = models.CharField(max_length = 100, blank = True, null = True)
    cJvd = models.CharField(max_length = 100, blank = True, null = True)
    cJvl = models.CharField(max_length = 100, blank = True, null = True)
    cJvp = models.CharField(max_length = 100, blank = True, null = True)
    cTjd = models.CharField(max_length = 100, blank = True, null = True)
    cTjl = models.CharField(max_length = 100, blank = True, null = True)
    cTjp = models.CharField(max_length = 100, blank = True, null = True)
    cJcd = models.CharField(max_length = 100, blank = True, null = True)
    cJcl = models.CharField(max_length = 100, blank = True, null = True)
    cJcp = models.CharField(max_length = 100, blank = True, null = True)
    cPrd = models.CharField(max_length = 100, blank = True, null = True)
    cPrl = models.CharField(max_length = 100, blank = True, null = True)
    cPrp = models.CharField(max_length = 100, blank = True, null = True)

#Table Dhama Bkk1
class Bkk1(TableAll): # name of alltable bkk1
    pass

class Bkk1001(Bkk1): # name of of table
    pass

class Bkk1002(Bkk1): # name of of table
    pass

class Bkk1003(Bkk1): # name of of table
    pass



#Table Dhama Skw1
class Skw1(TableAll): # name of alltable skw1
    pass


class Skw1001(Skw1): # name of of table
    pass

class Skw1002(Skw1): # name of of table
    pass
    
class Skw1003(Skw1): # name of of table
    pass

