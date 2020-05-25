from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Blog, User, Comment, Reply
from .forms import UserForm, RegisterForm, BlogForm

import hashlib

def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode()) # update方法只接收bytes类型
    return h.hexdigest()

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request,'user.html', locals())

def blogDetail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog.html', locals())

def login(request):
    if request.session.get('is_login',None):
        return redirect('/blog/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            username = username.strip()
            try:
                user = User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/blog/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login.html', locals())     
    
    login_form = UserForm()
    return render(request,'login.html', locals())

def register(request):
    if request.session.get('is_login',None):
        return redirect('/blog/')

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                
                new_user = User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.save()
                return redirect('/blog/login/')
    register_form = RegisterForm()
    return render(request,'register.html', locals())

def comment(request, blog_id):
    pass
    return render(request,'blog.html')

def reply(request, blog_id):
    pass
    return render(request,'blog.html')

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/blog/")
    request.session.flush()
    return redirect("/blog/")

def editBlog(request):
    if not request.session.get('is_login',None):
        return redirect('/blog/login/')

    if request.method == "POST":
        blog_form = BlogForm(request.POST)
        message = "请检查填写的内容！"
        if blog_form.is_valid():
            title = blog_form.cleaned_data['title']
            content = blog_form.cleaned_data['content']
            username = request.session.get('user_name')

            new_blog = Blog.objects.create()
            new_blog.title = title
            new_blog.body = content
            new_blog.author = username
            new_blog.save()
            print("博客", title, "已发布")
            return redirect('/blog/userIndex/', locals())
    blog_form = BlogForm()
    return render(request,'editBlog.html', locals())


def userIndex(request):
    if request.session.get('is_login',None):
        username = request.session.get('user_name')
        blogs = Blog.objects.filter(author=username)
        return render(request,'user.html', locals())
    
    return redirect('/blog/login/')
