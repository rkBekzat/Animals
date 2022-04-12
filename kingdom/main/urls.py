from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.AnimalDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.AnimalUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.AnimalDeleteView.as_view(), name='delete')
]