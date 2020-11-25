from django.shortcuts import render,redirect,HttpResponse
from pages.models import CompanyHeader
from .models import Service
# Create your views here.
def service(request,pk):
    details=CompanyHeader.objects.all()
    data=Service.objects.all()
    data1 = Service.objects.get(id=pk)
    return render(request,'service.html',{'detail':details,'service':data,'service_data':data1})

