from django.db import models
from django.contrib.auth.models import User 



class Conversation(models.Model):
    name = models.CharField(max_length=50)
    is_group = models.BooleanField(default=False)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE
    )    
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1) # 1: sent 2: received 3: seen
    img = models.ImageField(
        null=True, blank=True, upload_to = 'media'
    )
   
    def __str__(self):
       return self.text 