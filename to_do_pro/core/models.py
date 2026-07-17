from django.db import models

# Create your models here.

class Task(models.Model):
    TASK_TYPE = (
        ("daily","Daily"),
        ("goal","Goal")
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    type = models.CharField(choices=TASK_TYPE,default="daily",max_length=10)
    priority = models.CharField(max_length=10,
                                choices=[("high","High"),
                                         ("medium","Medium"),
                                         ("low","Low")],default="medium")
    is_active = models.BooleanField(default=True)


class task_log(models.Model):
    task = models.ForeignKey("Task",
                             on_delete=models.CASCADE,
                             related_name="logs")
    date = models.DateField()
    completed = models.BooleanField(default=False)

    completed_at = models.DateField()

    note = models.TextField()

    class Meta:
        unique_together = ("task","date")
        
            
    

