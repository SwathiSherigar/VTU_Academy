from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('select-year-semester/<slug:branch_slug>/', views.select_year_semester, name='select_year_semester'),
    path('videos_notes/<slug:branch_slug>/', views.videos_notes, name='videos_notes'),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
