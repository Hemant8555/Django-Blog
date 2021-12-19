from django.db import models

# Create your models here.


class funding_request(models.Model):
 
    STAGE = (
        ("Idea",  ('Idea')),
        ("Concept", ('Concept')),
        ("Established", ('Established')),
    )
    REGISTRATION = (
        ("Yes", ('Yes')),
        ("No", ('No')),
    )
    title = models.CharField(max_length=100, null=False, blank=False)
    stage = models.CharField(max_length=30, choices=STAGE, null=False, default=1)
    problem = models.TextField(max_length=500)
    solution = models.TextField(max_length=500)
    company = models.CharField(max_length=30,choices=REGISTRATION, default=2)

    def __str__(self):
        return str(self.title)

