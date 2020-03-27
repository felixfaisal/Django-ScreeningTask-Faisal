from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .forms import VideoForm,AudioForm
from .models import chunk,uploaded_audio,videos
from .splitter import video_split,setting_audio,video_download
from .serializers import VideoSerializer,ChunkSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from moviepy.editor import *

class VideoAPI(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=VideoSerializer
    queryset=videos.objects.all()
   
    
    def get(self,request):
        return self.list(request)

    def post(self,request):
        form=VideoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        all=videos.objects.get()
        Video=all.Video
        Sub=all.Sub
        a=video_split(Video,Sub)
        
        #video_path='uploaded/'+str(request.data['Video'])
        #sub_path='uploaded/'+request.data['Sub']
        #video_split(video_path,sub_path)
        try:
            return self.create(request)
        except Exception:
            return HttpResponse(200)

class ChunkAPI(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=ChunkSerializer
    queryset=chunk.objects.all()
    
    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


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

