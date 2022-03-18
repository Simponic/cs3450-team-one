from django.db import models
from authentication.models import User
from job.models import User

class Status(models.TextChoices):
    RESOLVED = 'resolved'
    OPEN = 'open'

# Create your models here.
class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    body = models.CharField(max_length=500, null=False)
    status = models.CharField(
            max_length=20,
            choices=Status.choices,
            default=Status.OPEN)

    def create_new_submission(self, submission):
        self.submission = submission
        self.status = Status.OPEN
