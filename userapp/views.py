from django.shortcuts import render,redirect
from django.http import HttpResponse
from adminapp.models import customerinfo,servicerequest
from datetime import timedelta  

#from .forms import UserRequestForm

def mainpage(request):
    return render(request,"Mainpage.html")

def Homepage(request):
    cust = customerinfo.objects.get(first_name=request.session.get("first_name"))
    serve_queryset = servicerequest.objects.filter(customer=cust)
    
    # Calculate adjusted dates for each service request
    adjusted_dates = [serve.request_date + timedelta(hours=3) for serve in serve_queryset]
    
    # Combine service requests and adjusted dates into a list of tuples
    service_data = list(zip(serve_queryset, adjusted_dates))
    
    context = {
        "custs": cust,
        "service_data": service_data,
    }

    return render(request, 'homepage.html', context)


def signup(request):
    if(request.method =="GET"):
        return render(request,"signup.html",{})
    else:
        id=request.POST["id"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        address=request.POST["address"]
        contact_no=request.POST["contact_no"]
        pwd=request.POST["pwd"]
        try :
            user=customerinfo.objects.get(first_name=first_name)
        except :
            user=customerinfo(id,first_name,last_name,email,address,contact_no,pwd)
            user.save()
            return redirect(login)
        else:
            return render(request,"signup.html")

def login(request):
    if(request.method =="GET"):
        return render(request,"login.html",{})
    else:
        first_name=request.POST["first_name"]
        pwd=request.POST["pwd"]
        print(first_name)
        try :
            user=customerinfo.objects.get(first_name=first_name,pwd=pwd) 
        except :
            return redirect(login)
        else:
            print("Else")
            request.session["first_name"]=first_name
            return redirect(Homepage)


def submit_request(request):
    if request.method == 'POST':
        #first_name= request.POST['first_name']
        request_type = request.POST['request_type']
        description = request.POST['description']
        attachment = request.FILES['attachment']

        if request_type and description and attachment:
            # Retrieve the customerinfo object based on the stored session data
            first_name = request.session.get('first_name')
            print(first_name)
            customer_info = customerinfo.objects.get(first_name=first_name)

            # Create a new ServiceRequest instance and save it
            service_request = servicerequest(
                customer=customer_info,
                request_type=request_type,
                details=description,
                attachment=attachment,
                first_name= first_name,
            )
            service_request.save()

            return redirect(Homepage)#Redirect to the home page or another appropriate URL

    return render(request, 'submit_request.html')

def manage_requests(request):
    requests = servicerequest.objects.all()
    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        new_status = request.POST.get('status')
        request = servicerequest.objects.get(id=request_id)
        request.status = new_status
        request.save()
        return redirect('manage_requests')

    return render(request, 'adminui.html', {'requests': requests})

def logout(request):
    request.session.clear()
    return redirect(login)
