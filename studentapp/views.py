from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def home_view(request):
    names = ['Jitendra', 'Rimaljit', 'Mohit', 'Deepak']
    address = ['Chandigarh', 'Ludhiana', 'Ludhiana', 'Ludhian']
    info = zip(names, address)
    data = {
        'info': info
        
    }

    return render(request, 'home.html', context=data)


def about_view(request):
    
    return render(request, 'about.html')


def login_view(request):
    qs = AdmissionDetails.objects.all()
    data = {'queryset': qs}
        
    if (request.method=='POST'):
        
        ad_no = request.POST.get('adno_text')
        name = request.POST.get('name_text')
        section = request.POST.get('class_text')
        
        # orm code to store value in database 
        # admission_details = AdmissionDetails()
        # admission_details.application_no = ad_no
        # admission_details.name = name
        # admission_details.section = section
        # admission_details.save()
        
        # OR

        # admission_details = AdmissionDetails(
        #         application_no = ad_no,
        #         name = name,
        #         section = section
        #     )

        # admission_details.save()
        
        # OR

        AdmissionDetails.objects.create(
                application_no = ad_no,
                name = name,
                section = section
            )
        
        #********************
        
                
    return render(request, 'login.html', context=data)


def delete_view(request):
    id = request.GET.get("id")    
    AdmissionDetails.objects.filter(application_no=id).delete()
    qs = AdmissionDetails.objects.all()
    data = {'queryset': qs}
                
    return render(request, 'login.html', context=data)


def details_view(request):
    id = request.GET.get("id")    
    qs = AdmissionDetails.objects.filter(application_no=id).first()
    data = {'queryset': qs}
                
    return render(request, 'details.html', context=data)


def edit_view(request):
    id = request.GET.get("id")    
    obj = AdmissionDetails.objects.filter(application_no=id).first()
    data = {'queryset': obj}
    
    if (request.method=='POST'):
        ad_no = request.POST.get('adno_text')
        name = request.POST.get('name_text')
        section = request.POST.get('class_text')
        obj.name = name
        obj.section = section
        obj.save()
        return redirect('../login')
                
    return render(request, 'edit.html', context=data)
