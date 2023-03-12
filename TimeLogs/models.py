from django.db import models

# TimeLogs is a model that has a team, username, job_number, booking_codes, booking_date,
# time_tracked, and task_estimate.
class TimeLogs(models.Model):
    team = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    job_number = models.CharField(max_length=250)
    booking_codes = models.CharField(max_length=250, null=True)
    booking_date = models.DateField(auto_now=False)
    time_tracked = models.DecimalField(max_digits=5, decimal_places=1)
    task_estimate = models.DecimalField(max_digits=5, decimal_places=1, null=True)


