from django.shortcuts import render,redirect
from Adminapp.models import*
from.models import*
import paypalrestsdk
from django.conf import settings
# Create your views here.
def userindex(request):
    cat=Category.objects.all()
    pro=Product.objects.all()
    return render(request,'userindex.html',{'cat':cat, 'pro':pro})

def viewcategories(request):
    cat=Category.objects.all()
    return render(request,'viewcategories.html',{'cat':cat})

def viewproducts(request,cat):
    if cat=='all':
        pro=Product.objects.all()
    else:
        pro=Product.objects.filter(pcat=cat)
    return render(request,'viewproducts.html',{'pro':pro})

def wishlist(request):
    pro=Product.objects.filter(status=1)
    return render(request,'wishlist.html',{'pro':pro})

def addtowish(request,id):
    Product.objects.filter(id=id).update(status=1)
    return redirect('wishlist')

def removewish(request,id):
    Product.objects.filter(id=id).update(status=2)
    return redirect('wishlist')

def viewmoreproducts(request,id):
    if 'u_id' in request.session:
        pro=Product.objects.filter(id=id)
        return render(request,'viewmoreproducts.html',{'pro':pro})
    return render(request,'userlog.html',{'msg1':'You need to Login First to access this page'})

def userreg(request):
    return render(request,'userreg.html')

def userlog(request):
    return render(request,'userlog.html')

def userregdata(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        data=Register(username=username,password=password,email=email,phone=phone)
        data.save()
    return redirect('userreg')

def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('pass')
        if Register.objects.filter(username=username,password=password).exists():
           data = Register.objects.filter(username=username,password=password).values('id','phone','email').first()
        
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['phone'] 
           request.session['email_u'] = data['email'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('userindex') 
        else:
            return render(request,'userlog.html',{'msg':'invalid user credentials'})
    else:
        return redirect('userindex')

def userlogout(request):

    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('userindex')

def cart(request):
    if 'u_id' in request.session:
       u=request.session.get('u_id')
       data=Cart.objects.filter(userid=u,status=0)
       return render(request,'cart.html',{'data':data})
    return render(request,'userlog.html',{'msg1':'You need to Login First to access this page'})
    

def cartdata(request,id):
    if request.method =='POST':
        u=request.session.get('u_id')
        q=request.POST.get('quantity')
        t=request.POST.get('total')
        data=Cart(userid=Register.objects.get(id=u),productid=Product.objects.get(id=id),quantity=q,total=t)
        data.save()
        return redirect('cart')
    
def cartdelete(request,id):
    Cart.objects.get(id=id).delete()
    return redirect('cart')

def checkout(request):
  if 'u_id' in request.session:
    u=request.session.get('u_id')
    data=Cart.objects.filter(userid=u,status=0)
    return render(request,'checkout.html',{'data':data})
  return render(request,'userlog.html',{'msg1':'You need to Login First to access this page'})
  

def checkoutdata(request):
    if request.method == 'POST':
        u=request.session.get('u_id')
        address=request.POST.get('address')
        pin=request.POST.get('pin')
        country=request.POST.get('country')
        ccart=Cart.objects.filter(userid=u,status=0)
        for i in ccart:
            data=Checkout(userid=Register.objects.get(id=u),cartid=Cart.objects.get(id=i.id),address=address,pincode=pin,country=country)
            data.save()
            Cart.objects.filter(id=i.id).update(status=1)
        return redirect('payment')
def payment(request):
    return render(request,'payment.html')

def paymentsuccess(request):
    return render(request,'paysuccess.html')

def error(request):
    return render(request,'payerror.html')

#----------------------------------------------------------------------------------------------------------------
#PAYPAL PAYMENT GATEWAY
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})
def create_payment(request):
    if request.method == 'POST':
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal",
            },
            "redirect_urls": {
                "return_url": "http://127.0.0.1:8000/execute_payment",
                "cancel_url": "http://127.0.0.1:8000/error",
            },
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "Test Item",
                        "sku": "001",
                        "price": "10.00",
                        "currency": "USD",
                        "quantity": 1
                    }]
                },
                "amount": {
                    "total": "10.00",
                    "currency": "USD"
                },
                "description": "Test Payment"
            }]
        })

        # Attempt to create the payment on PayPal
        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    return redirect(link.href)  # Redirect to PayPal approval URL
        else:
            return render(request, 'payerror.html', {'error': payment.error})

    return render(request, 'payment.html')
# def create_payment(request):
#     if request.method == 'POST':
#         payment=paypalrestsdk.Payment({
#             "intent":"sale",
#             "payer":{
#                 "payment_method":"paypal",
#             },
#             "redirect_urls":{
#                 "return_url":"http://127.0.0.1:8000/paymentsuccess",
#                 "cancel_url":"http://127.0.0.1:8000/error",
#             },
#             "transactions":[{
#                 "items_list":{
#                     "items":[{
#                        "name":"Test Item",
#                        "sku":"001",
#                        "price":"10",
#                        "currency":"INR",
#                        "quantity":1
#                     }]
#                 },
#                 "amount":{
#                     "total":"10",
#                     "currency":"INR"
#                 },
#                 "description":"This is a test Payment"
#             }]
#         })
#         if payment.create():
#             for link in payment.links:
#                 if link.rel == "approval_url":
#                     return redirect(link.href)
#                 else:
#                     return render(request,'error.html',{'error':payment.error})
#     return render(request,'payment.html')
def execute_payment(request):
    paymentid=request.GET.get('payment_id')
    payerid=request.GET.get('payer_id')
    payment=paypalrestsdk.Payment.find(paymentid)
    if payment.execute({'payerid':payerid}):
        return render(request,'paysuccess.html',{'payment':payment})
    else:
        return render(request,'payerror.html',{'error':payment.error})

#----------------------------------------------------------------------------------------------------------------



def orders(request):
    if 'u_id' in request.session:
        u=request.session.get('u_id')
        data=Checkout.objects.filter(userid=u)
        return render(request,'orders.html',{'data':data})
    return render(request,'userlog.html',{'msg1':'You need to Login First to access this page'})
    

def contact(request):
    return render(request,'contact.html')

def feedbacksuccess(request):
    return render(request,'feedbacksuccess.html')

def contactdata(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        data=Contact(name=name,email=email,message=message)
        data.save()
        return redirect('feedbacksuccess')
    
def about(request):
    return render(request,'about.html')

#----------------------------------------------------------------------------------------------------------------
#PAYPAL PAYMENT GATEWAY
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})
def create_payment(request):
    if request.method == 'POST':
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal",
            },
            "redirect_urls": {
                "return_url": "http://127.0.0.1:8000/execute_payment",
                "cancel_url": "http://127.0.0.1:8000/payerror",
            },
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "Test Item",
                        "sku": "001",
                        "price": "10.00",
                        "currency": "USD",
                        "quantity": 1
                    }]
                },
                "amount": {
                    "total": "10.00",
                    "currency": "USD"
                },
                "description": "Test Payment"
            }]
        })

        # Attempt to create the payment on PayPal
        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    return redirect(link.href)  # Redirect to PayPal approval URL
        else:
            return render(request, 'error.html', {'error': payment.error})

    return render(request, 'payment.html')
# def create_payment(request):
#     if request.method == 'POST':
#         payment=paypalrestsdk.Payment({
#             "intent":"sale",
#             "payer":{
#                 "payment_method":"paypal",
#             },
#             "redirect_urls":{
#                 "return_url":"http://127.0.0.1:8000/paymentsuccess",
#                 "cancel_url":"http://127.0.0.1:8000/error",
#             },
#             "transactions":[{
#                 "items_list":{
#                     "items":[{
#                        "name":"Test Item",
#                        "sku":"001",
#                        "price":"10",
#                        "currency":"INR",
#                        "quantity":1
#                     }]
#                 },
#                 "amount":{
#                     "total":"10",
#                     "currency":"INR"
#                 },
#                 "description":"This is a test Payment"
#             }]
#         })
#         if payment.create():
#             for link in payment.links:
#                 if link.rel == "approval_url":
#                     return redirect(link.href)
#                 else:
#                     return render(request,'error.html',{'error':payment.error})
#     return render(request,'payment.html')
def execute_payment(request):
    paymentid=request.GET.get('payment_id')
    payerid=request.GET.get('payer_id')
    payment=paypalrestsdk.Payment.find(paymentid)
    if payment.execute({'payerid':payerid}):
        return render(request,'paysuccess.html',{'payment':payment})
    else:
        return render(request,'payerror.html',{'error':payment.error})
    
def payment(request):
    if 'u_id' in request.session:
       return render(request,'payment.html')
    return render(request,'userlog.html',{'msg1':'You need to Login First to access this page'})
    

def paysuccess(request):
    if 'u_id' in request.session:
       return render(request,'paysuccess.html')
    return render(request,'userlog.html',{'msg1':'You need to Login First to access this page'})
    

def payerror(request):
    if 'u_id' in request.session:
       return render(request,'payerror.html')
    return render(request,'userlog.html',{'msg1':'You need to Login First to access this page'})
    

#----------------------------------------------------------------------------------------------------------------