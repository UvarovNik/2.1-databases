import csv
import os

import django

from django.core.management.base import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones data from CSV file'

    def handle(self, *args, **options):
        csv_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'phones.csv')
        csv_path = os.path.normpath(csv_path)

        with open(csv_path, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(
                name=phone['name'],
                price=int(phone['price']),
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'] == 'True',
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(phones)} phones'))
