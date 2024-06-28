from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DeleteView,DetailView,FormView,ListView,CreateView,UpdateView
from django.views import View
from django.urls import reverse_lazy
from clsroom_app.forms import TeacherRegistration,StudentRegistration,TeacherLoginForm,StudentLoginForm,EditDetailsForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from clsroom_app.models import Classes,Subject
from django.shortcuts import render
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import pkg_resources
import razorpay





# Create your views here.


# class Index(TemplateView):
#     template_name='index.html'
#     def get_context_data(self, **kwargs):
#          context=super().get_context_data(**kwargs)
#          products=Products.objects.all()
#          context['products']=products
#          return context

class Index(View):
    def get(self,request):
        return render(request,'index.html')
        
    
class TeacherRegisterView(CreateView):
    template_name='teacher_register.html'
    form_class=TeacherRegistration
    success_url=reverse_lazy('home_view')

    def form_valid(self, form):
        User.objects.create_user(**form.cleaned_data)
        return redirect('home_view')
    

class StudentRegisterView(CreateView):
    template_name='student_register.html'
    form_class=StudentRegistration
    success_url=reverse_lazy('stud_view')

    def form_valid(self, form) :
        User.objects.create_user(**form.cleaned_data)
        return redirect('stud_view')


class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login_page.html')
    

class TeacherLoginView(View):
    def get(self,request,*args,**kwargs):
        form=TeacherLoginForm
        return render(request,'t_login.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        pswd=request.POST.get('password')
        u_name=request.POST.get('username')
        user=authenticate(request,username=u_name,password=pswd)
        if user:
            login(request,user)
            messages.success(request,'login_success')
            return redirect('home_view')
        else:
            messages.error(request,'invalid_credentials')
            return render(request,'t_login.html')

class StudentLoginView(View):
    def get(self,request,*args,**kwargs):
        form=StudentLoginForm
        return render(request,'s_login.html',{'form':form})
    def post(self,request,*args,**kwars):
        pswd=request.POST.get('password')
        u_name=request.POST.get('username')
        user=authenticate(request,username=u_name,password=pswd)
        if user:
            login(request,user)
            messages.success(request,'login_success')
            return redirect('stud_view')
        else:
            messages.error(request,'invalid_credentials')
            return render(request,'s_login.html')


class Logout(View):
    def get(self,request,*args,**kwargs) :
        logout(request)
        messages.warning(request,'successfully logged out')
        return render(request,'index.html')
    
class TeacherMoreDetails(ListView):
    model=Classes
    template_name='projects.html'
    context_object_name='subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.all()
        return context



class TeahcerUploads(ListView):
    model=Classes
    template_name='resume.html'
    # pk_url_kwarg='id'
    context_object_name='subject'


class StudentClass(ListView):
    model=Classes
    template_name='stud_class.html'
    context_object_name='subject'

class Home(View):
    def get(self,request):
        return render(request,'index1.html')
    
# class ClassView(View):
#     def get(self,request):
#         return render(request,'resume.html')
    
class DetailedView(DetailView):
    model=Classes
    template_name='details.html'
    pk_url_kwarg='id'
    context_object_name='details'

    def detailed_view(request, id):
        # print(id)
    # Retrieve the Classes object with the specified ID
        classes= Classes.objects.get(id=id)
        return render(request, 'details.html', {'classes_instance': classes})
    
class StudView(View):
    def get(self,request):
        return render(request,'student.html')
    
class ClassDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        delete=Classes.objects.get(id=id)
        delete.delete()
        messages.warning(request,'video is deleted')
        return render(request,'details.html')
    
class EditDetails(UpdateView):
    form_class=EditDetailsForm
    model=Classes
    template_name='edit.html'
    success_url=reverse_lazy('detailed_view')
    pk_url_kwarg='id'
    
    
# class StudClassView(View):
#     def get(self,request):
#         return render(request,'stud_class.html')
    

class UserData(View):
    def get(self,request):
        return render(request,'user_data.html')
    
class TryPremium(View):
    def get(self,request,*args,**kwargs):
        return render(request,'try_premium.html')
    

    




