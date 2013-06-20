from django.db import models

class SourceCode(models.Model):
    code = models.TextField()
    name = models.CharField(max_length = 20)
    max_cycle = models.IntegerField(default=1)
    

class Phase(models.Model):
    source_code = models.ForeignKey(SourceCode)
    register = models.TextField()
    memory = models.TextField()
    cycle = models.IntegerField(default=1)

    