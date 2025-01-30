from django.db import models

class task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    TAGS_CHOICES = [ ('trabalho', 'Trabalho'), ('pessoal', 'Pessoal'), ('estudo', 'Estudo'), ('outro', 'Outro') ]
    tags = models.CharField(max_length=15, choices=TAGS_CHOICES, default='outro')
    task_done = models.BooleanField(default=False)


    def __str__(self):
        return self.task_name