from django.shortcuts import render

# Create your views here.

def home(request):
    
    
    context = {
        
    }
    return render(request, 'index.html', context)

def register_login_view(request):
    
    context = {
        
    }
    return render(request, 'auth_template/auth_index.html', context)


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





def documents(request):
    
    return render(request, 'dashboard_templates/documents.html')


def help_handbook(request):
    
    return render(request, 'dashboard_templates/help-handbook.html')


