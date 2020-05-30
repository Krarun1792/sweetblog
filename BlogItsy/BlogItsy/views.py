from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article,Author,Signup

def home(request):
    featured    = Article.objects.filter(featured=True)
    latest      = Article.objects.order_by('-timestamp')[0:3]
    articles    = Article.objects.all().order_by('date')
    author      = Author.objects.all()

    # article1     = Article.objects.get(slug=slug)

    context = {
        'featured': featured,
        'latest': latest,
        'blog_list': articles,
        'author': author
    }
    return render(request, 'index.html',context)

def about(request):
    author      = Author.objects.all()
    return render(request, 'about.html',{'author': author})

def blog(request):
    return render(request, 'blog.html')

def contact(request):

    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        new_signup = Signup()
        new_signup.name = name
        new_signup.email = email
        new_signup.message = message
        new_signup.save()

    return render(request, 'contact.html')
