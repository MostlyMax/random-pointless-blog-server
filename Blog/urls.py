from django.urls import path
from . import views

# define the urls
urlpatterns = [
    path('entries/', views.entries),
    path('featured/', views.featured),
    path('entry_detail/<int:pk>', views.entry_detail, name='entry-detail')
]