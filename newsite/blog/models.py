# chatbot/models.py

from ckeditor.fields import RichTextField
from django.db import models


class Interaction(models.Model):
    user_input = RichTextField()
    bot_response = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
