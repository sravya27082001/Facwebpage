
#from django.contrib.auth import authenticate,login
#from django.views.generic import View
from fac.forms import RegistrationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from . import models
from .models import Qualification, Faculty
from django.conf import settings
import requests

import html2text

def index(request):
    return render(request,"fac/home.html")

def bsbe(request):
    all=User.objects.all()

    return render(request,'fac/bsbe.html',{'all':all})
def ce(request):
    all=User.objects.all()

    return render(request,'fac/chem.html',{'all':all})
def ch(request):
    all=User.objects.all()

    return render(request,'fac/ch.html',{'all':all})
def civ(request):
    all=User.objects.all()
    return render(request,'fac/civ.html',{'all':all})
def comp(request):
    all=User.objects.all()
    return render(request,'fac/comp.html',{'all':all})
def math(request):
    all=User.objects.all()
    return render(request,'fac/maths.html',{'all':all})
def ee(request):
    all=User.objects.all()
    return render(request,'fac/ee.html',{'all':all})
def ph(request):
    all=User.objects.all()
    return render(request,'fac/phy.html',{'all':all})
def mech(request):
    all=User.objects.all()
    return render(request,'fac/me.html',{'all':all})
def des(request):
    all=User.objects.all()
    return render(request,'fac/design.html',{'all':all})

def home(request,username):
    user=User.objects.get(username=username)
    return render(request,"fac/pr.html",{'user':user })


def edit_user_page(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    return render(request,"fac/edit_profile.html")


def edit_user(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    else:
        user=request.user
        department = request.POST['department']
        Position = request.POST['Position']
        Webmail = request.POST['Webmail']
        phone=request.POST['phone']
        fax=request.POST['fax']
        Room_No=request.POST['Room_No']
        About=request.POST['About']
        image=request.FILES.get('image','1.jpg')
        obj = models.Faculty.objects.filter(user=request.user)
        if not obj.exists():
            faculty=models.Faculty(department=department,Position=Position,Webmail=Webmail,phone=phone,fax=fax,Room_No=Room_No,About=About,image=image)
            faculty.user=request.user
            faculty.save()
        else:
            models.Faculty.objects.filter(user=user).update(department=department,Position=Position,Webmail=Webmail,phone=phone,fax=fax,Room_No=Room_No,About=About,image=image)
            obj=models.Faculty.objects.get(user=user)
            obj.image=image
            obj.save()

        return HttpResponseRedirect('/fac/profile')

def edit_user1_page(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    return render(request,"fac/edit_profile1.html")


def edit_user1(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    else:
        Mtech = request.POST['Mtech']
        Btech=request.POST['Btech']
        PHD=request.POST['PHD']
        obj = models.Qualification(Mtech=Mtech,Btech=Btech,PHD=PHD)

        obj.user=request.user
        obj.save()

        return HttpResponseRedirect('/fac/profile')


def edit_user2_page(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    return render(request,"fac/edit_profile2.html")


def edit_user2(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    else:
        title = request.POST['title']
        Sponsorer = request.POST['Sponsorer']
        role = request.POST['role']
        duration = request.POST['duration']

        obj = models.Projects(title=title,Sponsorer=Sponsorer,role=role,duration=duration)
        obj.user=request.user
        obj.save()
        return HttpResponseRedirect('/fac/profile')


def edit_user3_page(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    return render(request,"fac/edit_profile3.html")


def edit_user3(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    else:
        Course =request.POST['Course']
        time = request.POST['time']
        Semester=request.POST['Semester']

        obj = models.Teaching(Course=Course,time=time,Semester=Semester)
        obj.user=request.user
        obj.save()
        return HttpResponseRedirect('/fac/profile')

def edit_user4_page(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    return render(request,"fac/edit_profile4.html")


def edit_user4(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    else:
        Institute =request.POST['Institute']
        Position = request.POST['Position']
        year=request.POST['year']

        obj = models.Experience(Institute=Institute,Position=Position,year=year)
        obj.user=request.user
        obj.save()
        return HttpResponseRedirect('/fac/profile')



def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'fac/3.html')
        else:
            return render(request,'fac/2.html')
	    #else:
		 #   return redirect('/fac/register')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request,"fac/reg_form.html", args)

def view_profile(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    args={'user':request.user}
    return render(request,'fac/main.html',args)


def edit_user5_page(request,username):
    user = User.objects.get(username=username)
    args={'user':user}

    return render(request,"fac/edit_profile5.html",args)


def edit_user5(request,username):
    user = User.objects.get(username=username)
    name=request.POST['name']
    que = request.POST['que']

    obj = models.Question(name=name,que=que)
    obj.user = user
    obj.save()
    return HttpResponseRedirect('/fac/profile')
def edit_user6_page(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    return render(request,"fac/edit_profile6.html")


def edit_user6(request):
    if not request.user.is_authenticated():
        return redirect('/fac/login')
    else:
        ans =request.POST['ans']


        obj = models.Question(ans=ans)
        obj.user=request.user
        obj.save()
        return HttpResponseRedirect('/fac/profile')

def change_password(request):
    if request.method=="POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/fac/logout')
        else:
            return HttpResponse("Not valid!!!GO BACK")
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'fac/change_password.html',args)

def tr(request,username):
    import requests

    import html2text
    user = User.objects.get(username=username)
    quote_page = 'https://www.iitg.ernet.in/cseweb/automation/people?statusCode=3c6234c6f6ff2880ec3c0c979ba87ba4'
    name = user.first_name +" "+user.last_name
    page = requests.get(quote_page)

    plain_text = page.text

    det = plain_text.split("<strong><u>" + name + "</u></strong></span>")

    mat = det[1].split('</font></td></tr>')

    jake = html2text.html2text(mat[0])
    kake = jake.replace('**', ', ').replace('_', '')
    args={'kake':kake}
    return render(request,'fac/tr.html',args)


    # for link in soup.findAll('p', {'class': 'text-justify'}):

    #   title = link.text
    #  print(title)

# Create your views here.
#class UserFormView(View):
 #   form_class=UserForm
  #  template_name='fac/reg.html'

#    def get(self,request):
 #       form=self.form_class(None)
  #      return render(request,self.template_name,{'form':form})

#    def post(self,request):
 #       form=self.form_class(request.POST)
  #      if form.is_valid():
   #         user=form.save(commit=False)
#
 #           username=form.cleaned_data['username']
        #    password=form.cleaned_data['password']
         #   user.set_password(password)
          #  user.save()
           # user=authenticate(username=username,password=password)
            #if user is not None:
             #   if user.is_active:
              #      login(request,user)
               #     return redirect('fac:index')
            #return render(request,self.template_name,{'form':form})

