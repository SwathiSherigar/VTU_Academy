from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/select-year-semester/{self.slug}/"


class VideoLecture(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='video_lectures')
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/video-lecture/{self.id}/"


class VideoNote(models.Model):
    SEMESTER_CHOICES = [(i, f"Semester {i}") for i in range(1, 9)]

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='video_notes')
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/videos-note/{self.id}/"


class NotesImage(models.Model):
    video_note = models.ForeignKey(VideoNote, on_delete=models.CASCADE, related_name='notes_images')
    image = models.ImageField(upload_to='notes_images/')

    def __str__(self):
        return f"Image for {self.video_note.title}"
