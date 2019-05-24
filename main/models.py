from django.db import models

# Create your models here.
class Problem(models.Model):
    name=models.CharField(max_length=200,blank=False,null=False)
    code=models.CharField(max_length=200,blank=False,null=False)
    url=models.CharField(max_length=200,blank=False,null=False)
    status=models.CharField(max_length=200,blank=False,null=False)
    accuracy=models.CharField(max_length=200,blank=False,null=False)
    submissions=models.CharField(max_length=200,blank=False,null=False)
    submit_url=models.CharField(max_length=200,blank=False,null=False)
    question_type=models.CharField(max_length=200,blank=False,null=False)
    def __str__(self):
        return self.code

    def __unicode(self):
        return self.codes