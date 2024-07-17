from django.shortcuts import render
from .models import Post

def index(request):
# گرفتن اطلاعات پست ها
    posts_list = Post.objects.all()

    context = {
        'posts' : posts_list
    }

    return render(request , 'posts/posts.html', context)

def post(request):
    return render(request , 'posts/post.html')

def search(request):
    return render(request , 'posts/search.html')
