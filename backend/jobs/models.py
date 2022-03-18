from django.db import models
from authentication.models import User, Worker
from django.conf import settings
import math

class Status(models.TextChoices):
    AVAILABLE = 'available'
    ASSIGNED = 'assigned'
    COMPLETE = 'complete'
    DISPUTED = 'disputed'


class JobType(models.Model):
    job_type = models.CharField(max_length=50, null=False)
    icon = models.CharField(max_length=100, null=False)
    archived = models.BooleanField(null=False, default=False)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    price = models.FloatField()
    time_estimate = models.FloatField()
    start_time = models.BigIntegerField(default=0, null=False)
    end_time = models.BigIntegerField(default=0, null=False)
    address = models.CharField(max_length=150)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    comment = models.CharField(max_length=150)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.AVAILABLE)

    job_type = models.OneToOneField(JobType, on_delete=models.SET_NULL, null=True)

class WorkerJobTimes(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    start_time = models.BigIntegerField(default=0, null=False)
    end_time = models.BigIntegerField(default=0, null=False)

    def assign_job(self):
        # creating variables to make code in future less confusing when doing the math
        userLat = self.job.latitude / 57.29577951
        userLong = self.job.longitude / 57.29577951
        workerLat = self.worker.user.home_latitude / 57.29577951
        workerLong = self.worker.user.home_longitude / 57.29577951
        # 57.29577951 is approximately 180/PI, so converts values from degrees to radians

        Distance = 3963.0 * math.arccos[(math.sin(userLat) * math.sin(workerLat)) + math.cos(userLat) *
                                        math.cos(workerLat) * math.cos(workerLong - userLong)]

        # formula from https://www.geeksforgeeks.org/program-distance-two-points-earth/

        Distance = abs(Distance)

        if Distance < 25:
            for i in self.WorkerAvailability

            self.job.status = 'assigned'



