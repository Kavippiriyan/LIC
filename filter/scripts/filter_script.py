# import random

# from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Restaurent, Rating, Sale
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower



# class Command(BaseCommand):
#     help = 'Creates application data'

#     def handle(self, *args, **kwargs):
#         # get or create an admin user
#         user = User.objects.filter(username='admin')
#         if not user.exists():
#             user = User.objects.create_superuser(username='admin', password='test')
#         else:
#             user = user.first()

# def run():

#     restaurent =[
#     {'name': 'Pizzeria 1', 'date_opened': timezone.now() - timezone.timedelta(days=20), 'Restaurent_type': Restaurent.Typechoices.ITALIAN, 'latitude': 55.869829854, 'logitude': -4.28583219},
#     {'name': 'Pizzeria 2', 'date_opened': timezone.now() - timezone.timedelta(days=27), 'Restaurent_type': Restaurent.Typechoices.ITALIAN, 'latitude': 55.862, 'logitude': -4.247},
#     {'name': 'Golden Dragon', 'date_opened': timezone.now() - timezone.timedelta(days=15), 'Restaurent_type': Restaurent.Typechoices.CHINESE, 'latitude': 55.953251, 'logitude':  -3.188267},
#     {'name': 'Bombay Bustle', 'date_opened': timezone.now() - timezone.timedelta(days=44), 'Restaurent_type': Restaurent.Typechoices.INDIAN, 'latitude': 51.509865, 'logitude':  -0.118092},
#     {'name': 'McDonalds', 'date_opened': timezone.now() - timezone.timedelta(days=51), 'Restaurent_type': Restaurent.Typechoices.FASTFOOD, 'latitude': 53.483959, 'logitude':  -2.244644},
#     {'name': 'Taco Bell', 'date_opened': timezone.now() - timezone.timedelta(days=12), 'Restaurent_type': Restaurent.Typechoices.FASTFOOD, 'latitude': 53.413959, 'logitude':  -2.254644},
#     {'name': 'Chinese 2', 'date_opened': timezone.now() - timezone.timedelta(days=31), 'Restaurent_type': Restaurent.Typechoices.CHINESE, 'latitude': 53.400002, 'logitude':  -2.983333},
#     {'name': 'Chinese 3', 'date_opened': timezone.now() - timezone.timedelta(days=71), 'Restaurent_type': Restaurent.Typechoices.CHINESE, 'latitude': 55.070859, 'logitude':  -3.60512},
#     {'name': 'Indian 2', 'date_opened': timezone.now() - timezone.timedelta(days=46), 'Restaurent_type': Restaurent.Typechoices.INDIAN, 'latitude': 53.350140, 'logitude':  -6.266155},
#     {'name': 'Mexican 1', 'date_opened': timezone.now() - timezone.timedelta(days=52), 'Restaurent_type': Restaurent.Typechoices.MEXICAN, 'latitude': 51.481583, 'logitude':  -3.179090},
#     {'name': 'Mexican 2', 'date_opened': timezone.now() - timezone.timedelta(days=50), 'Restaurent_type': Restaurent.Typechoices.MEXICAN, 'latitude': 55.847258, 'logitude':  -4.440114},
#     {'name': 'Pizzeria 3', 'date_opened': timezone.now() - timezone.timedelta(days=4), 'Restaurent_type': Restaurent.Typechoices.ITALIAN, 'latitude': 54.966667, 'logitude':  -1.600000},
#     {'name': 'Pizzeria 4', 'date_opened': timezone.now() - timezone.timedelta(days=61), 'Restaurent_type': Restaurent.Typechoices.ITALIAN, 'latitude': 48.856614, 'logitude':  2.3522219},
#     {'name': 'Italian 1', 'date_opened': timezone.now() - timezone.timedelta(days=37), 'Restaurent_type': Restaurent.Typechoices.ITALIAN, 'latitude': 41.902782, 'logitude':  12.496366},

#     ]
#     Restaurent.objects.all().delete()

#     for i in restaurent:
#         Restaurent.objects.create(**i)

def run():


           #  Filter only Chinese Restaurent
    # restaurent = Restaurent.objects.filter(Restaurent_type = Restaurent.Typechoices.CHINESE)
    # print(restaurent)
    # print(connection.queries)

        # Filter the pizzeria 1 restaurent
    # restaurent = Restaurent.objects.filter(name = "Pizzeria 1")
    # print(restaurent.count())
    # print(connection.queries)

        # get method we can use only for particular element not a all values
    # restaurent = Restaurent.objects.filter(name = "Pizzeria 1")
    # print(restaurent.get())
    # print(connection.queries)
   
        # Here we can't give get becaues it returns more than 1 rows
    # restaurent = Restaurent.objects.filter(Restaurent_type = 'IT')
    # print(restaurent.count())
    # print(connection.queries)


        # exists function is calling whether the value is present or not it wil give output booleans
    # restaurent = Restaurent.objects.filter(name = "Pizzeria ")
    # print(restaurent.exists())
    # print(connection.queries)

        # It gives output like what is there in the particular field
    # restaurent = Restaurent.objects.filter(Restaurent_type__in=['IT', 'IN'])
    # print(restaurent)
    # print(restaurent.count())


        # AND
    # restaurent = Restaurent.objects.filter(Restaurent_type = "CH", name__startswith='C')
    # print(restaurent)
    # print(restaurent.count())
    # restaurent = Restaurent.objects.filter(Restaurent_type = "CH")
    # print(restaurent)
    # print(restaurent.count())

        # except this give other values
    # restaurent = Restaurent.objects.exclude(Restaurent_type = "CH",name__startswith="C")
    # print(restaurent)
    # print(restaurent.count())

            # less than lookup
    # restaurent = Restaurent.objects.filter(name__lt = "C")
    # print(restaurent.count())
    # print(restaurent)

        # Filtering the Range queries -- between and
    # sale = Sale.objects.filter(income__range=(5,10))
    # print(sale)
    # print(sale.count())


        # Printing the individual values of income
    # sale = Sale.objects.filter(income__range=(5,10))
    # print([sales.income for sales in sale])
    # print(sale.count())


        # Order By name ASC
    # restaurent =Restaurent.objects.order_by('name')
    # print(restaurent)

        # Order By name ASC    
    # restaurent =Restaurent.objects.order_by('name').reverse()
    # print(restaurent)
    # print(connection.queries[-1])

    # restaurent =Restaurent.objects.order_by('-name')
    # print(restaurent)
    # pprint(connection.queries[-1])

    # sales =Sale.objects.order_by('time')
    # print([sale.time for sale in sales])
    # print(connection.queries[-1])


    # restaurent =Restaurent.objects.first()
    # print(restaurent)
    
    # restaurent =Restaurent.objects.order_by('name')
    # pprint(restaurent)
    # pprint(connection.queries[-1])


            # Converting to lowercase
    # restaurent =Restaurent.objects.order_by(Lower('name'))
    # pprint(restaurent)
    # pprint(connection.queries[-1])

    
    # restaurent.name = restaurent.name.lower()
    # restaurent.save()

    # print(connection.queries[-1])
   
    
    # restaurent =Restaurent.objects.first()
    # print(restaurent)
    

    # Index and Slicing

    # restaurent = Restaurent.objects.order_by('date_opened')[0]
    # print(restaurent)
    # pprint(connection.queries[-1])

    # restaurent = Restaurent.objects.order_by('date_opened')[:1]
    # print(restaurent)
    # pprint(connection.queries[-1])

    # restaurent = Restaurent.objects.order_by('date_opened')[2:6]
    # print(restaurent)
    # pprint(connection.queries[-1])

    # restaurent = Restaurent.objects.all()
    # for r in restaurent:
    #     if r.name.lower() == r.name:
    #         print(r.__dict__)



        # Earliest , latest method (when you work with datetime)


        # restaurent = Restaurent.objects.earliest('date_opened')
        # print(restaurent)
        # # pprint(connection.queries)


        # restaurent = Restaurent.objects.latest('date_opened')
        # print(restaurent)
        # # pprint(connection.queries)


            # model page latest classs Meta:
        # latest_restaurent = Restaurent.objects.latest('date_opened')
        # print(latest_restaurent)

        # pprint(connection.queries)
    

        # ratings= Rating.objects.filter(Restaurent__name__startswith= 'C')
        # print(ratings)
        # pprint(connection.queries[-1]) 

        
        sales= Sale.objects.filter(Restaurent__name__startswith= 'C')
        print(sales)
        pprint(connection.queries[-1]) 