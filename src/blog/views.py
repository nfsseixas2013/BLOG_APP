from django.shortcuts import render

posts = [
    {
        'author': 'AB',
        'title': 'Blog post 1 blastoise',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'BA',
        'title': 'Blog post 2 blastoise',
        'date_posted': 'August 27, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
