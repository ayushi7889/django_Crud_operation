from django.shortcuts import render,redirect,HttpResponse
from .forms import EmployeeForm
from .models import Crud


# Create your views here.

def Crud_list(request):
    context = {'Crud_list':Crud.objects.all()}
    return render(request,"Crud_app/Crud_list.html",context)

def Crud_form(request,id=0):
    if request.method == 'GET':
        if id==0:
            form=EmployeeForm()
        else:
            employee=Crud.objects.get(pk=id)
            form=EmployeeForm(instance=employee)
        return render(request,"Crud_app/Crud_form.html",{'form':form})
    else:
        if id == 0:
            form=EmployeeForm(request.POST)
        else:
            employee=Crud.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)

        if form.is_valid():
            form.save()
        return redirect('/crud/list')


def Crud_delete(request,id):
    employee=Crud.objects.get(pk=id)
    employee.delete()
    return redirect('/crud/list')

def search(request):
    search=request.GET['search']
    
    context = {'Crud_list':Crud.objects.filter(fullname__icontains=search)}

    #List = Crud.objects.all()
    #allList = Crud.objects.filter(fullname__icontains=search)
    return render(request,'Crud_app/search.html',context)
    #return HttpResponse('this is search page')
