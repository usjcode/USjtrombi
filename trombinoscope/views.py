from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .models import Trombinoscope,Member,Department,Category
# Create your views here.



class HomeView(View):
    def get(self,request,*args,**kwargs):
        lastyear=Trombinoscope.objects.last().year
        return redirect("trombinoscope",year=lastyear)

class TrombiView(TemplateView):
    template_name = 'trombinoscope.html'
    def get_context_data(self, **kwargs):
        year=kwargs["year"]
        trombinoscope=Trombinoscope.objects.get(year=year)
        trombinoscopes=Trombinoscope.objects.all()
        members=Member.objects.filter(trombinoscope=trombinoscope)
        context=super().get_context_data(**kwargs)
        context["trombinoscopes"]=trombinoscopes
        context["members"]=members
        context["category"]=Category.objects.all()
 
        return context

        