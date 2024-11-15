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

    def __str__(self) -> str:
        return self.desc + "/t|\t" + self.author.username
    
    class BookMark(BaseModel):
        author = models.ForeignKey(User, on_delete=models.CASCADE
                                   related_name="user_bookmarks")
        target = models.ForeignKey(Photo, on_delete=models.CASCADE, 
                                   related_name="photo_bookmarks")
        
    def __str__(self) -> str:
        return f"{self.author.username} -> {self.target.desc}"

class Like(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE
                                   related_name="user_likes")
    target = models.ForeignKey(Photo, on_delete=models.CASCADE, 
                                   related_name="photo_likes")
    
    def __str__(self) -> str:
        return f"{self.author.username} -> {self.target.desc}"
    
class Commet(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE
                                   related_name="user_comments")
    target = models.ForeignKey(Photo, on_delete=models.CASCADE, 
                                   related_name="photo_comments")
    text = models.TextField()

    def __str__(self) -> str:
        return f"{self.author.username} -> {self.target.desc}"
    
class Subscribe(BaseModel):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, 
                              related_name='user_subscribes')
    target = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='user_subscibers')
    
    def __str__(self) -> str:
        return f"{self.autor.username} -> {self.target.username}"
    