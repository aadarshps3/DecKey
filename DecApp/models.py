from django.db import models

# Create your models here.

sts = (
    ('Completed', 'Completed'),
    ('Incompleted', 'Incompleted'),
    ('Pending', 'Pending')
)


class Work_Details(models.Model):
    work_number = models.IntegerField()
    Date = models.DateField()
    Party = models.CharField(max_length=255)
    Reference = models.CharField(max_length=255)
    Work = models.CharField(max_length=255)
    Details = models.CharField(max_length=255)
    Assign_to = models.CharField(max_length=255)
    Status = models.CharField(max_length=255, choices=sts)
    Finished_date = models.DateField()
    Delivery_Date = models.DateField()
    Bill_Amount = models.CharField(max_length=255)
    Fee_amount = models.CharField(max_length=255)
    DOR = models.CharField(max_length=255)
