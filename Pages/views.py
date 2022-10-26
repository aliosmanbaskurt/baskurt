from django.shortcuts import render
from django.urls import reverse_lazy
from Courses.models import Course ,Category
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from Pages.models import Contact
from . forms import ContactForm
# Create your views here.


# def index (request):
#     courses = Course.objects.all().order_by('?')[:8]
#     cats= Category.objects.all()
#     context = {
#         'courses' : courses,
#         'cats': cats
#     }
#     return render(request ,'index.html' , context)


class IndexView(TemplateView):
    template_name = 'index.html'
  
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['courses']= Course.objects.filter(available=True).order_by('?')[:8]
        context['cats']=Category.objects.all()
       
        return context
    
  
class ContactView( SuccessMessageMixin,FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_url= reverse_lazy ('contact')
    success_message = "Mesajınız Alındı..."
    
    def form_valid (self, form):
        form.save()
        return super().form_valid(form)