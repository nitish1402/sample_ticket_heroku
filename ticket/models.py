from django.db import models

class Ureg(models.Model):
    uname = models.CharField(max_length=20)
    umail = models.EmailField()
    upass = models.CharField(max_length=30)
    uphone = models.CharField(max_length=10)
    uaddr = models.TextField()
    urole = models.CharField(max_length=20)

    def __str__(self):
        return self.umail

class Treg(models.Model):
    tmail = models.EmailField()
    tname = models.CharField(max_length=30,blank=True,null=True,default='Please update')
    tcity = models.CharField(max_length=30, blank=True, null=True, default='Please update')
    tloc = models.CharField(max_length=30, blank=True, null=True, default='Please update')
    tmorn_img = models.ImageField(upload_to='',blank=True,null=True)
    tmorn_name = models.CharField(max_length=30,blank=True,null=True,default='No Movie Name')
    tafter_img = models.ImageField(upload_to='', blank=True,null=True)
    tafter_name = models.CharField(max_length=30,blank=True,null=True,default='No Movie Name')
    teve_img = models.ImageField(upload_to='',blank=True,null=True)
    teve_name = models.CharField(max_length=30,blank=True,null=True,default='No Movie Name')
    tcost = models.IntegerField(default=150,blank=True,null=True)
    tdate = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.tmail

class Movie(models.Model):
    mname = models.CharField(max_length=30)
    mimg = models.ImageField(upload_to='',blank=True,null=True)
    mcity = models.CharField(max_length=30,default='')
    def __str__(self):
        return self.mname

class Slot(models.Model):
    sumail = models.CharField(max_length=30,blank=True,null=True)
    stname = models.CharField(max_length=30,blank=True,null=True)
    stdate = models.DateField(blank=True,null=True)
    sshowname = models.CharField(max_length=30,blank=True,null=True)
    sshowtype = models.CharField(max_length=30,blank=True,null=True)
    sid = models.IntegerField(default=0)
    sslot = models.CharField(max_length=30,blank=True,null=True)
    stcost = models.IntegerField(blank=True,null=True)
    sstat = models.CharField(default='no',max_length=3)
    scity = models.CharField(default='',blank=True,null=True,max_length=30)

    def __str__(self):
        return self.sumail


class Sample(models.Model):
    sname = models.CharField(max_length=20)

    def __str__(self):
        return self.sname

