from django.db import models

# Create your models here.

class Info(models.Model):

    #index = models.AutoField(primary_key=True, default=1)
    category = models.CharField(max_length = 100, null=True)
    link = models.CharField(max_length = 500)

    """def save(self, *args, **kwargs):
        if self.index == 0:
            self.index = 1;
        else:
            i = Info.objects.all().order_by('-index')[0]
            self.index = i.index+1
        super(Info, self).save(*args, **kwargs)"""
#    def __str__(self):
#        return self.type

