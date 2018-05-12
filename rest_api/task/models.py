from django.db import models
from rest_framework import serializers

# Create your models here.
class Task(models.Model):
    title = models.CharField('标题',max_length=100)
    description = models.TextField('描述')
    completed = models.BooleanField('是否完成',default=False)
    create_data = models.DateTimeField('创建时间',auto_now_add=True)
    def __unicode__(self):
        return self.title

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title','description','completed','create_data')