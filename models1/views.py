from django.shortcuts import render
from . import models
# Create your views here.

def dash_model(request):
    
    mdls = models.MainModel.objects.all()
    
    context = {
        'models': mdls,
    }
    return render(request, 'dashboard_templates/models_temp/info.html', context)


def inside_model_view(request, pk):
    
    model_objects = models.InsideModel(md_id = pk)
    context = {
        'model_objects': model_objects,
    }
    return render(request, 'dashboard_templates/models_temp/prezintatsiya.html', context)


def test_view(request):
    
    questions = models.QuestionModel
    
    return render(request, 'dashboard_templates/models_temp/test.html')


