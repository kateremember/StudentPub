#!/usr/bin/python
#
from django.shortcuts import render_to_response

def userlogin(request):
	#print 'aaa'
	if request.method == 'POST':
		print 'login success'
		#form = LoginForm()
	else:
		print 'bb'
	
	return render_to_response('account/login',{ 'captcha': None})
