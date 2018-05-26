from django.contrib import admin
from imdb.models import *
# Register your models here.


class CustProducer(admin.ModelAdmin):
	list_display=('name','sex','DOB','bio')
	list_filter=('DOB','sex')
admin.site.register(Producers, CustProducer)

class CustMovie(admin.ModelAdmin):
	def producer(self, model_object):
		producer=Producers.objects.get(pk=model_object.producer_id.pk).name
		return producer
	def actors(self,model_object):
		actorList=""
		actor=ActorMovie.objects.filter(movie_fk=model_object.pk).values_list('actor_fk',flat=True)
		for x in actor:
			actorList+=''.join(Actors.objects.get(pk=x).name)+" , "
		return actorList
		# if model_object.name[0].lower()=='s': return mark_safe('<h1> YES </h1>')
		# else: return False
	list_display=('name','year_of_release','producer','actors')
	list_filter=('name','year_of_release')
admin.site.register(Movies, CustMovie)

class CustActor(admin.ModelAdmin):
	list_display=('name','sex','DOB','bio')
	list_filter=('sex','DOB')

admin.site.register(Actors,CustActor)

class CustActorMovie(admin.ModelAdmin):
	list_display=('actor_fk','movie_fk')
	list_filter=('actor_fk','movie_fk')
	


admin.site.register(ActorMovie,CustActorMovie)
admin.site.register(GenderChoice)