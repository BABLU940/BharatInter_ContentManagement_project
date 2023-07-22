from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.
def add_view(request):
    if request.method=="POST" or request.method=="FILES":
        Name = request.POST.get('Name','NA')
        Image = request.FILES.get('Image',"NA")
        Text = request.POST.get('Text','NA')
        Video = request.POST.get('Video','NA')
        emp = Blog.objects.create(Name=Name,Image=Image,Text=Text,Video=Video)
        emp.save()
        messages.success(request, "Blog Added Successfully...")
    
    resp = render(request,'CMT/add.html')
    return resp

def show_view(request):
    user_list=Blog.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 4)
    try:
        emp = paginator.page(page)
    except PageNotAnInteger:
        emp = paginator.page(1)
    except EmptyPage:
        emp = paginator.page(paginator.num_pages)
    d={'emp':emp}
    resp = render(request,'CMT/showall.html',context=d)
    return resp


def view_blog(request,eid):
    emp=Blog.objects.get(id=eid)
    d={'emp':emp}
    resp = render(request,'CMT/view.html',context=d)
    return resp


def update_view(request,eid):
    data = Blog.objects.get(id=eid)
    if request.method=="POST":
        data.Name = request.POST.get('Name')
        data.Image = request.FILES.get('Image',data.Image)
        data.Text = request.POST.get('Text')
        data.Video = request.POST.get('Video')
        data.save()
        return redirect('/')
    d={'data':data}
    resp = render(request,'CMT/update.html',context=d)
    return resp

def delete_view(request,eid):
    data= Blog.objects.get(id=eid)
    data.delete()   
    return redirect('/')    