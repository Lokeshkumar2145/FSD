from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth.models import User
from .models  import feeds,comment,like_msg
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def dashboard(request):
    feed=feeds.objects.all()
    l=like_msg.objects.filter(liked=True)
    f=[int(x.feed_id) for x in l]
    cmt=comment.objects.select_related('feed_id').order_by('-date_cmt')
    return render(request,'dashboard/home.html',{'feed':feed,"f":f,'cmt':cmt})
def home(request):
 if request.user.is_authenticated:
    feed=feeds.objects.filter(user=request.user).select_related('user')
    l=like_msg.objects.filter(user=request.user,liked=True)
    f=[int(x.feed_id) for x in l]
    cmt=comment.objects.select_related('feed_id').order_by('-date_cmt')
    print(cmt)
    print(cmt.query)
    return render(request,"dashboard/index.html",{'feed':feed,"f":f,'cmt':cmt})
 return render(request,"dashboard/home.html")


def liked(request,uid):
   f=feeds.objects.get(pk=uid)
   try:
        l1=like_msg.objects.get(user=request.user,liked=True,feed_id=f.feed_id)
        if l1 is not None:
            l1.liked=False
            l1.save()
   except Exception as e:
         l=like_msg.objects.create(user=request.user,feed_id=f.feed_id,liked=True)
  
   return redirect('home')

def signup(request):
    if request.method=="POST":
        username=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['pass']
        confirm_password=request.POST['pass1']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'account/signup.html')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"UserName is Taken")
                return render(request,'account/signup.html')
        except Exception as e:
            messages.warning(request,e)
        try:
            user = User.objects.create_user(username=username,first_name=fname,last_name=lname,email=username)
            user.set_password(password)
            user.save()
            return render(request,"account/login.html")
        except Exception as e:
            messages.warning(request,e)
    return render(request,"account/signup.html")

    # return render(request,"account/signup.html")
def signin(request):
     if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        user=authenticate(username=username,password=userpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Login Success")
            return redirect('home')

        else:
            messages.error(request,"invalid Credentials ")
            return redirect("/account/login/")

        return render(request,"account/login.html")

     return render(request,"account/login.html")

def handle_logout(request):
    logout(request)
    return redirect('dashboard')

def comments(request,id):
    try:
        if  request.method=="POST":
            cmt=request.POST.get('comment')
            comment.objects.create(user=request.user,feed_id=feeds.objects.get(feed_id=id),text=cmt)
            return redirect('home')
        return redirect('home')
    except Exception as e:
        pass
    return redirect('home')


def delete_commennt(request,id):
    cmt=comment.objects.get(comment_id=id).delete()
    return redirect('home')


def all_feed(request):
    try:
        feed=comment.objects.all().select_related('feed_id')
        l=like_msg.objects.filter(liked=True)
        f=[int(x.feed_id) for x in l]
        print(feed.query)
        return render(request,'dashboard/all_dashboard.html',{'feed':feed,'f':f})
    except Exception as e:
        pass
    return render(request,'dashboard/all_dashboard.html',{'feed':feed})