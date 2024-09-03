from django.shortcuts import render
from django.http import HttpResponse
from.models import Datas

# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        password=request.POST['pass']
        cpassword=request.POST['cpass']
       

        obj=Datas()
        obj.Name=name
        obj.Email=email
        obj.Address=address
        obj.Password=password
        obj.Cpassword=cpassword
        obj.save()

    return render(request,"reg.html")
    