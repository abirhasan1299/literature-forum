from django.shortcuts import render,redirect
from .models import story
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# -------------Create your views here.----------------




#--------------------------------- Category-Wise-Story-List ---------------------------------------

def CatStoryList(request,cat):
   # data = story.objects.all().get(tag=cat)
    sata = story.objects.filter(tag=cat)
    name_tag = story.objects.filter(tag=cat)[:1]
    context = {'sata':sata,'name_tag':name_tag}

    return render(request,'story/story_list.html',context)


#---------------------------------Story Writing ---------------------------------------
@login_required
def WriteStory(request):
    try:
        if request.method == "POST":
            name = request.POST['title']
            tag = request.POST['choices']
            des = request.POST['about']
            thumb = request.FILES['files']
            unique_id = request.user
            author = str(request.user.first_name)+" "+str(request.user.last_name)
            if tag == '':
                messages.warning(request, "ক্যাটেগরি নির্বাচন করেন নি !")
                return redirect('StoyWrite')
            else:
                obj = story(title=name, tag=tag, description=des,
                            unique_id=unique_id, author=author,thumb=thumb)
                obj.save()
                messages.success(request,"গল্পটি আপলোড হয়েছে")
                return redirect('StoryHome')
    except:
        raise ValueError("Something wrong in value")
        
    context={}
    return render(request,'story/write_story.html',context)

#------------------------------------Front Page-----------------------------
def StoryHome(request):
    context = {}
    return render(request,'story/story.html',context)
#---------------------Story Reading Part--------------------------------
def ReadStory(request,pk):
    data = story.objects.filter(id=pk)
    context ={
        'data':data
    }
    return render(request,'story/story_read.html',context)