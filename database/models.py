from django.db import models

class SourceCode(models.Model):
    code = models.TextField()
    maxcycle = models.IntegerField(default=1)
    name = models.CharField(max_length = 20)
    

class Phase(models.Model):
    source_code = models.ForeignKey(SourceCode)
    register = models.TextField()
    memory = models.TextField()
    cycle = models.IntegerField()

    
    
