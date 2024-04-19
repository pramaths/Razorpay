import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Subscription
from rest_framework.views import APIView
from rest_framework.response import Response

def webhook_receiver(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        subscription_id = data.get('subscription_id')
        event_type = data.get('event_type')

        # Example to handle different types of webhook events
        try:
            subscription = Subscription.objects.get(razorpay_subscription_id=subscription_id)
            if event_type == 'subscription.paused':
                subscription.pause_status = True
                subscription.active_status = False
            elif event_type == 'subscription.resumed':
                subscription.pause_status = False
                subscription.active_status = True
            elif event_type == 'subscription.cancelled':
                subscription.active_status = False
            subscription.save()
            return JsonResponse({'status': 'success', 'message': 'Subscription updated successfully'})
        except Subscription.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Subscription not found'}, status=404)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

class PingView(APIView):
    def get(self,*args,**kwargs):
        print("hello")
        return Response(data={"ping":"message"})