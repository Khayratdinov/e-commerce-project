from django.shortcuts import render
# ============================================================================ #
from project.apps.common.models import HomeSlider
# Create your views here.



def index(request):
    home_sliders = HomeSlider.objects.all()[:3]

    context = {

        'home_sliders': home_sliders,

    }

    return render(request, 'index.html', context)
