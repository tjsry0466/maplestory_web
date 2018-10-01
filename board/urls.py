from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from . import views

app_name='board'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('download/', views.TemplateView.as_view(template_name='board/download.html'), name='download'),
    path('ranking/', TemplateView.as_view(template_name="ranking.html"), name='ranking'),
    path('like/', views.Board_like, name='like'),
    path('board/<str:slug>', views.BoardLV.as_view(), name='list'),
    path('board/<slug:categorySlug>/new', views.BoardNew , name='boardnew'),
    path('board/<str:category>/<str:slug>', views.BoardDetail.as_view(), name='detail'),
    path('boardcontrol/<int:pk>/delete', views.Boarddelete.as_view(), name='boarddelete'),
    path('boardcontrol/<int:pk>/update', views.Boardupdate, name='boardupdate'),
    path('comment/<str:boardslug>/new', views.CommentNew, name='commentnew'),
    path('commentcontrol/<int:pk>/delete', views.Commentdelete.as_view(), name='commentdelete')
    
]
