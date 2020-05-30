from django.shortcuts import render
from .models import Article,Author
from django.http import HttpResponse

# Create your views here.
def blog_list(request):
    blogs = Article.objects.all().order_by('date')
    author      = Author.objects.all()

    
    context = {
        'articles':blogs,
        'author': author
    }
    return render(request,'articles/blog.html',context)


def blog_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request,'articles/single.html',{'article': article })
