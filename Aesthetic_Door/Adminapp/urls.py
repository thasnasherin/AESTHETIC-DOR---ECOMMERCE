from django.urls import path
from .import views


urlpatterns = [
     path('adminindex',views.adminindex,name='adminindex'),
     path('add_aesthetic_categories',views.add_aesthetic_categories,name='add_aesthetic_categories'),
     path('addcat',views.addcat,name='addcat'),
     path('view_aesthetic_categories',views.view_aesthetic_categories,name='view_aesthetic_categories'),
     path('edit_category/<int:id>',views.edit_category,name='edit_category'),

     path('updatecat/<int:id>',views.updatecat,name='updatecat'),
     path('delete_category/<int:id>',views.delete_category,name='delete_category'),
     path('add_aesthetic_products',views.add_aesthetic_products,name='add_aesthetic_products'),
     path('addpro',views.addpro,name='addpro'),
     path('view_aesthetic_products',views.view_aesthetic_products,name='view_aesthetic_products'),
     path('edit_products/<int:id>',views.edit_products,name='edit_products'),

     path('updatepro/<int:id>',views.updatepro,name='updatepro'),
     path('delete_products/<int:id>',views.delete_products,name='delete_products'),
     path('viewreg',views.viewreg,name='viewreg'),
     path('viewcontact',views.viewcontact,name='viewcontact'),
     path('vieworders',views.vieworders,name='vieworders'),



]
