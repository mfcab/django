from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Post,Category,Tag
from comments.forms import CommentForm


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)

    except PageNotAnInteger:
        contacts = paginator.page(1)

    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', context={'contacts': contacts})



def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)

    except PageNotAnInteger:
        contacts = paginator.page(1)

    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', context={'contacts': contacts})


def tags(request, pk):
    cate = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=cate).order_by('-created_time')
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)

    except PageNotAnInteger:
        contacts = paginator.page(1)

    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', context={'contacts': contacts})
