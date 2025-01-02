from django.shortcuts import render,redirect
from.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Userapp.models import*
# Create your views here.
def adminindex(request):
    cat=Category.objects.all().count()
    pro=Product.objects.all().count()
    reg=Register.objects.all().count()
    con=Contact.objects.all().count()
    ord=Checkout.objects.all().count()
    return render(request,'adminindex.html',{'cat':cat,'pro':pro,'reg':reg,'con':con,'ord':ord})

def add_aesthetic_categories(request):
    return render(request,'add_aesthetic_categories.html')

def addcat(request):
    if request.method == 'POST':
        cname=request.POST['cname']
        cdesc=request.POST['cdesc']
        cimage=request.FILES['cimage']
        data=Category(cname=cname, cdesc=cdesc, cimage=cimage)
        data.save()
        return redirect('view_aesthetic_categories')
    
def view_aesthetic_categories(request):
    cat=Category.objects.all()
    return render(request,'view_aesthetic_categories.html',{'cat':cat})

def edit_category(request,id):
    data=Category.objects.filter(id=id)
    return render(request,'edit_category.html',{'data':data})

def updatecat(request,id):
    if request.method == 'POST':
        cname=request.POST['cname']
        cdesc=request.POST['cdesc']
        # try:
        #     img_c = request.FILES['cimage']
        #     fs = FileSystemStorage()
        #     file = fs.save(img_c.name, img_c)
        # except MultiValueDictKeyError:
        #     file = Category.objects.get(id=id).cimage
        Category.objects.filter(id=id).update(cname=cname, cdesc=cdesc, cimage=file)
    return redirect('view_aesthetic_categories')

def delete_category(request,id):
    data=Category.objects.filter(id=id).delete()
    return redirect('view_aesthetic_categories')

def add_aesthetic_products(request):
    cat=Category.objects.all()
    return render(request,'add_aesthetic_products.html',{'cat':cat})

def addpro(request):
    if request.method == 'POST':
        pname=request.POST['pname']
        pcat=request.POST['pcat']
        pprice=request.POST['pprice']
        pstock=request.POST['pstock']
        pimage=request.FILES['pimage']
        data=Product(pname=pname, pcat=pcat, pprice=pprice,pstock=pstock,pimage=pimage)
        data.save()
        return redirect('view_aesthetic_products')
    
def view_aesthetic_products(request):
    pro=Product.objects.all()
    return render(request,'view_aesthetic_products.html',{'pro':pro})

def edit_products(request,id):
    cat=Category.objects.all()
    data=Product.objects.filter(id=id)
    return render(request,'edit_products.html',{'data':data,'cat':cat})

def updatepro(request,id):
    if request.method == 'POST':
        pname=request.POST['pname']
        pcat=request.POST['pcat']
        pprice=request.POST['pprice']
        pstock=request.POST['pstock']
        try:
            pimage=request.FILES['pimage']
            fs = FileSystemStorage()
            file = fs.save(pimage.name, pimage)
        except MultiValueDictKeyError:
            file = Product.objects.get(id=id).pimage
        Product.objects.filter(id=id).update(pname=pname, pcat=pcat, pprice=pprice,pstock=pstock,pimage=file)
    return redirect('view_aesthetic_products')

def delete_products(request,id):
    data=Product.objects.filter(id=id).delete()
    return redirect('view_aesthetic_products')

def viewreg(request):
    data=Register.objects.all()
    return render(request,'viewreg.html',{'data':data})

def viewcontact(request):
    data=Contact.objects.all()
    return render(request,'viewcontact.html',{'data':data})

def vieworders(request):
    data=Checkout.objects.all()
    return render(request,'vieworders.html',{'data':data})
