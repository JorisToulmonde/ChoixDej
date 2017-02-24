from celery.task.schedules import crontab
from celery.decorators import periodic_task
from datetime import datetime
from django.db import connection
from collections import namedtuple
from index.models import Restaurant, Groupes

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab()))
def hello():
	with connection.cursor() as cursor:
		#Incremente l'anciennete des restaurants
		cursor.execute("UPDATE index_restaurant SET anciennete = anciennete + 1")

		#Reactualise le score des restaurants
		cursor.execute("UPDATE index_restaurant, star_ratings_rating SET index_restaurant.score = index_restaurant.anciennete - index_restaurant.frequence + 3 * star_ratings_rating.average where index_restaurant.id = star_ratings_rating.object_id")

		#Remet les prensences a 0
		cursor.execute("UPDATE index_groupes SET present = 0")
