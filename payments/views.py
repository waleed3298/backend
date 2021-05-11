from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import stripe
import json
from django.views.decorators.csrf import csrf_exempt
import math
stripe.api_key = "sk_test_51HpEAFBvgj2EIc8TcbG48FSuuMtpy9nDxKSIjM7qRnoRTRKg9UduHwAFyKTnVgIPwIhrf4W2enAhpY0tGVoSbvak00DkE8kEup"


@api_view(["POST"])
def test_payment(request):
    data = request.data
    test_payment_intent = stripe.PaymentIntent.create(
        amount=math.trunc(data['amount']),
        currency="pln",
        payment_method_types=["card"],
        receipt_email="test@example.com",
    )
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)


@api_view(["POST"])
def save_stripe_info(request):
    data = request.data
    email = data["email"]
    payment_method_id = data["payment_method_id"]
    extra_msg = ""  # add new variable to response message
    # checking if customer with provided email already exists
    customer_data = stripe.Customer.list(email=email).data

    # if the array is empty it means the email has not been used yet
    if len(customer_data) == 0:
        # creating customer
        customer = stripe.Customer.create(email=email, payment_method=payment_method_id)
    else:
        customer = customer_data[0]
        extra_msg = "Customer already existed."
    stripe.PaymentIntent.create(
        customer=customer,
        payment_method=payment_method_id,
        currency="pkr",  # you can provide any currency you want
        amount=math.trunc(data['amount']),
        confirm=True,
    )
    return Response(
        status=status.HTTP_200_OK,
        data={
            "message": "Success",
            "data": {"customer_id": customer.id, "extra_msg": extra_msg},
        },
    )
