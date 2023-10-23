from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    bio = models.CharField(max_length=155, null=True, blank=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users '


class Banner(models.Model):
    title = models.CharField(max_length=75)
    dascriptinon = models.CharField(max_length=25)
    text = models.CharField(max_length=255)
    img = models.ImageField(upload_to='banner_img/')

    def __str__(self):
        return self.dascriptinon

class About (models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()
    img = models.ImageField(upload_to='about_img/')

    def __str__(self):
        return self.title

class Servise(models.Model):
    name = models.CharField(max_length=255)
    dascriptinon = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='sar_icon/')

    def __str__(self):
        return self.name

class Category(models.Model):
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=25)
    dascriptinon = models.CharField(max_length=25)
    img = models.ImageField(upload_to='meal_photo/')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    prise = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Client(models.Model):
    photo = models.ImageField(upload_to='client_photo/')



class Blog (models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(to=Blog_Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(to=Tag)
    dascriptinon = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='blog_photo')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Contacts(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    message = models.TextField()
    email = models.CharField(max_length=55, null=True, blank=True)
    cubject = models.CharField(max_length=55, null=True, blank=True)

    def __str__(self):
        return self.first_name
class Info(models.Model):
    logo = models.ImageField(upload_to='info_photo/')
    phone_namber = models.CharField(max_length=25)
    addrses = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    fecebook = models.CharField(max_length=255)
    img = models.ImageField(upload_to='info_photo/')
    lot = models.FloatField()
    lat = models.FloatField()
    email = models.CharField(max_length=55)

    def __str__(self):
        return self.phone_namber

class Chef(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='chef_photo/')
    job = models.CharField(max_length=25)
    about_chef = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Blog_Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models. CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)







