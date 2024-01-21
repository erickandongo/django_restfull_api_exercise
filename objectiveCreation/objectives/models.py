from django.db import models
import uuid

class Objective(models.Model):
    objectives_type_choices = [
        ('financial', 'financial'),
        ('non-financial','non-financial')
        ]
    complexity_choices = [
        ('Hard','Hard'),
        ('Medium','Medium'),
        ('Low','Low')
    ]

    priority_choices = [
        ('High', 'High'),
        ('Low','Low')
    ]
    objective_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    objective_name = models.CharField(max_length= 200, default="default value")
    action_phrase = models.CharField(max_length=200)
    number = models.IntegerField(null=False)
    units = models.CharField(max_length=200)
    deadline = models.DateTimeField(verbose_name = "Dealine")
    objective_type = models.CharField(max_length=200, choices =objectives_type_choices )
    priority = models.CharField(choices=priority_choices, max_length=200 )
    complexity = models.CharField(choices=complexity_choices, max_length=200)
    start_date = models.DateTimeField(verbose_name = "start date")
    end_date = models.DateTimeField(verbose_name = "end date")
    definition_of_good = models.ManyToManyField("DOG")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.objective_name
    
class DOG(models.Model):
    text= models.TextField(max_length =200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

