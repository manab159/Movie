from django.db import models
from datetime import datetime  

# Create your models here.
class GenderChoice(models.Model):
	GENDER_CHOICES = (
		('M', "MALE"),
		('F', "FEMALE"),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES,unique=True)
	def __str__(self):
		return self.gender

class Actors(models.Model):
	name = models.CharField(max_length=50,unique=True)
	sex= models.ForeignKey("GenderChoice", on_delete=models.CASCADE)
	DOB= models.DateField()
	bio=models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Actors"
		verbose_name_plural = "Actors"

class Producers(models.Model):
	name=models.CharField(max_length=50,unique=True)
	sex=models.ForeignKey("GenderChoice", on_delete=models.CASCADE)
	DOB=models.DateField()
	bio=models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Producers"
		verbose_name_plural = "Producers"

class Movies(models.Model):
	name=models.CharField(max_length=50,unique=True)
	year_of_release=models.PositiveIntegerField(default=2010)
	plot=models.TextField(blank=True, null=True)
	poster=models.ImageField(upload_to='Documents/',blank=True)
	producer_id=models.ForeignKey(Producers, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Movies"
		verbose_name_plural = "Movies"
		unique_together = ('name', 'producer_id')

class ActorMovie(models.Model):
	actor_fk = models.ForeignKey(Actors, on_delete=models.CASCADE)
	movie_fk = models.ForeignKey(Movies, on_delete=models.CASCADE)
	def __str__(self):
		return '{}, {}'.format(self.actor_fk, self.movie_fk)
	class Meta:
		verbose_name = "ActorMovie"
		verbose_name_plural = "ActorMovie"
		unique_together = ('actor_fk', 'movie_fk')