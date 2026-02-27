from django.db import models

class ChatbotResponse(models.Model):
    intent = models.CharField(max_length=100)
    keywords = models.TextField(help_text="Enter comma separated keywords")
    response = models.TextField()

    def __str__(self):
        return self.intent