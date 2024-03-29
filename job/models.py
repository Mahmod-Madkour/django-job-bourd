from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),

)

class Category(models.Model):
    name = models.CharField(max_length = 25)

    def __str__ (self):
        return self.name

class Job(models.Model):                            # cl;ass == table in database
    title = models.CharField(max_length = 100)      # this is line == column in database
    job_type = models.CharField(max_length = 15, choices = JOB_TYPE)
    description = models.TextField(max_length = 1000)
    published_at = models.DateTimeField(auto_now = True)
    vacancy = models.IntegerField(default = 1)
    salary = models.IntegerField(default = 0)
    experience  = models.IntegerField(default = 1)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, )

    def __str__ (self):
        return self.title




