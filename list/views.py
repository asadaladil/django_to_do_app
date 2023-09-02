from django.shortcuts import render,redirect,HttpResponseRedirect
from list.forms import ToDoForm,Signup_Form,TaskSearchForm,TaskOrdering,edit_profile_from
from list.models import ToDoModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.utils import timezone

# Create your views here.


def home2(request):
    return render(request,'home2.html')

def home(request):
    x=ToDoModel.objects.all()
    cnt=0
    for i in x:
        if i.is_completed is False:
            cnt+=1
    return render(request,'home.html',{'count':cnt})

def sign_up(request):
    fm=Signup_Form(request.POST)
    if request.method=="POST" and fm.is_valid():
        user=fm.save()
        login(request,user)
        return redirect('homepage')
    else:
        Signup_Form()
    return render(request,'sign_up.html',{'form':fm})

def log_in(request):  
    if not request.user.is_authenticated:
        fm=AuthenticationForm(request=request,data=request.POST)
        if request.method=="POST" and fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/home/',{"user":user})
            
        else:
            fm=AuthenticationForm()
        return render(request,"log_in.html",{"form":fm})
    else:
        return HttpResponseRedirect('/home/')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/home/')

def incomplete_tasks(request):
    tasks = ToDoModel.objects.all()
    print(tasks)
    return render(request,'incomplete.html',{'data':tasks})

def completed_tasks(request):
    tasks= ToDoModel.objects.filter(is_completed=True)
    return render(request,'complete.html',{'data':tasks})


def complete_task(request, id):
    tasks= ToDoModel.objects.get(pk=id)
    tasks.is_completed = True
    tasks.finished_time=timezone.now()
    tasks.save()
    return redirect('completedpage')

def add_tasks(request):
    if(request.method=='POST'):
        tasks = ToDoForm(request.POST)
        if tasks.is_valid():
            tasks.save()
            return redirect('incompletepage')
    else:
        tasks=ToDoForm()
    return render(request,'add.html',{'form':tasks})

def edit_task(request,id):
    tasks =ToDoModel.objects.get(pk=id)
    if(request.method=='POST'):
       form=ToDoForm(request.POST,instance=tasks)
       if form.is_valid():
            form.save()
            return redirect('incompletepage')
    else:
        form=ToDoForm(instance=tasks)
    return render(request,'add.html',{'form':form,'task':tasks})

def delete_task(request,id):
    tasks=ToDoModel.objects.get(pk=id).delete()
    return redirect('incompletepage')

def deleted_task(request,id):
    tasks=ToDoModel.objects.get(pk=id).delete()
    return redirect('completedpage')
    

def task_search(request):
    if request.method == 'GET':
        form= TaskSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            tasks = ToDoModel.objects.filter(title__icontains=search_query)
        else:
            tasks = ToDoModel.objects.all()
    else:
        form = TaskSearchForm()
        tasks = ToDoModel.objects.all()

    return render(request, 'task_search.html', {'form': form, 'tasks': tasks})

def task_ordering(request):
    if request.method == 'GET':
        form=TaskOrdering(request.GET)
        if form.is_valid():
            sort=form.cleaned_data['ordering']
            tasks = ToDoModel.objects.all()
            tasks = ToDoModel.objects.order_by(sort)
        else:
            tasks = ToDoModel.objects.all()
    else:
        form = TaskSearchForm()
        tasks = ToDoModel.objects.all()

    return render(request, 'task_order.html', {'form': form, 'tasks': tasks})



def edit_profile(request):
    if request.user.is_authenticated:
        fm=edit_profile_from(request.POST,instance=request.user)
        if request.method=="POST" and fm.is_valid():
            fm.save()
            return render(request,"home.html",{'count':cnt})
        else:
                
            fm=edit_profile_from(instance=request.user)
            return render(request,"profile.html",{'form':fm})
           
    else:
        return HttpResponseRedirect('/log_in/')