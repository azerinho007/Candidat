from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login,logout as dj_logout
from .models import Profile
from django.contrib.auth.decorators import login_required
import smtplib
import ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from django.views.generic.edit import UpdateView


# Create your views here.
def signin(request,msg):
    print(msg)
    if(request.method == 'POST'):
        user = request.POST['login']
        pwd = request.POST['pwd']
        try:
            u = User.objects.get(username=user,password=pwd)
            login(request,u)
            return redirect('login:home')
        except Exception as x:
            return render(request, 'signin.html', {"msg": 1})
    else:
        return render(request, 'signin.html', {"msg": 0})

def signup(request):
    import string
    import random
    if(request.method == 'POST'):
        request.session['fname'] = request.POST['fname']
        request.session['lname'] = request.POST['lname']
        request.session['mail'] = request.POST['mail']
        request.session['user'] = request.POST['username']
        request.session['pwd'] = request.POST['pwd']

        code = [random.choice(string.ascii_letters) for i in range(50)]
        code = "".join(code)
        request.session['code'] = code

        sendmail(request.session['mail'],request.session['user'],code)
        return redirect('login:verify',0)
    else:
        return render(request,'signup.html')

def home(request):
    return render(request,'blank.html')

def verify(request,msg):
    if(request.method == "POST"):
        code = request.POST['code']
        if (code == request.session['code']):
            u = User()
            u.username = request.session['user']
            u.email = request.session['mail']
            u.first_name = request.session['fname']
            u.last_name = request.session['lname']
            u.password = request.session['pwd']
            u.save()
            p = Profile(code=code, user=u)
            p.save()
            request.session.clear()
            return redirect('login:sign',0)
        else:
            return render(request, 'verify.html',{"msg":1})
    else:
        return render(request,'verify.html', {"msg":0})


def sendmail(mail,user,code):
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("azerch.1996@gmail.com", '01246790aA')

        msg = MIMEMultipart()
        msg['from'] = 'Django Candidat'
        msg['to'] = mail
        msg['Subject'] = "Last step to register"
        message = '<h1> Welcome {} </h1> <br> <br> <img src="https://www.lhotellerie-restauration.fr/journal/equipement-materiel/2018-06/img/tablhotel.jpg" alt="check connection" <br><br><br><br><br><br> Your verifying code is: <underline> {} </underline>'.format(user,code)
        msg.attach(MIMEText(message, 'html'))
        server.sendmail('azerch.1996@gmail.com"', mail, msg.as_string())

@login_required
def logout(request):
    dj_logout(request)
    return render(request,'blank.html')

class UserUpdateView(UpdateView):
    model = User
    fields = ['username','first_name','last_name','email','password']
    template_name = 'user_update_form.html'
    success_url = "/"