from django.urls import path
from .import views

urlpatterns = [
     path('',views.userindex,name='userindex'),
     path('viewcategories',views.viewcategories,name='viewcategories'),
     path('viewproducts/<str:cat>',views.viewproducts,name='viewproducts'),
     path('viewmoreproducts/<int:id>',views.viewmoreproducts,name='viewmoreproducts'),
     path('cart',views.cart,name='cart'),
     path('userreg',views.userreg,name='userreg'),
     path('userlog',views.userlog,name='userlog'),
     path('userregdata',views.userregdata,name='userregdata'),
     path('publicdata',views.publicdata,name='publicdata'),
     path('userlogout',views.userlogout,name='userlogout'),
     path('cartdata/<int:id>',views.cartdata,name='cartdata'),
     path('cartdelete/<int:id>',views.cartdelete,name='cartdelete'),
     path('checkout',views.checkout,name='checkout'),
     path('checkoutdata',views.checkoutdata,name='checkoutdata'),
     path('orders',views.orders,name='orders'),
     path('contact',views.contact,name='contact'),
     path('contactdata',views.contactdata,name='contactdata'),
     path('about',views.about,name='about'),
     path('create_payment',views.create_payment,name='create_payment'),
     path('execute_payment',views.execute_payment,name='execute_payment'),
     path('payment',views.payment,name='payment'),
     path('paysuccess',views.paysuccess,name='paysuccess'),
     path('payerror',views.payerror,name='payerror'),







]
