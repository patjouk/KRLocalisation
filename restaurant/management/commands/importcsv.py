import csv
import datetime

from django.core.management import BaseCommand
from restaurant.models import Restaurant

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('/home/nokomis/Thèse/base de données/base_restau.txt', newline='') as f:
            reader = csv.reader(f, delimiter=';')
            i = iter(reader)
            next(i)
            Restaurant.objects.all().delete()
            print(Restaurant.objects.all())
            for row in i:
                r = Restaurant(num_entree=row[0],
                               nom=row[1],
                               nom_coreen=row[2],
                               latitude=row[3],
                               longitude=row[4],
                               code_postal=row[5],
                               adresse=row[6],
                               num_tel=row[7],
                               num_siret=row[8],
                               proprietaire=row[9],
                               proprietaire_coreen=row[10],
                               #date_immatriculation=datetime.datetime.strptime(row[11], "%d/%m/%Y").date() if row[11] else None,
                               #date_radiation=datetime.datetime.strptime(row[12], "%d/%m/%Y").date() if row[12] else None,
                               site_web=row[13],
                               statut_societe=row[14],
                               #contact=row[15],
                               #interview=row[16],
                               #annuaire_alloparis=row[17],
                               #annuaire_hansik=row[18],
                               #radiation=row[19],
                               #nolebang=row[20],
                               notes=row[21])
                r.save()
            print(Restaurant.objects.all())