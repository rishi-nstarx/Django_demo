from django.shortcuts import render
from .models import PersonalInfo
from django.shortcuts import get_object_or_404

from .models import PersonalInfo, Plateform
from .forms import PersonalInfoForm

# Create your views here.
def home(request):
    info = PersonalInfo.objects.all()
    return render(request, 'test_app/all_test_app.html', {'infos': info})

def details(request, info_id):
    details = get_object_or_404(PersonalInfo, pk=info_id)
    return render(request, 'test_app/detailed_info.html', {'details': details})

def plateform_view(request):
    plateforms = None
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            personal_info = form.cleaned_data['personal_info']
            plateforms = Plateform.objects.filter(infos = personal_info)
    else:
        form = PersonalInfoForm()
    
    return render(request, 'test_app/info_plateform.html', {'form':form, 'plateforms':plateforms})


