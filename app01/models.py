from django.db import models

# Create your models here.
class Depart(models.Model):
    Dname = models.CharField(max_length=20,unique=True,null=False)

class Classes(models.Model):
    Clsname = models.CharField(max_length=20,null=False)
    Dep = models.ForeignKey(to='Depart',on_delete=models.CASCADE,related_name='classes',null=False)
    class Meta:
        unique_together = [('Clsname','Dep')]

class Student(models.Model):
    Sno = models.CharField(max_length=20,primary_key=True)
    Sname = models.CharField(max_length=20, null=False, default=None)
    Ssex = models.BooleanField(null=False, default=None)
    Sbirthday = models.DateTimeField(null=True, default=None)
    Cls = models.ForeignKey(to='Classes',on_delete=models.CASCADE,related_name='students',null=False)

class Teacher(models.Model):
    Tno = models.CharField(max_length=20, primary_key=True)
    Tname = models.CharField(max_length=20, null=False)
    Tsex = models.BooleanField(null=False)
    Tbirthday = models.DateTimeField(null=True)
    Prof = models.CharField(max_length=20, null=True)
    Dep = models.ForeignKey(to='Depart', on_delete=models.CASCADE, related_name='teachers',null=False)

class Course(models.Model):
    Cno = models.CharField(max_length=20,primary_key=True)
    Cname = models.CharField(max_length=20,null=False)
    Tea = models.ManyToManyField(to='Teacher',related_name='courses')

class Score(models.Model):
    Stu = models.ForeignKey(to='Student',on_delete=models.CASCADE,related_name='scores',null=False)
    Cno = models.ForeignKey(to='Course',on_delete=models.CASCADE,related_name='scores',null=False)
    Degree = models.DecimalField(max_digits=4,decimal_places=1)
