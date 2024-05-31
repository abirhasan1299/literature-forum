from django.shortcuts import render,redirect
#import validators
import qrcode
from django.contrib import messages
from .models import person
from django.contrib.auth.models import User
from django.conf import settings
import base64
from django.contrib.auth.decorators import login_required

# Create your views here.
def public_profile(request,pk):
    datas = person.objects.all().get(id=pk)
    x = User.objects.filter(username=datas.unique_id)
    context ={
        'datas':datas,
        'x':x
    }
    return render(request,'profile/public.html',context)

@login_required
def userUpdate(request):

    data = person.objects.filter(unique_id=request.user)
    
    if request.method == "POST":

        nickname = request.POST['nickname']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        bio = request.POST['bio']
        rltn = request.POST['rltn']
        t1 = request.POST['t1']
        t2 = request.POST['t2']
        t3 = request.POST['t3']
        profession = request.POST['profession']
        death = request.POST['death']
        clr = request.POST['clr']
        dob = request.POST['dob']
        edu_q = request.POST['edu_q']
        dept_sub = request.POST['dept_sub']
        edu_ins = request.POST['edu_ins']
        fb = request.POST['fb']
        youtube = request.POST['youtube']
        insta = request.POST['insta']
        unique_id = request.user

        if t1 == t2 or t1 == t3 or t2 == t3:
            messages.warning(request, "অভিন্ন টাইটেল যুক্ত করুন")
            return redirect('userUpdate')

        if validators.url(fb) == True:
            if validators.url(insta) == True:
                if validators.url(youtube) == True:
                    data = person.objects.filter(unique_id=request.user).update(nickname=nickname, gender=gender, unique_id=unique_id, bio=bio, mobile=mobile, relationship_status=rltn, tags_1=t1, tags_2=t2, tags_3=t3,
                                 profession=profession, fav_clr=clr, edu_qual=edu_q, edu_ins=edu_ins, depart_sub=dept_sub, dob=dob, fb=fb,death=death, youtube=youtube, insta=insta)
                    
                    return redirect("profile")
                else:
                    messages.warning(request, 'Youtube লিংক ভুল হয়েছে')
                    return redirect("userUpdate")
            else:
                messages.warning(request, 'Instagram লিংক ভুল হয়েছে')
                return redirect("userUpdate")
        else:
            messages.warning(request, 'Facebook লিংক ভুল হয়েছে')
            return redirect("userUpdate")


    context={
        'data':data
    }
    return render(request,'profile/user-update.html',context)

@login_required
def PersonHome(request):

    data = person.objects.filter(unique_id=request.user)
    

    context={
        'data':data
    }
    return render(request,'profile/main.html',context)

@login_required
def profile(request):

    if request.method=="POST":

        nickname = request.POST['nickname']    
        gender = request.POST['gender']    
        mobile = request.POST['mobile']
        bio = request.POST['bio']    
        rltn = request.POST['rltn']    
        t1 = request.POST['t1']    
        t2 = request.POST['t2']    
        t3 = request.POST['t3']    
        profession = request.POST['profession']    
        clr = request.POST['clr']    
        dob = request.POST['dob']    
        edu_q = request.POST['edu_q']    
        dept_sub = request.POST['dept_sub']    
        edu_ins = request.POST['edu_ins']   
        fb = request.POST['fb']    
        youtube = request.POST['youtube']    
        insta = request.POST['insta']
        unique_id = request.user

        sample_string = str(request.user.username)+str(request.user.email)

        sample_string_bytes = sample_string.encode("ascii")
        
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        data = base64_string

        img = qrcode.make(data)
        img_name = data+'.png'

        
        if t1==t2 or t1==t3 or t2==t3:
            messages.warning(request,"অভিন্ন টাইটেল যক্ত করুন")
            return redirect('updateprofile')

        if validators.url(fb)==True:
            if validators.url(insta)==True:
                if validators.url(youtube)==True:

                    obj = person(nickname=nickname, gender=gender, unique_id=unique_id, bio=bio, mobile=mobile, relationship_status=rltn, tags_1=t1, tags_2=t2, tags_3=t3, profession=profession, fav_clr=clr, edu_qual=edu_q, edu_ins=edu_ins, depart_sub=dept_sub, dob=dob, fb=fb, youtube=youtube, insta=insta, qr_code_name=img_name)

                    img.save(settings.MEDIA_ROOT + '/qrcode/' + img_name)

                    obj.save()
                    return redirect("profile")
                else:
                    messages.warning(request,'Youtube লিংক ভুল হয়েছে')
                    return redirect("updateprofile")
            else:
                messages.warning(request, 'Instagram লিংক ভুল হয়েছে')
                return redirect("updateprofile")
        else:
            messages.warning(request, 'Facebook লিংক ভুল হয়েছে')
            return redirect("updateprofile")
    
    context={}
    return render(request,"profile/update.html",context)