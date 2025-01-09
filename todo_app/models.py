from django.db import models

# Create your models here and creating table here
# python manage.py makemigrations and python manage.py migrate (models.py change huda yo duita command chai run garnu parney)
class Todo(models.Model):
    title = models.CharField(max_length=200)
    
