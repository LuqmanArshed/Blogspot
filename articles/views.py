from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users,admin_only
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def logoutuser(request):
	logout(request)
	return redirect('home')






def login_page(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('user_home')
		else:
			messages.info(request,'User or Password is Incorrect')

	context={}
	return render(request,'pages/login.html',context)





def home(request):
    all_blogs = Blog.objects.all()
    context={'all_blogs':all_blogs}
    return render(request,'pages/home.html',context)




def blog_view(request,id):
    blog = Blog.objects.get(id=id)
    check = False
    if blog.language == 'English':
        check = True

    context={'blog':blog,'check':check}
    return render(request,'pages/article.html',context)



@login_required(login_url=login_page)
@allowed_users(allowed_roles=['admin'])
def user_home(request):
    all_blogs = Blog.objects.all()
    context={'all_blogs':all_blogs}
    return render(request,'pages/user_panel.html',context)

@login_required(login_url=login_page)
@allowed_users(allowed_roles=['admin'])
def new_blog(request):
    form = new_blog_form(request.POST,request.FILES)
    files = request.FILES.getlist('thumbnail')
    files1 = request.FILES.getlist('title_image')
    files2 = request.FILES.getlist('center_image')
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save()
            for image in files:
                obj.thumbnail = image
                obj.save()
            for imag in files1:
                obj.title_image = imag
                obj.save()
            for img in files2:
                obj.center_image = img
                obj.save()        
            return redirect('user_home')
	
    context = {'form':form}
    return render(request,'pages/new_blog.html',context)


@login_required(login_url=login_page)
@allowed_users(allowed_roles=['admin'])
def edit_blog(request,id):
    blog_to_edit = Blog.objects.get(id=id)
    form = new_blog_form(instance=blog_to_edit)
    files = request.FILES.getlist('thumbnail')
    if request.method == 'POST':
        form = new_blog_form(request.POST,instance=blog_to_edit)
        if form.is_valid():
            obj = form.save()
            for image in files:
                obj.thumbnail = image
                obj.save()
            return redirect('user_home')
	
    context = {'form':form}
    return render(request,'pages/edit_blog.html',context)