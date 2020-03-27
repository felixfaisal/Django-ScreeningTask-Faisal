from django.contrib import admin
from .models import videos,chunk,uploaded_audio
# Register your models here.

admin.site.register(videos)
admin.site.register(chunk)
admin.site.register(uploaded_audio)
