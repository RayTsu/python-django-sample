from django.db import models

# Create your models here.
class Classes(models.Model):
    """
    班级表，男
    """
    titile = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")


class Teachers(models.Model):
    """
    老师表，女
    """
    name = models.CharField(max_length=32)


class Student(models.Model):
    """
    cid_id  tid_id
        1    1
        1    2
        6    1
        1000  1000
    """
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(
        Classes,
        on_delete=models.CASCADE,
                           )