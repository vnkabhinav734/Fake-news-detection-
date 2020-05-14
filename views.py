from django.shortcuts import render
from django.http import HttpResponse, request
from .models import user
from .Search import Search
from .models import urls
from .models import tfidfsc
from .tfidf import TFIDF
from .models import lda
from .LDA import LDA
from django.db.models import Avg  

# Create your views here.
def home(request):
	return render(request, 'index.html')
def userlogin(request):
	return render(request, 'user.html')
def uregistraction(request):
	return render(request, 'ureg.html')
def uregaction(request):
	email=request.POST['mail']
	pwd=request.POST['pwd']
	zip=request.POST['zip']
	name=request.POST['name']
	age=request.POST['age']
	gen=request.POST['gen']

		
	d=user.objects.filter(email__exact=email).count()
	if d>0:
		return render(request, 'ureg.html',{'msg':"Email Already Registered"})
	else:
		d=user(name=name,email=email,pwd=pwd,zip=zip,gender=gen,age=age)
		d.save()
		return render(request, 'ureg.html',{'msg':"Register Success, You can Login.."})

	return render(request, 'ureg.html',{'msg':"Register Success, You can Login.."})


def ulogin(request):
	uid=request.POST['uid']
	pwd=request.POST['pwd']
	d=user.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
	if d>0:
		d=user.objects.filter(email__exact=uid)
		request.session['email']=uid
		return render(request, 'uhome.html',{'data': d[0]})

	else:
		return render(request, 'user.html',{'msg':"Login Fail"})

def uhome(request):
	return render(request, 'uhome.html')

def ulogout(request):
	try:
		del request.session['email']
	except:
		pass
	return render(request, 'user.html')


def uhome(request):
	return render(request, 'uhome.html')
def newssearch(request):
	if "email" in request.session:
		return render(request, 'search.html')

	else:
		return render(request, 'user.html')

def viewpprofile(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=user.objects.filter(email__exact=uid)
		return render(request, 'viewpprofile.html',{'data': d[0]})

	else:
		return render(request, 'user.html')

def searchnews(request):
	keys=request.POST['keys']
	request.session['keys']=keys
	data=Search.main(keys)
	urls.objects.all().delete()
	for d1 in data:
		d=urls(url=d1,score=0.0)
		d.save()
	return render(request, 'results.html',{'data':data})

def tfidfcalc(request):
	data=urls.objects.all()
	keys=request.session["keys"]
	print(data)
	tfidfsc.objects.all().delete()


	for d1 in data:
		print(d1.url)
		sc=TFIDF.process(d1.url,keys)
		print('----------------->',sc)
		sc=round(sc, 4)
		d=tfidfsc(url=d1.url,score=sc)
		d.save()
	data=tfidfsc.objects.all().order_by('-score')	
	return render(request, 'tfresults.html',{'data':data})
def test(request):
	d=lda.objects.all().aggregate(Avg('score'))
	print(d.get('score__avg'))
	return render(request, 'ldaresults.html')

def ldaaction(request):
	data=tfidfsc.objects.filter(score__gt=0)
	keys=request.session["keys"]
	lda.objects.all().delete()
	for d in data:
		print(d.url,d.score)

		sc=LDA.process(d.url,keys)
		if sc>0:
			sc=1
		else:
			sc=0
		d=lda(url=d.url,score=sc)
		d.save()
		d=lda.objects.all().aggregate(Avg('score'))
		print(d.get('score__avg'))
		res=d.get('score__avg')
		if res>0.5:
			res='Genuine News'
		else:
			res='Fake News'

	return render(request, 'ldaresults.html',{'data':res})



    
		
	