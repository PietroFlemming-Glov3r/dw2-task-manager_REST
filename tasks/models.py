from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    TAGS_CHOICES = [ ('Trabalho', 'Trabalho'),
                     ('Pessoal', 'Pessoal'),
                     ('Estudo', 'Estudo'),
                     ('Outro', 'Outro') ]
    tags = models.CharField(max_length=15, choices=TAGS_CHOICES, default='outro')
    done = models.BooleanField(default=False)
    deadline = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name