from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from PIL import Image
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='def.png', upload_to='profile')


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created =  models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return self.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            with Image.open(self.image.path) as im:
                if im.width > 300 or im.height > 300:
                    output = (300, 300)
                    im.thumbnail(output)
                    im.save(self.image.path)


    def send_email(self):
        pass
