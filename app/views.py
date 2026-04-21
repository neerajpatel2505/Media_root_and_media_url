from django.shortcuts import render, redirect
from .models import MyModel

# Create your views here.

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        date_field = request.POST.get('date_field')
        time_field = request.POST.get('time_field')
        datetime_field = request.POST.get('datetime_field')
        image = request.FILES.get('image')
        resume = request.FILES.get('resume')
        print(date_field, time_field, datetime_field, image, resume, name)
        print(type(date_field), type(time_field), type(datetime_field), type(image), type(resume), type(name))
        MyModel.objects.create(
            name=name,
            date_field=date_field,
            time_field=time_field,
            datetime_field=datetime_field,
            image=image,
            resume=resume
        )

        return render(request, 'registration.html')

    return render(request, 'registration.html')