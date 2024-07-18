from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def index(request):
# گرفتن اطلاعات پست ها
    posts_list = Post.objects.all()

# ساخت paginator
    paginator = Paginator(posts_list , 3)   
    page = request.GET.get('page')
    paged_post_list = paginator.get_page(page)     

    context = {
        'posts' : paged_post_list
    }

    return render(request , 'posts/posts.html', context)

def post(request , post_id:int):
    return render(request , 'posts/post.html')

def search(request):
    return render(request , 'posts/search.html')
