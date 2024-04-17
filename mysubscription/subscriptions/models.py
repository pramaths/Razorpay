from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    razorpay_subscription_id = models.CharField(max_length=100, blank=True, null=True)
    plan = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    subscription_start_date = models.DateField(default=now)
    subscription_period = models.IntegerField(help_text="Subscription period in days")
    active_status = models.BooleanField(default=True)
    pause_status = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan}"
