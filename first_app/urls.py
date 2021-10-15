from django.conf.urls import url
from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [
    path('', views.index,name = 'index'),
    path('index/',views.index,name = 'index'),
    # path('contact/',views.contact,name = 'contact'),
    path('form/', views.form, name = 'form'),
    path('test/',views.test,name = 'test'),

    path('db_test/',views.db_test,name = 'db_test'),
    path('musician_form_n/',views.musician_form_n,name = 'musician_form_n'),
    path('album_form/',views.album_form,name = 'album_form'),
    path('album_list/<int:artist_id>/',views.album_list,name = 'album_list'),
    path('edit_artist/<int:artist_id>/',views.edit_artist, name='edit_artist'),
    path('edit_album/<int:album_id>/',views.edit_album, name='edit_album'),
    path('delete_album/<int:album_id>/',views.delete_album, name='delete_album'),
    path('delete_artist/<int:artist_id>/',views.delete_artist, name='delete_artist'),
    path('template_view/',views.template_view, name='template_view'),


    # class view method 
    path('indexview/',views.IndexView.as_view(), name = 'indexview'),
    path('base_new/',views.base_new, name = 'base_new'),
    path('musician_details/<pk>/',views.MusicianDetail.as_view(), name = 'musician_details'),
    path('add_musician_n/',views.AddMusician.as_view(), name = 'add_musician_n'),
    path('musician_update/<pk>/',views.UpdateMusician.as_view(), name = 'musician_update'),
    path('delete_musician/<pk>/',views.DeleteMusician.as_view(), name = 'delete_musician'),



]

