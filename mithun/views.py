from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from mithun.models import *



# Create your views here.

def hello(request):
	number1="9845947613"
	return render(request,"home.html",{"number":number1,"sims":2})
def hello1(request):
        number1="9845947613"
        return JsonResponse({"number":number1,"sims":2})

def crudops(request):
   #Creating an entry
   
   dreamreal = Dreamreal(
      website = "www.polo.com", mail = "sorex@polo.com", 
      name = "sorex", phonenumber = "002376970"
   )
   
   dreamreal.save()
   return JsonResponse({"number":"number","sims":2})


def crudops1(request):
   #Creating an entry

   dream = Dream(
      web = "www.polo.com", ma = "sorex@polo.com",
      na = "sorex", ph = "002376970"
   )

   dream.save()
   return JsonResponse({"number":"number","sims":2})

def cr(request):
   #Creating an entry

   dream = Dream.objects.all()
   res='';
   for elt in dream:
      res += elt.na+"<br>"
   return HttpResponse(res)

def hi(request):
	year="278727822"
	sims="2"
	return redirect("/mithun/hi1/"+str(year)+"/"+str(sims))
	#return redirect ("/mithun/hi1/")

def hi1(request,year,month):
	return render(request,"home.html",{"number":year,"sims":month})



