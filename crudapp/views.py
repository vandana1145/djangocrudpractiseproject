from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

# This function will add and show the new items 
def add_show(req):
    if req.method == 'POST':
        fm = StudentRegistration(req.POST)
        if fm.is_valid():
            #fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else: 
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(req, 'crudapp/addandshow.html', {'form':fm, 'stud':stud})


# This function will update or edit
def update_data(req, id):
    if req.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(req.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(req, 'crudapp/updatestudent.html', {'form':fm})


# This function will delete the existing items
def delete_data(req, id):
    if req.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')