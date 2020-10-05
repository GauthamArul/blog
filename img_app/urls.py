from django.urls import path
from . import views

urlpatterns = [
    
    path('create_user',views.UserView.as_view(),name='create_user'),
    path('addpicture/', views.PictureUploadView.as_view(),name='addpicture'),
    
]