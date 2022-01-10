from django.http import response
from django.shortcuts import render
from django.http import FileResponse, HttpResponse
# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Test, classinline, natijalar, TestModul


# def register_login_view(request):
#     context = {

#     }
#     return render(request, 'auth_template/auth_index.html', context)

# def sertificates(request)

def home(request):
    
    return render(request, 'index.html')

def auoth_index(request):
    context = {

    }
    return render(request, 'dashboard_templates/index.html', context)


def dashboard_about(request):
    context = {

    }
    return render(request, 'dashboard_templates/about.html', context)


def dashboar_article(request):
    return render(request, 'dashboard_templates/article.html')


def dashboard_sertificate(request):
    return render(request, 'dashboard_templates/certificates.html')


def dashboard_pasword_change(request):
    return render(request, 'dashboard_templates/dashboard-password-change.html')


def dashboard(request):
    return render(request, 'dashboard_templates/dashboard.html')


def documents(request):
    return render(request, 'dashboard_templates/documents.html')


def help_handbook(request):
    return render(request, 'dashboard_templates/help-handbook.html')


# def info(request):
#     user = request.user.id
#     kurs = Moduls.objects.filter(users=user)
#     context = {
#         'kurs': kurs
#     }

#     return render(request, 'dashboard_templates/info.html', context)


# def info_prezentatsiya(request, id, id1):
#     lesson = lessons.objects.filter(moduls_key=id, num=id1)
#     lesson1 = lessons.objects.filter(moduls_key=id)
#     # tepada books modelmini as qilib book ga tenglab oldim chuniki def funksiyalarimda 
#     books1 = book.objects.filter(modul_key=id)
#     # if books1:
#     #     print('dsa')
#     # for data in lesson1:
#     #     d = data.prizentatsiya
#     # print(d)
#     modul_id = id

#     context = {
#         'lesson': lesson,
#         'lessons': lesson1,
#         'm_id': modul_id,
#         'books1': books1,

#     }
#     return render(request, 'dashboard_templates/prezentatsiya.html', context)


def videos(request):
    return render(request, 'dashboard_templates/videos.html')


def poisk(request):
    return render(request, 'dashboard_templates/poisk.html')


def stoer(request):
   

    return render(request, 'dashboard_templates/store.html')


# def xabar(request):
#     return render(request, )

def books(request):
    return render(request, 'dashboard_templates/store-inner.html')


# def open(request, id):
#     booka = book.objects.filter(id=id)
#     for i in booka:
#         d = i.book
#     response = FileResponse(d)
#     # response['Content-Disposition'] = '; filename="shartnoma.pdf"'
#     return response

    # return response


from .models import Test
from .form import NatijaForm


# def home(request)

def test(request, pk):
    global h, g
    test = TestModul.objects.filter(moduls_test_key=pk)
    for i in test:
       id = i.id
    
    test1 = Test.objects.filter(test_key=id).order_by('?')
    
    test3 = TestModul.objects.get(id=1)

    for i in test:
        soat = int(i.test_time) * 3600
        min = int(i.test_time) * 60
    answers = []
    for i in test1:
        a = i.id
        answer = request.GET.get(f'test-{a}')
        answers.append(answer)

    option = []
    for i in test1:
        option.append(i.answer)
    g = 0
    h = 0
    print(option)
    print(answers)
    d = 0

    for a in option:
        if option[g] == answers[g]:
            h = h + 1
            d = 1
        g = g + 1
    print(h)
    sa = pk
    if request.GET:
        if answers != []:
            da = natijalar()
            da.user = request.user
            da.test_t = h
            da.test_alls = g
            da.Test1 = test.first()
            da.save()

            return redirect('result', pk=sa)
        else:
            pass

    context = {
        "test1": test1,
        "test": test,
        "soat": soat,
        'min': min,
        'da': d,
        'id': id,

    }
    return render(request, 'dashboard_templates/test.html', context)


def result(request,pk):
    # data = natijalar.objects.filter(test=id)
    # test = TestModul.objects.filter(id=1)
    result = []
    # for i in data:m
    #     result.append(i.test_t)
    # for i in data:
    #     i.test_t
    from pages.models import natijalar
    data = natijalar.objects.filter(Test1=1)
    results = []
    for i in data:
        results.append(i.test_t)
    d = max(results)
    data2 = natijalar.objects.filter(Test1=pk).last()
        
    # for i in data2:
    d = data2.test_t
    d2 = data2.test_alls
    porsent = int(float(d) / float(d2) * 100)
    d3 = d2 - d

    context = {
        'data': data,
        'd': d,
        'd2': d2,
        'd3': d3,
        'porsent': porsent
    }
    return render(request, 'dashboard_templates/score.html', context)
# def ati