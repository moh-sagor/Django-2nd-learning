from django.forms.fields import BooleanField
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from first_app.models import Musician,Album
from first_app import forms, models
from django.db.models import Avg
from django.views.generic import View, TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1':'List of Musician','musician':musician_list}
    return render(request,'first_app/index.html',context=diction)
     #<a href = '/contact/'>Contact</a>  (for linking )


# def contact(request):
#     return HttpResponse("<h1>Contact is <b>0174000</b></h1> <a href = '/first_app/name/'>Name</a> ") #<a href = '/contact/'>Contact</a>  (for linking )

def form(request):
    # for models.py section
    new_forms = forms.MusicianForm()

    if request.method == 'POST':
        new_forms = forms.MusicianForm(request.POST)

        if new_forms.is_valid():
            new_forms.save(commit=True)
            return index(request)

    diction ={'test_form':new_forms, 'heading_a':"Add New Musician"}

    return render(request,'first_app/form.html',context=diction)

def test(request):
    diction = {'text_2':"Testing Example of filter",}
    return render(request,'first_app/test.html',context=diction)


def db_test(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title':'Home Page' , 'musician_list':musician_list}
    return render(request,'first_app/home_index.html', context=diction)


def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(artist=artist_id).order_by('name')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('star_num'))
    diction = {'title':'List of Album','artist_info':artist_info,'album_list':album_list,'artist_rating':artist_rating}
    return render(request,'first_app/album_list.html', context=diction)

def musician_form_n(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        new_forms = forms.MusicianForm(request.POST)

        if new_forms.is_valid():
            new_forms.save(commit=True)
            return index(request)

    diction = {'title':'Add Musician','musician_form':form}
    return render(request,'first_app/musician_form_n.html', context=diction)


def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        new_forms = forms.AlbumForm(request.POST)

        if new_forms.is_valid():
            new_forms.save(commit=True)
            return index(request)

    diction = {'title':'Add Album','album_form':form}
    return render(request,'first_app/album_form.html', context=diction)


def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance = artist_info)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST,instance = artist_info)

        if form.is_valid():
            form.save(commit=True)
            return album_list(request, artist_id)

    diction = {'edit_form':form,'artist':artist_info}
    return render(request,'first_app/edit_artist.html',context=diction)


def edit_album(request,album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance = album_info)
    diction = {}

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST,instance = album_info)

        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'Successfully updated!'})

    diction.update({'edit_form':form})
    diction.update({'album_id':album_id})
    return render(request,'first_app/edit_album.html',context=diction)


def delete_album(request,album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'album':album,'delete_success':'Album deleted successfully'}
    return render(request,'first_app/delete_album.html',context=diction)


 
def delete_artist(request,artist_id):
    artist = Musician.objects.get(pk=artist_id).delete()
    diction = {'artist':artist,'delete_success':'Artist deleted successfully'}
    return render(request,'first_app/delete_artist.html',context=diction)

def base_new(request):
    return render(request, 'first_app/base_new.html', context={})





def template_view(request):
    return HttpResponse("Hello World")

# Template View
# class IndexView(TemplateView):
#     template_name = 'first_app/indexview.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context ['sample_text_1'] = 'Sample Text 1'
#         context ['sample_text_2'] = 'Sample Text 2'
#         return context


# list view 
class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/indexview.html'

# DetailView 
class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'first_app/musician_details.html'
    
# CreateView 
class AddMusician(CreateView):
    fields = '__all__'
    model = models.Musician
    template_name = 'first_app/musician_form.html'
# Update View 
class UpdateMusician(UpdateView):
    fields = '__all__'
    model = models.Musician
    template_name = 'first_app/musician_form.html'

# Delete View 
class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('first_app:indexview')
    template_name = 'first_app/delete_musician.html'












    # new_forms = forms.user_form()
    # diction = {'test_form':new_forms, 'msg_1':"This form is created by Django"}

    # if request.method == 'POST':
    #     new_forms = forms.user_form(request.POST,)
    #     diction.update({'test_form':new_forms})
        

        # if new_forms.is_valid():
            # user_name = new_forms.cleaned_data['user_name']
            # user_email = new_forms.cleaned_data['user_email']
            # user_dob = new_forms.cleaned_data['user_dob']

            # boolean_field = new_forms.cleaned_data['boolean_field']
            # char_field = new_forms.cleaned_data['char_field']
            # choice_field = new_forms.cleaned_data['choice_field']
            # radio_field = new_forms.cleaned_data['radio_field']
            # multi_field = new_forms.cleaned_data['multi_field']

            # val_name = new_forms.cleaned_data['val_name']




            # diction.update({'user_name':user_name})
            # diction.update({'user_email':user_email})
            # diction.update({'user_dob':user_dob})
            # diction.update({'boolean_field':boolean_field})
            # diction.update({'char_field':char_field})
            # diction.update({'choice_field':choice_field})
            # diction.update({'radio_field':radio_field})
            # diction.update({'multi_field':multi_field})

            # diction.update({'val_name':val_name})

            # # diction.update({'field': new_forms.cleaned_data['number_field']})
            # diction.update({'field':'Field Matched !'})

            # diction.update({'form_submited':"YES"})


    # return render(request,'first_app/form.html',context=diction)
