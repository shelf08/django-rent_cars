from django.shortcuts import render

# Create your views here.
def tables_home(request):
    return render(request,  'tables/tables_home.html')