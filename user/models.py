from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from admins.models import grade

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        # if not username:
        #     raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            # username = username,
            # first_name = first_name,
            # last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user





class School(AbstractBaseUser):
    email     = models.CharField(max_length=50,unique=True)
    name      = models.CharField(max_length=50)
    city      = models.CharField(max_length=50)
    pin_code  = models.IntegerField()
    # required
    date_joined     = models.DateTimeField(auto_now_add=True,null=True)
    last_login      = models.DateTimeField(auto_now_add=True,null=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    is_superadmin    = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = MyAccountManager()
    


class Student(models.Model):
    name = models.CharField(max_length=50,blank=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    school_id = models.ForeignKey(School,on_delete=models.CASCADE,related_name='school')
    class_id = models.ForeignKey(grade,on_delete=models.CASCADE,related_name='grade',null=True)
