from django.db import models

class Message(models.Model): 
    id = models.AutoField(primary_key=True) 
    message = models.CharField(max_length=50)
    date_time_received = models.DateTimeField(auto_now_add=True)
    date_time_sending = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Comunicação: {self.id}'
