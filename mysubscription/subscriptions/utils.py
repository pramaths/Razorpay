import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

def create_razorpay_subscription(plan_id, total_count, customer_id):
    data = {
        "plan_id": plan_id,
        "total_count": total_count,
        "customer_id": customer_id,
    }
    return client.subscription.create(data=data)
