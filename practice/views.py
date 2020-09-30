from django.shortcuts import render
# Create your views here.
from api.models import NewUser





def practiceViews(request):
    data = NewUser.objects.all()
    # a = NewUser.objects.all()
    #
    # a.delete()
    #
    return render(request, 'template.html', {"data" : data})
