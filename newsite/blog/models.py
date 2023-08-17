# chatbot/models.py

from django.db import models
from ckeditor.fields import RichTextField

class Interaction(models.Model):
    user_input = RichTextField()
    bot_response = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
