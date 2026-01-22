from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import razorpay

def email(request):
    return render(request,'email.html')

def payment(request):
    return render(request,'payment.html')

def pay(request):
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))

    data = { "amount": 50000, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.

    return HttpResponse(payment)