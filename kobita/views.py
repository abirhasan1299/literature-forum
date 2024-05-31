from django.shortcuts import render,redirect,HttpResponseRedirect
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from person.models import person

# Create your views here.
def bnNumber(request):
    value= ''
    digit = str(request)
    for i in range(len(digit)):
        if digit[i]=='0':
            value +='০'
        elif digit[i]=='1':
            value += '১'
        elif digit[i]=='2':
            value += '২'
        elif digit[i]=='3':
            value += '৩'
        elif digit[i]=='4':
            value += '৪'
        elif digit[i] == '5':
            value += '৫'
        elif digit[i] == '6':
            value += '৬'
        elif digit[i] == '7':
            value += '৭'
        elif digit[i]=='8':
            value += '৮'
        elif digit[i] == '9':
            value += '৯'
    return value

def readpoem(request,pk,name):
    obj = Poem.objects.all().get(id=pk,poem_name=name)
    author = person.objects.filter(unique_id = obj.unique_id)

    cmt = comment.objects.filter(poem_unique_id=pk).order_by('-id')

    cmt_count = comment.objects.filter(poem_unique_id=pk).count()

    related_poem = Poem.objects.filter(tag=obj.tag).order_by('-id')
 
    view = (obj.view)+1
    view_ins = Poem.objects.filter(id=pk).update(view=view)

    view_data = bnNumber(obj.view)
    
    cmt_data = bnNumber(cmt_count)

    if request.method=="POST":
        username = request.user.username
        fullname = f"{request.user.first_name} {request.user.last_name}"
        cmt = request.POST['comment']
        poem_unique_id = request.POST['id']
        date = datetime.datetime.now()
        
        obj = comment(username=username,fullname=fullname,cmt=cmt,poem_unique_id=poem_unique_id,date_time=date)
        obj.save()
        return HttpResponseRedirect(request.build_absolute_uri())

    context={
        'obj':obj,
        'author':author,
        'cmt':cmt,
        'cmt_data':cmt_data,
        'related_poem':related_poem,
        'view_data': view_data
    }
   
    return render(request,'kobita/read-poem.html',context)


def KobitaHome(request):

    poem = Poem.objects.all().order_by('-id')
    most_read = Poem.objects.all().order_by('-view')
    romantic_poem = Poem.objects.all().filter(tag='রোম্যান্টিক')
    country = Poem.objects.all().filter(tag='দেশাত্মবোধক')
    eighteen_plus = Poem.objects.all().filter(tag='আঠারো উর্ধ্ব')
    social = Poem.objects.all().filter(tag='সমাজকেন্দ্রিক')
    kishor = Poem.objects.all().filter(tag='কিশোর')
    nature = Poem.objects.all().filter(tag='প্রকৃতিপ্রেম')
    wake = Poem.objects.all().filter(tag='জাগরন মূলক')
    love = Poem.objects.all().filter(tag='ভালোবাসা-প্রেম')
    sad = Poem.objects.all().filter(tag='দুঃখের কবিতা')
    child = Poem.objects.all().filter(tag='শিশু কবিতা')

    sql = 'SELECT "person_person"."id", "person_person"."nickname", "person_person"."gender", "person_person"."death", "person_person"."unique_id_id", "person_person"."bio", "person_person"."mobile", "person_person"."relationship_status", "person_person"."tags_1", "person_person"."tags_2", "person_person"."tags_3", "person_person"."profession", "person_person"."fav_clr", "person_person"."edu_qual", "person_person"."edu_ins", "person_person"."depart_sub", "person_person"."dob", "person_person"."fb", "person_person"."youtube", "person_person"."insta", "person_person"."qr_code_name", "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" FROM "person_person" INNER JOIN "auth_user" ON ("person_person"."unique_id_id" = "auth_user"."id")'

    badge_author= person.objects.raw(sql)
    
    # for b in badge_author:
    #     print(str(b.nickname)+"-"+str(b.username +
    #           "-"+str(b.email)+"-"+str(b.date_joined)))
    
    context={
        'poem':poem,
        'most_read':most_read,
        'romantic_poem': romantic_poem,
        'country':country,
        'eighteen_plus': eighteen_plus,
        'social':social,
        'kishor':kishor,
        'nature':nature,
        'wake':wake,
        'love':love,
        'sad':sad,
        'child':child,
        'badge_author':badge_author
    }
    return render(request,'kobita/main.html',context)
@login_required
def WritePoem(request):
    if request.method=="POST":

        title = request.POST['title'] 
        author = request.POST['author']
        view = request.POST['view'] 
        tag = request.POST['category'] 
        description = request.POST['detail']
        posted_time = datetime.datetime.now()
        unique_id = request.user
        obj = Poem(unique_id=unique_id,author=author,poem_name=title,poem_description=description,view=view,date=posted_time,tag=tag)
        obj.save()

        return redirect("HomeKobita")

    context = {}

    return render(request,'kobita/create.html',context)

