from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

LEVEL_CHOICES = [(i, str(i)) for i in range(1, 6)]

# Create your models here.
class ToDoModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=30)
    level=models.IntegerField(choices=LEVEL_CHOICES,default=1)
    is_completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(default=timezone.now)
    finished_time=models.DateTimeField(null=True,blank=True)
    
    
    def complete_task(self):
        if self.is_completed ==True:
            self.finished_time = timezone.now()
            self.save()
        
    
    def __str__(self) -> str:
        return self.title
