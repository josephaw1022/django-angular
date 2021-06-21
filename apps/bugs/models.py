from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Bug(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='Problem', blank=True)

    started = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    # For Admin site
    def _str_(self):
        return self.title
