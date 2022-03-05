from django.db import models

# Create your models here.
class Flats(models.Model):
    flat_id = models.IntegerField(verbose_name="公寓编号")
    flat_name = models.CharField(max_length=20, verbose_name="公寓名称")
    flat_number = models.IntegerField(verbose_name="所住人数")
    flat_teacher = models.CharField(max_length=20, verbose_name="管理老师")
    flat_image = models.ImageField(upload_to='',default=False)
    # upload_to是指要上传到哪一个文件夹'

class Students(models.Model):
    student_number = models.IntegerField(verbose_name="学号")
    student_name = models.CharField(max_length=20, verbose_name="姓名")
    student_gender = models.CharField(max_length=5, verbose_name="性别")
    student_math = models.IntegerField(verbose_name="数学成绩")
    student_chinese = models.IntegerField(verbose_name="语文成绩")
    student_english = models.IntegerField(verbose_name="英语成绩")
    student_flat = models.ForeignKey('Flats', on_delete=models.CASCADE, verbose_name="所住公寓")