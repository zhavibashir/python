from django.db import models
from django.contrib.auth.models import User



class Message(models.Model):
    text = models.CharField(max_length=1000)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fromuser")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="touser")
    date = models.DateTimeField(auto_now=True)



