#python first
#django second
#our apps
from django.conf import settings
from django.contrib import messages

from django.core.mail import send_mail
from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect

#from django.views.decorators.vary import vary_on_headers

from .forms import UserForm
#@vary_on_headers('User-Agent')
def home(request): 
    return render_to_response("signup.html",locals(),context_instance=RequestContext(request))

def thankyou(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        subject="thank you for joining"
        message="we are very welcome to join us./n We will be in touch"
        from_email=settings.EMAIL_HOST_USER
        to_list=[save_it.email,settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=True) 
        
        messages.success(request,'irtibatta olalim')
        return HttpResponseRedirect('/thank-you/')
    return render_to_response("thankyou.html",locals(),context_instance=RequestContext(request))

def aboutus(request):   
    return render_to_response("aboutus.html",locals(),context_instance=RequestContext(request))


def signin(request):   
    return render_to_response("signin.html",locals(),context_instance=RequestContext(request))


