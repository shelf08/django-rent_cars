from django.shortcuts import render

# Create your views here.
def auto_home(request):
    return render(request,  'auto/auto_home.html')