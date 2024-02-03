from django.urls import path
from content import views

# to access images
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.projects_list , name="projects_list"),
    path("experience_list/", views.experience_list , name="experience_list"),
]

# To access images 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
