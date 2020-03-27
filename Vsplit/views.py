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
        try:
            return self.create(request)
        except Exception:
            return HttpResponse(200)

class ChunkAPI(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin):
    serializer_class=ChunkSerializer
    queryset=chunk.objects.all()
    lookup_field='chunk'
    
    def get(self,request,chunk=None):
        if id:
            return(self.retrieve(request))
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

class ChunksAPI(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin):
    serializer_class=ChunkSerializer
    queryset=chunk.objects.all()
    
    def get(self,request,chunk=None):
            return self.list(request)


def list(request):
        all = chunk.objects.all()
        m=request.GET.get('Button',False)
        if request.method=='POST':
            allz = uploaded_audio.objects.all()
            for i in allz:
                i.delete()
            form=AudioForm(request.POST,request.FILES)
            print(form)
            chunk_id=request.POST.get('Button',False)
            chunk_id=int(chunk_id)
            if form.is_valid():
                form.save()
            allz=uploaded_audio.objects.get()
            audio_path = 'media/'+str(allz.Audio)
            setting_audio(chunk_id,audio_path)
            video_download()
            print('Should upload')

        
        form=AudioForm()
        return render(request,'list.html',{'all':all,'form':form})
    
def home(request):
    if request.method == 'POST':
        form=VideoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        all=videos.objects.get()
        Video=all.Video
        Sub=all.Sub
        video_split(Video,Sub)
        return redirect('list')
    else:
        all = videos.objects.all()
        for i in all:
            i.delete()
        all = chunk.objects.all()
        for i in all:
            i.delete()
        
        form = VideoForm()
        return render(request,'upload.html',{'form':form})

