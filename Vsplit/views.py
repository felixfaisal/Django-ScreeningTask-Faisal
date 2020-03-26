from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import VideoForm,AudioForm
from .models import chunk,uploaded_audio,videos
from .splitter import video_split,setting_audio,video_download


# Create your views here.
def news(request):
    return render(request,'news.html')

def list(request):
        all = chunk.objects.all()
        m=request.GET.get('Button',False)
        if m==str(963):
            print('Should donwload')
            a=video_download()
            print(a)
        elif request.method=='POST':
            allz = uploaded_audio.objects.all()
            for i in allz:
                i.delete()
            form=AudioForm(request.POST,request.FILES)
            #print(request.GET)
            #print(request.POST)
            print(form)
            
            chunk_id=request.POST.get('Button',False)
            chunk_id=int(chunk_id)
            #print(form.is_valid())
            if form.is_valid():
                form.save()
            allz=uploaded_audio.objects.get()
            type(allz)
            audio_path = 'media/'+str(allz.Audio)
            setting_audio(chunk_id,audio_path)
            #print(audio)
            print('Should upload')

        
        form=AudioForm()
        return render(request,'list.html',{'all':all,'form':form})
    
def home(request):
    if request.method == 'POST':
       
        form=VideoForm(request.POST,request.FILES)
        #print(request.POST)
        if form.is_valid():
            form.save()
        all=videos.objects.get()
        Video=all.Video
        Sub=all.Sub
        a=video_split(Video,Sub)
        print(Video)
        #print(a)
        
        return redirect('list')
    else:
        all = videos.objects.all()
        for i in all:
            print(i)
            i.delete()
        
        form = VideoForm()
        return render(request,'upload.html',{'form':form})

