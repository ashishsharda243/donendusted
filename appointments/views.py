from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Appointment, DateTime,Services
from datetime import date, datetime
import pandas as pd
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.


def appointment(request):
    services =  Services.objects.all()
    if request.method == "POST":
    
        dateValue = datetime.strptime(request.POST.get("date"), "%Y-%m-%d")
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        category = request.POST.get("category")
        timeValue = request.POST.get("time")
        # amount = request.POST.get("amount")

        appoint = Appointment()
        appoint.name = name
        appoint.email = email
        appoint.mobile = mobile
        appoint.service = category
        appoint.date = dateValue
        appoint.time = timeValue
        # appoint.amount = amount
        appoint.save()

        return render(request, 'appointments/appointment.html', { "message": "Your appointment has been booked.",'services':services})

    return render(request, 'appointments/appointment.html',{'services':services})


def appointmentTime(request):
    dateValue = datetime.strptime(request.GET.get('date'), "%Y-%m-%d")
    serv = request.GET.get("service","")
    if not serv :
        return JsonResponse({'message':""})
    ser = Services.objects.get(service = serv)
    print("*****")
    print(ser.freq)
    currentDate = DateTime.objects.get(date=dateValue)
    startTime = currentDate.fromTime
    endTime = currentDate.fromTo
    # freq = currentDate.freq
    
    try:
        timeLists = pd.date_range(str(startTime), str(endTime), freq=ser.freq+"min").time
        df = pd.DataFrame({"Time" : timeLists})
        
        recordList = []
        records = Appointment.objects.filter(date = dateValue).values_list('time', flat=True)
        for record in records:
            recordList.append(record)
        df['status'] = df['Time'].apply(lambda x : 0 if x not in recordList else 1)
        timeList = df['Time'].to_list()
        statusList = df['status'].to_list()
    except Exception as e:
        
        timeList = [1, 2, 3, 4, 5, 6, 7, 8]
        statusList = [0,0,1,0,1,0,0,1]
        
    return JsonResponse({"timeList" : timeList, "statusList" : statusList}, safe=False)

def cancelAppointment(request):
    id = request.GET.get('id')
    appoint = Appointment.objects.get(appointId=id)
    appoint.status = 2
    appoint.save()
    print(appoint)
    return HttpResponse("#"+id)

def completedAppointment(request):
    id = request.GET.get('id')
    appoint = Appointment.objects.get(appointId=id)
    appoint.status = 3
    appoint.save()
    print(appoint)
    return HttpResponse("#"+id)



def staff(request):
    appoints = Appointment.objects.filter(status = 1)
    cancelApoints = Appointment.objects.filter(status = 2)
    completedApoints = Appointment.objects.filter(status = 3)
    
    return render(request,"staff/staff.html",{'appoints':appoints,'cancelApoints':cancelApoints,'completedApoints':completedApoints})

    

