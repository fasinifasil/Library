from .import views
from django.urls import path
app_name='app1'
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('book/<int:book_id>/',views.detail,name='detail'),
    path('add',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
