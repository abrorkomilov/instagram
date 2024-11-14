from django.db import models
from apps.base.models import BaseModel
from apps.accounts.models import User

# Create your models here.
class Tag(BaseModel):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    


class Photo(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Yaratuvchi", related_name="user_photos")
    image = models.ImageField(upload_to="images/")
    desc = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag, related_name="tag_photos")

