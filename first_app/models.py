from django.db import models
from django.urls import reverse
# Create your models here.

class Musician(models.Model):
    # id = models.AutoField(Primary_key = True)  auto declare as primary key
    first_name = models.CharField(max_length=50)  #required thakle khali rakha jay na
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    # class Meta:
    #     db_table = "Musician"

    def __str__(self):
        return self.first_name + " "+self.last_name

    def get_absolute_url(self):
        return reverse("first_app:musician_details", kwargs={'pk':self.pk})

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete = models.CASCADE , related_name = 'album_list')
    name = models.CharField(max_length=100)
    release_date = models.DateField(default = None)

    rating = (
        (1, "Wrost"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent!"),
    )

    star_num = models.IntegerField(choices=rating,default = None)

    # class Meta:
    #     db_table = "Album"

    def __str__(self):
        return self.name + " "+str(self.star_num)

    
