from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader
from django.views.decorators.clickjacking import xframe_options_exempt





def index(request):
	template = loader.get_template('index.html')
	return HttpResponse(template.render({'sd':"context",},request))


def Overview(request):
	template=loader.get_template('Overview/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
def News(request):
	template=loader.get_template('News/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
def Trends(request):
	template=loader.get_template('Trends/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
def Projects(request):
	template=loader.get_template('Projects/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
def graduate(request):
	template=loader.get_template('graduate/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
	
@xframe_options_exempt
def Friend(request):
	template=loader.get_template('Friend/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
def Services(request):
	template=loader.get_template('Services/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
def statistics(request):
	template=loader.get_template('statistics/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
def SourceDown(request):
	template=loader.get_template('SourceDown/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
def Experience(request):
	template=loader.get_template('Experience/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
def ModelApp(request):
	template=loader.get_template('ModelApp/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))
def faq(request):
	template=loader.get_template('faq/default.html')
	return HttpResponse(template.render({'22':'asdfa',},request))