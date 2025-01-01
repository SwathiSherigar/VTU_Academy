
# from django.contrib import admin
# from .models import Branch, VideoLecture, VideoNote
# admin.site.register(Branch)
# admin.site.register(VideoNote)
# admin.site.register(VideoLecture)

from django.contrib import admin
from .models import VideoNote, NotesImage, Branch, VideoLecture

class NotesImageInline(admin.TabularInline):
    model = NotesImage
    extra = 1  # Display one empty image form by default


class VideoNoteAdmin(admin.ModelAdmin):
    inlines = [NotesImageInline]
    list_display = ('title', 'branch', 'semester', 'year')
    search_fields = ('title', 'branch__name')


admin.site.register(VideoNote, VideoNoteAdmin)

admin.site.register(Branch)
admin.site.register(VideoLecture)
