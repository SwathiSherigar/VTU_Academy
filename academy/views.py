# from django.shortcuts import get_object_or_404, render
# from .models import Branch, VideoLecture, VideoNote

# def home(request):
#     branches = Branch.objects.all()
#     video_lectures = VideoLecture.objects.all()
#     return render(request, 'index.html', {'branches': branches, 'video_lectures': video_lectures})

# def select_year_semester(request, branch_slug):
#     semester = request.GET.get('semester')  # For example, "semester=1"
#     year = request.GET.get('year')  # For example, "year=2024"

#     # Filter data by semester and year (modify according to your model fields)
#     videos_and_notes = VideoNote.objects.filter(semester=semester, year=year)
#     branch = get_object_or_404(Branch, slug=branch_slug)

#     context = {
#         'videos_and_notes': videos_and_notes,
#         'semester': semester,
#         'year': year,
#         'branch':branch
#     }
#     return render(request, 'select_year_semester.html',  context)

# def videos_notes(request, branch_slug):
#     branch = get_object_or_404(Branch, slug=branch_slug)
#     semester = request.GET.get('semester')  # For example, "semester=1"
#     year = request.GET.get('year')  
#     videos_and_notes = VideoNote.objects.filter(branch=branch,semester=semester,year=year)
#     print(branch_slug,branch)
#     return render(request, 'videos_notes.html', {'branch': branch, 'videos_and_notes': videos_and_notes,'semester':semester,'year':year})
from django.shortcuts import get_object_or_404, render
from .models import Branch, VideoLecture, VideoNote

def home(request):
    branches = Branch.objects.all()
    video_lectures = VideoLecture.objects.all()
    return render(request, 'index.html', {'branches': branches, 'video_lectures': video_lectures})


def select_year_semester(request, branch_slug):
    semester = request.GET.get('semester')
    year = request.GET.get('year')

    branch = get_object_or_404(Branch, slug=branch_slug)
    videos_and_notes = VideoNote.objects.filter(branch=branch, semester=semester, year=year)

    context = {
        'videos_and_notes': videos_and_notes,
        'semester': semester,
        'year': year,
        'branch': branch,
    }
    return render(request, 'select_year_semester.html', context)


def videos_notes(request, branch_slug):
    branch = get_object_or_404(Branch, slug=branch_slug)
    semester = request.GET.get('semester')
    year = request.GET.get('year')

    videos_and_notes = VideoNote.objects.filter(branch=branch, semester=semester, year=year).prefetch_related('notes_images')

    return render(request, 'videos_notes.html', {
        'branch': branch,
        'videos_and_notes': videos_and_notes,
        'semester': semester,
        'year': year
    })
