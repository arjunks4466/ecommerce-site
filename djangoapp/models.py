from django.db import models

# Create your models here.

class registers(models.Model):
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    dob=models.DateField()
    password=models.CharField(max_length=20)


class register(models.Model):
    Employee_Name=models.CharField(max_length=30)
    Email_id=models.EmailField()
    Company_Name=models.CharField(max_length=50)
    Designation=models.CharField(max_length=50)
    Phone=models.IntegerField()

# class login(models.Model):
#     email=models.CharField(max_length=30)
#     password=models.IntegerField()





class fileupload(models.Model):
    fname=models.CharField(max_length=20)
    fileimage=models.FileField(upload_to='djangoapp/static')
    description=models.CharField(max_length=200)

class audii(models.Model):
    aname=models.CharField(max_length=20)
    audio=models.FileField(upload_to='djangoapp/static')
    vname=models.CharField(max_length=20)
    video=models.FileField(upload_to='djangoapp/static')
    pname=models.CharField(max_length=20)
    pdf=models.FileField(upload_to='djangoapp/static')


class stat(models.Model):
    choice=[
        ('Kerala','Kerala'), #(database,label(template))
        ('Tamilnadu','Tamilnadu'),
        ('Karnataka','Karnataka')

    ]
    fname=models.CharField(max_length=30)
    state=models.CharField(max_length=30,choices=choice)
    english=models.BooleanField(default=False)
    hindhi=models.BooleanField(default=False)
    other=models.BooleanField(default=False)

class regmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class filemodel(models.Model):
    itemname=models.CharField(max_length=20)
    image=models.FileField(upload_to='media')
    def __str__(self):
        return self.itemname

class imageupload(models.Model):
    item_name=models.CharField(max_length=20)
    image=models.FileField(upload_to='media')
    def __str__(self):
        return self.item_name


class fileuploads_model(models.Model):
    pdfname = models.CharField(max_length=30)
    pdf=models.FileField(upload_to='pdf/')
    audioname=models.CharField(max_length=30)
    audio=models.FileField(upload_to='audio/')
    videoname=models.CharField(max_length=30)
    video=models.FileField(upload_to='video/')
