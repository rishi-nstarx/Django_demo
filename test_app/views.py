from django.shortcuts import render
from .models import PersonalInfo
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    info = PersonalInfo.objects.all()
    return render(request, 'test_app/all_test_app.html', {'infos': info})

def details(request, info_id):
    details = get_object_or_404(PersonalInfo, pk=info_id)
    return render(request, 'test_app/detailed_info.html', {'details': details})

