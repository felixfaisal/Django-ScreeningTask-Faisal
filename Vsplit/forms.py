from django import forms
from .models import videos,uploaded_audio

class VideoForm(forms.ModelForm):
    class Meta:
        model=videos
        fields=('Video','Sub')

class AudioForm(forms.ModelForm):
    Audio = forms.FileField(widget=forms.FileInput, label='')
    class Meta:
        model=uploaded_audio
        fields=('Audio',)