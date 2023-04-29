from django.shortcuts import render,HttpResponse,redirect
from . models import Department , Role ,Employee
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')
def view(request):
    emps= Employee.objects.all()
    context={
        "emps":emps
    }
    return render(request, 'view.html',context)

def add(request):
    if request.method=='POST':
        fname = request.POST['f-name']
        lname = request.POST['l-name']
        dpt = request.POST['depts']
       
        role = request.POST['role']
        #location = request.POST['location']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone= int(request.POST['phone'])
       # hrdate = request.POST['hire-date']
        new_emp=Employee(first_name=fname,last_name=lname,phone=phone,salary=salary, dept_id=dpt,role_id=role,bonus=bonus,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Succesfully")
        
    else:
         return render(request, 'add.html')

def remove(request,emp_id=0):
    if emp_id:
        try:
            emp_remove=Employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse("Succesfully Removed Employee")
        except:
            return HttpResponse("Please Enter valid Id")
    emps=Employee.objects.all()
    context={
        "emps":emps
       }

    return render(request, 'remove.html' ,context)

def filter(request):
    if request.method=='POST':
        name=request.POST['ename']
        dept=request.POST['depts']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        context={
            "emps":emps
            
        }
        return render(request, 'view.html',context)
    else:
        return render(request, 'filter.html')

def index(request):
    return render(request, 'index.html')