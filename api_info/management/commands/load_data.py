# banks/management/commands/load_bank_data.py

import csv
from django.core.management.base import BaseCommand
from api_info.models import Bank

class Command(BaseCommand):
    help = 'Load bank data from CSV into the database'

    def handle(self, *args, **kwargs):
        banks = []
        with open('data/bank_branches.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                bank = Bank(
                    ifsc=row['ifsc'],
                    bank_id=row['bank_id'],
                    branch=row['branch'],
                    address=row['address'],
                    city=row['city'],
                    district=row['district'],
                    state=row['state'],
                    bank_name=row['bank_name']
                )
                banks.append(bank)
                
            # Bulk create all at once
            Bank.objects.bulk_create(banks, batch_size=10000)
        
        self.stdout.write(self.style.SUCCESS('Bank data loaded successfully.'))