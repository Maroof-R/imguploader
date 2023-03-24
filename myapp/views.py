from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.

def home(request):
    if request.method =='POST':
        file = ImageForm(request, request.FILES)
        if file.is_valid():
            file.save()

    form = ImageForm()
    img = Image.objects.all()

    return render(request, 'myapp/home.html' ,{'form':form, 'img':img})