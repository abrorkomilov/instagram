from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from apps.base.models import BaseModel


class User(AbstractUser, BaseModel):
    avatar = models.ImageField(upload_to="avatars/")

    def __str__(self) -> str:
        return self.username
    
class Chat(BaseModel):
    users = models.ManyToManyField(User, related_name='user_chats')

class Message(BaseModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_messages')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_messages')
    text = models.TextField()
