from django.db import models

# Create your models here.
from django.db import models

class MyModel(models.Model):
    # Text field (optional)
    name = models.CharField(max_length=100)

    # Date only
    date_field = models.DateField()

    # Time only
    time_field = models.TimeField()

    # Date + Time
    datetime_field = models.DateTimeField()

    # Auto fields (optional but useful)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Image upload
    image = models.ImageField(upload_to='images/')

    # Resume / file upload
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name