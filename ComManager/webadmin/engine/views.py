# Create your views here.
#!/usr/bin/python
#-*-coding:utf-8-*--
#from django.template import RequestContext
from django.shortcuts import render_to_response
#set the login_required every url must login the index.html
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
	print ruquest
	username = request.user.username
	#print request
	print request.user.username
	return render_to_response('index.html',{
			"title":'main',
			'username':username
		}
		#, context_instance = RequestContext(request)
	)
