from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Notice,Free,Tip
from .forms import NoticeForm,FreeForm,TipForm
# Create your views here.
def notice_home(request):
    blogs = Notice.objects.all()
    blog_list = Notice.objects.all()

    paginator = Paginator(blog_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/notices.html', {'blogs': blogs, 'posts': posts})
    # blog_list = Blog.objects.all()
    # page = request.GET.get('page', 1)

    # paginator = Paginator(blog_list, 10)
    # try:
    #     blogs = Paginator.page(page)
    # except PageNotAnInteger:
    #     blogs = paginator.page(1)
    # except EmptyPage:
    #     blogs = paginator.page(paginator,num_pages)

    # return render(request, 'blog/notices.html', {'blogs': blogs})

def notice_detail(request, pk):
    blog = get_object_or_404(Notice, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})

def notice_create(request):
    form = NoticeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog_form.html', {'form': form})

def notice_update(request, pk):
    blog = get_object_or_404(Notice, pk=pk)
    form = NoticeForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog_form.html', {'form': form})

def noice_delete(request, pk):
    return render(request, 'blog_delete.html')

def free_home(request):
    blogs = Free.objects.all()
    blog_list = Free.objects.all()

    paginator = Paginator(blog_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/free.html', {'blogs': blogs, 'posts': posts})
    # blog_list = Blog.objects.all()
    # page = request.GET.get('page', 1)

    # paginator = Paginator(blog_list, 10)
    # try:
    #     blogs = Paginator.page(page)
    # except PageNotAnInteger:
    #     blogs = paginator.page(1)
    # except EmptyPage:
    #     blogs = paginator.page(paginator,num_pages)

    # return render(request, 'blog/notices.html', {'blogs': blogs})

def free_detail(request, pk):
    blog = get_object_or_404(Free, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})

def free_create(request):
    form = FreeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog_form.html', {'form': form})

def free_update(request, pk):
    blog = get_object_or_404(Free, pk=pk)
    form = FreeForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog_form.html', {'form': form})

def free_delete(request, pk):
    return render(request, 'blog_delete.html')

def tip_home(request):
    blogs = Tip.objects.all()
    blog_list = Tip.objects.all()

    paginator = Paginator(blog_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/tip.html', {'blogs': blogs, 'posts': posts})
    # blog_list = Blog.objects.all()
    # page = request.GET.get('page', 1)

    # paginator = Paginator(blog_list, 10)
    # try:
    #     blogs = Paginator.page(page)
    # except PageNotAnInteger:
    #     blogs = paginator.page(1)
    # except EmptyPage:
    #     blogs = paginator.page(paginator,num_pages)

    # return render(request, 'blog/notices.html', {'blogs': blogs})

def tip_detail(request, pk):
    blog = get_object_or_404(Tip, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})

def tip_create(request):
    form = TipForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog_form.html', {'form': form})

def tip_update(request, pk):
    blog = get_object_or_404(Tip, pk=pk)
    form = TipForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'blog_form.html', {'form': form})

def tip_delete(request, pk):
    return render(request, 'blog_delete.html')