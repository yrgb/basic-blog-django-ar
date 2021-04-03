from django.shortcuts import render

# Create your views here.

def home(request):


    context = {
        'title': 'الصفحة الرئيسية',
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'من أنا'})
