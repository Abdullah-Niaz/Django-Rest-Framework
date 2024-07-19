import uuid
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    is_done  = models.BooleanField(default=False)
    