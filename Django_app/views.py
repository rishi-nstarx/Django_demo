from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world!, This is the home page created by Rishi.")
    return render(request, 'websites/index.html')

def about(request):
    return HttpResponse("Hello world!, This is the about page created by Rishi.")

def contact(request):
    return HttpResponse("Hello world!, This is the contact page created by Rishi.")