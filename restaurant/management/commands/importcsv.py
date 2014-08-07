import csv
import datetime

from django.core.management import BaseCommand
from restaurant.models import Restaurant

def to_bool(s):
    if s in ['1', 'True']:
        return True
    elif s in ['0', 'False']:
        return False
    else:
        raise Exception('Cannot convert {} into boolean'.format(s))

def to_date(s):
    if s in ['inconnu', 'aucune']:
        return None
    else:
        return datetime.datetime.strptime(s, "%d/%m/%Y").date()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if Restaurant.objects.all().count():
            print("La base de donnée n'est pas vide. Merci de la vider à la main ou d'arrêter de faire n'importe quoi, va te coucher maintenant.")
            return
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
                               date_immatriculation=to_date(row[11]),
                               date_radiation=to_date(row[12]),
                               site_web=row[13],
                               statut_societe=row[14],
                               contact=to_bool(row[15]),
                               interview=to_bool(row[16]),
                               annuaire_alloparis=to_bool(row[17]),
                               annuaire_hansik=to_bool(row[18]),
                               radiation=to_bool(row[19]),
                               nolebang=to_bool(row[20]),
                               notes=row[21])
                r.save()
            print(Restaurant.objects.all())