from django.shortcuts import render, get_object_or_404, redirect #get_object_or_404 추가, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost



def blog(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog.html', {'blogs' : blogs, 'posts' : posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'  + str(blog.id))

def blogpost(request):
    if request.method == "POST":
        form = BlogPost(request.POST)
        if form.is_valid():                         # is_valid 함수로 입력 값이 잘 들어 왔으면 true 아니면 fasle
            post = form.save(commit = False)        # model에서는 3개의 값이 필요함 아직 저장하면 안됨 모델 객체를 반환받되 저장x save함수에 commit=false로 해결
            post.pub_date = timezone.now()          # pub_date 추가
            post.save()
            return redirect('home')

    else:
        form = BlogPost()
        return render(request, 'new2.html', {'form' : form})

def delete(request, blog_id):
    blog_detail = get_object_or_404(Blog, id = blog_id)
    blog_detail.delete()
    return redirect('/')

def edit(request, blog_id):
    blog = get_object_or_404(Blog, id = blog_id)

    # 글을 수정사항을 입력하고 제출을 눌렀을 때
    if request.method == "POST":
        form = BlogPost(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            blog.title = form.cleaned_data['title']
            blog.body = form.cleaned_data['body']
            blog.save()
            return redirect('/blog/' + str(blog.pk))

    # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
    else:
        form = BlogPost(instance = blog)
        context = {
            'form' : form,
            'writing' : True,
            'now' : 'edit',
        }
        return render(request, 'edit_post.html', context)