from django import forms
from django.core import validators
# from first_app.models import Musician,Album
from first_app import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"

        # exclude = ['first_name']  field bad dite ata use korte hbe 
        

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"











# def even_or_odd(value):
#     if value % 2 == 1:
#         raise forms.ValidationError("Please insert an even value")



# class user_form(forms.Form):
    # user_name = forms.CharField(label="Full Name",widget=forms.TextInput(attrs={'placeholder':'Enter your name'}))  #required = false and ..........initial="Sagor"
    # user_email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'style':'background : yellow'}))
    # user_dob = forms.DateField(label = "Date of Birth",widget=forms.TextInput(attrs={'type':'date'}))


    # boolean_field = forms.BooleanField()
    # char_field = forms.CharField(max_length=15,min_length=5)
    # choice_field = forms.ChoiceField(choices=(('','---SELECT OPTION---'),('Pabna','Pabna'),('Dhaka','Dhaka'),('Sirajgonj','sirajgonj')))
    # choice = (('apple','apple'),('banana','banana'),('cat','cat'), ('dog','dog'))
    # radio_field = forms.ChoiceField(choices=choice, widget=forms.RadioSelect)
    # multi_field = forms.MultipleChoiceField(choices=choice, widget=forms.CheckboxSelectMultiple)


    # validators example
    # val_name = forms.CharField(validators=[validators.MaxLengthValidator(10)])

    # number_field = forms.IntegerField(validators = [even_or_odd])

    # user_email = forms.EmailField()
    # user_vmail = forms.EmailField()

    # def clean(self):
    #     all_cleaned_data = super().clean()
    #     user_email = all_cleaned_data['user_email']
    #     user_vmail = all_cleaned_data['user_vmail']

    #     if user_email != user_vmail:
    #         raise forms.ValidationError("Fields Dont Matched")





