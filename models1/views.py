from django.shortcuts import redirect, render
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse


# Create your views here.

def dash_model(request):
    
    description = models.DescriptModel.objects.filter(m_id=1).first()
    mdls = models.MainModel.objects.all()
    contents = models.DesContentModel.objects.filter(des=description)
    for i in mdls:
        print('Pk: ', i.id)
    context = {
        'models': mdls,
        'description': description,
        'contents': contents
    }
    return render(request, 'dashboard_templates/models_temp/info.html', context)


# def universal_view_2(request):
    

def universal_view(request, pk, model_id):
    objects = models.InsideModel.objects.filter(m_id = model_id)
    b_id = models.InsideModel.objects.get(id=pk)
    files = models.FileModel.objects.filter(inside_model=b_id)
    contents = models.InlineModelContent.objects.filter(inside_model=b_id)
    universal_sources = []
    documents = []
    anothers = []
    print('filelar', universal_sources)
    print(object)
    for file in files:
        print('File_type: ', file.file_type)
        if file.file_type != 'Documents': 
            
            anothers.append(file)
            universal_sources.append(file)
        else:
            documents.append(file)
    for content in contents:
        universal_sources.append(content)
  
    n_p = 0
    for ob in objects:  # hozirgi page raqamini aniqlash
        n_p +=1
        if ob == b_id:
            break
    
    
    hozirgi_page = n_p
    keyingi_page = n_p +1
    # Pagega chiqadigan ma'lumotlarimini saralayman

    
    c_objects = objects.count()
    songi_page = c_objects
    test_num = c_objects + 1 # test raqami
    print('Songi page: ', c_objects)
    print('Documents: ', documents)
    
    context = {
            'objects': objects,
            'model_id': model_id,
            'universal_sources': universal_sources,
            'test_num': test_num,
            'hozirgi_page': hozirgi_page,
            'keyingi_page': keyingi_page,
            'songi_page': songi_page,
            'documents': documents,
            'contents': contents,
        }
    if len(documents) > len(anothers):
        # return redirect('home')
        return render(request, 'dashboard_templates/documents.html', context)

    return render(request, 'dashboard_templates/models_temp/universal.html', context)



def inside_model_view(request, pk):
    model = models.MainModel.objects.get(id=pk)
    objects = models.InsideModel.objects.filter(m_id = model)
    b_id = models.InsideModel.objects.get(id=objects.first().id )
    files = models.FileModel.objects.filter(inside_model=b_id)
    contents = models.InlineModelContent.objects.filter(inside_model=b_id)
    universal_sources = []
    
    for file in files:
        universal_sources.append(file)
    for content in contents:
        universal_sources.append(content)
  
    n_p = 0
    for ob in objects:  # hozirgi page raqamini aniqlash
        n_p +=1
        if ob == b_id:
            break
    
    
    hozirgi_page = n_p
    keyingi_page = n_p +1
    # Pagega chiqadigan ma'lumotlarimini saralayman
    
    c_objects = objects.count()
    songi_page = c_objects
    test_num = c_objects + 1 # test raqami
    print('Songi page: ', c_objects)
    context = {
        'objects': objects,
        'model_id': pk,
        'universal_sources': universal_sources,
        'test_num': test_num,
        'hozirgi_page': hozirgi_page,
        'keyingi_page': keyingi_page,
        'songi_page': songi_page,
    }
    
    return render(request, 'dashboard_templates/models_temp/prezentatsiya.html', context)


# def test_view(request):
    
#     questions = models.QuestionModel
    
#     return render(request, 'dashboard_templates/models_temp/test.html')


# def document_view(request, pk, model_id):
#     objects = models.InsideModel.objects.filter(m_id = model_id)
#     documents = []

#     files = models.FileModel.objects.filter(inside_model=pk)
#     contents = models.InlineModelContent(inside_model=pk)
#     for file in files:
#         if file.file_type != 'Video':
#             documents.append(file)
          
        
#     print('Documents: ', documents)
    
#     context = {
#         'contents': contents,
#         'documents': documents,
#         'model_id': model_id,
#         'objects': objects,
#     }
    
#     return render(request, 'dashboard_templates/documents.html', context)


def download(request, pk):
    file1 = models.FileModel.objects.filter(id=pk)
    for i in file1:
        d= i.file
    response = FileResponse(d)
    # response['Content-Disposition'] = '; filename="shartnoma.pdf"'
    return response
