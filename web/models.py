from django.db import models

# Create your models here.
class Entries(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    url = models.TextField()
    date_created = models.TextField()
    timestamp = models.FloatField()

    class Meta:
        db_table = 'entries'

    def __str__(self):
        return str(self.title)
