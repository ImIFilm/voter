from django.db import models
from lecturers.models import Lecturer

class Course(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
