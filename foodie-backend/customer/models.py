from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from passlib.hash import pbkdf2_sha256


# Create your models here.

class MyCustomerManager(BaseUserManager):
    def create_user(self, customer_email, customer_name, customer_address, customer_phoneNo, customer_dateOfBirth, password=None):
        if not customer_email:
            raise ValueError("User must have an email address")
        if not customer_name:
            raise ValueError("User must have name")
        if not customer_address:
            raise ValueError("User must have an address")

        if not customer_phoneNo:
            raise ValueError("User must have a phone number")
        if not customer_dateOfBirth:
            raise ValueError("User must have a date of birth")
        user = self.model(
            customer_email=self.normalize_email(customer_email),
            customer_name=customer_name,
            customer_phoneNo=customer_phoneNo,
            customer_address=customer_address,
            customer_dateOfBirth=customer_dateOfBirth,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, customer_email,  customer_name,customer_address,customer_phoneNo,customer_dateOfBirth ,password):
        user = self.create_user(
            customer_email=self.normalize_email(customer_email),
            customer_name=customer_name,
            customer_phoneNo=customer_phoneNo,
            customer_address=customer_address,
            customer_dateOfBirth=customer_dateOfBirth,
            password = password,

        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser):
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField(max_length=200)
    customer_email = models.EmailField(max_length=62, unique=True)
    customer_phoneNo = models.CharField(max_length=20)
    customer_accountCreated = models.DateTimeField(auto_now_add=True)
    customer_profilePicture = models.ImageField(upload_to='static/customer_image', blank=True, null=True)
    customer_dateOfBirth = models.DateField(blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'customer_email'
    REQUIRED_FIELDS = ['customer_name', 'customer_phoneNo', 'customer_address', 'customer_dateOfBirth']

    objects = MyCustomerManager()

    def __str__(self):
        return self.customer_email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
