from django.db import models


# Create your models here.
class Zadacha(models.Model):
    # id = models.AutoField(auto_created=True, primary_key=True)
    y = "yes"
    n = "no"
    complete = [(y,"YES"), (n, "NO")]
    title = models.CharField(max_length=100, null=True)
    text = models.TextField()
    date = models.DateField()
    task_completed = models.CharField(max_length=100,
        choices=complete, default=n,)


    class Meta:
        db_table = 'zadacha'

    def __str__(self):
        return self.title
