from django.shortcuts import render,HttpResponse,redirect
import datetime
import requests

# Create your views here.
def home(request):
    
    if request.method == "POST":
        city = request.POST.get("city")

        API_KEY = "your API here"
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        PARAMS = {"units":"metric"}

        data = requests.get(url,PARAMS).json()

        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        temp = data["main"]["temp"]

        day = datetime.date.today()

        return render(request,"home.html",{"description":description,"icon":icon,"temp":temp,"city":city,"day":day})
    
    return render(request,"home.html")