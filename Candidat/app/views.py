from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import  User
from .models import  Taburl

# Create your views here.
class UserUpdateView(UpdateView):
    model = User
    fields = ['username','first_name','last_name','email','password']
    template_name = 'user_update_form.html'
    success_url = "/"


def api(request,pk):
    import string
    import random
    if(request.method == "POST"):
        d = 1

        try:
            base = Taburl.objects.get(basic=request.POST['url'])
            #base.nb = base.nb + 1
            url = base.miniurl
        except Exception as x:
            while(d):
                url = [random.choice(string.ascii_letters + string.digits + '?!*-.,=@') for k in range(9)]
                url = "".join(url)
                try:
                    u = Taburl.objects.get(basic=url)
                except:
                    d = 0

            user = User.objects.get(id=pk)
            tab = Taburl()
            tab.user = user
            tab.basic = request.POST['url']
            tab.miniurl = url
            tab.nb = 0
            tab.save()

        return render(request, 'raccorcisor.html', {'ok': 1, 'msg': "127.0.0.1:8000/a/filter/" + url})
    else:
        return render(request,'raccorcisor.html',{'ok':0, 'msg': ""})

def stat(request, pk):
    user = User.objects.get(id=pk)
    try:
        hist = Taburl.objects.filter(user=user)
    except Exception as x:
        hist = []
    return render(request, 'stat.html',{"users":hist, "ok":1})

def filter(request,url):
    basic = Taburl.objects.get(miniurl=url)
    basic.nb = basic.nb + 1
    basic.save()
    return render(request,'filter.html',{"basic":basic.basic})