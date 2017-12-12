from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Faculty(models.Model):
    user=models.OneToOneField(User)
    Webmail=models.CharField(max_length=100,default="")
    Position=models.CharField(max_length=100,default="")
    department=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=100,default="")
    image=models.FileField(upload_to="project/media/profile_image/",default='project/media/profile_image/1.png')
    fax=models.CharField(max_length=100,default="")
    About=models.CharField(max_length=2000,default="")
    Room_No=models.CharField(max_length=200,default=0)

    def __str__(self):
        return self.user.username
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Faculty.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Qualification(models.Model):
    user=models.ForeignKey(User)
    Btech=models.CharField(max_length=1000,default="")
    Mtech=models.CharField(max_length=1000,default="")
    PHD=models.CharField(max_length=1000,default="")


    def __str__(self):
        return self.user.username




class Projects(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100, default="")
    Sponsorer = models.CharField(max_length=1000, default="")
    role = models.CharField(max_length=1000, default="")
    duration = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.user.username



class Teaching(models.Model):
    user = models.ForeignKey(User)
    Course = models.CharField(max_length=200,default="")
    time=models.CharField(max_length=2000,default="")
    Semester=models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.user.username

class Experience(models.Model):
    user = models.ForeignKey(User)
    Institute = models.CharField(max_length=100, default="")
    Position = models.CharField(max_length=1000, default="")
    year = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.user.username
class Question(models.Model):
    user=models.ForeignKey(User)
    name = models.CharField(max_length=2000, default="Unknown")
    que =models.CharField(max_length=2000,default="")
    ans =models.CharField(max_length=2000,default="NULL")

    def __str__(self):
        return self.user.username





