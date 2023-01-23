from .models import Category,Trombinoscope

def trombi_context(request):
   return {'ingenieur' : Category.objects.get_or_create(name="UISJ - Ingenieur")[0],
           'management':Category.objects.get_or_create(name="UISJ - management")[0],
           'trombinoscopes':Trombinoscope.objects.all()}