from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,FormView
from .models import Trombinoscope,Member,Role,Category
import datetime
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
        members=Member.objects.filter(trombinoscope=trombinoscope)
        context=super().get_context_data(**kwargs)
        context["members"]=members
        return context




class PageView(TemplateView):
    template_name = 'page.html'
    def get_context_data(self, **kwargs):       
        context=super().get_context_data(**kwargs)
        year=kwargs["year"]
        trombinoscope=Trombinoscope.objects.get(year=year)
        context["type"]=Role.objects.get(pk=kwargs["role"])
        members=Member.objects.filter(role=context["type"],trombinoscope=trombinoscope)
 
        context["members"]=members
        context["trombinoscope"]=trombinoscope
        return context



class PageStaffView(TemplateView):
    template_name = 'staffpage.html'
    def get_context_data(self, **kwargs):
        year=kwargs["year"]
        trombinoscope=Trombinoscope.objects.get(year=year)
        members=Member.objects.filter(role__category=Category.objects.get_or_create(name="staff")[0],trombinoscope=trombinoscope)
        context=super().get_context_data(**kwargs)
        context["members"]=members
        context["trombinoscope"]=trombinoscope

        return context
        

