from django.shortcuts import render
def page1(request):
    return render(request,"index.html")
def page2(request1):
    return render(request1,"appointment.html")
def page3(request2):
    return render(request2,"login-page.html")
# Create your views here.
