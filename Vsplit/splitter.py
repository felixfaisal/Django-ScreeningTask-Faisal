from moviepy.editor import *
from moviepy.video.tools.subtitles import file_to_subtitles
from .models import chunk,uploaded_audio,videos
#This folder contains functions used for Video Analysing 

def video_split(Video_path,Sub_path):
    clip=VideoFileClip('media/'+str(Video_path))
    sub=file_to_subtitles('media/'+str(Sub_path))
    count=0
    for i in sub:
        try:
            sub_clip=clip.subclip(i[0][0],i[0][1])
            sub_clip.write_videofile('media/'+str(count)+'.mp4')
            audio=sub_clip.audio
            audio.write_audiofile('media/'+str(count)+'.mp3')
            b=chunk()
            b.chunk=count
            b.Time_start=str(i[0][0])
            b.Time_end=str(i[0][1])
            b.Sequence=count
            b.Subtitle=i[1]
            b.Audio='media/'+str(count)+'.mp3'
            b.Video='media/'+str(count)+'.mp4'
            b.save()
            count=count+1
        except Exception:
            continue


        
def video_download():
    allvideos=chunk.objects.all()
    allchunks=[]
    ah=allvideos[0].Video
    ah='media/final_clip.mp4'
    for i in allvideos:
        clip=VideoFileClip(str(i.Video))
        allchunks.append(clip)
    
    final_clip=concatenate_videoclips(allchunks)
    final_clip.write_videofile(ah)

        
def setting_audio(chunk_id,audio_path):
    chunk.objects.filter(chunk=chunk_id).update(Audio=audio_path)
    all=chunk.objects.filter(chunk=chunk_id)
    for i in all:
        clip=VideoFileClip(str(i.Video))
        audio=AudioFileClip(str(audio_path))
        clip.write_videofile(str(i.Video),audio=str(audio_path))        
        i.save()
        

      