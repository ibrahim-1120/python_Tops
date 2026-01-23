from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
import razorpay

def sendmail(request):
    context = {}
    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request,'email.html',context)
    
def email(request):
    return render(request,'email.html')

def payment(request):
    return render(request,'payment.html')

def pay(request):
    amt=request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))

    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.

    return JsonResponse(payment)