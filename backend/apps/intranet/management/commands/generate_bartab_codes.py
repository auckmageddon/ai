from django.core.management.base import BaseCommand

from apps.intranet.models import BarTab

import random
import string
from optparse import make_option


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--value',
            dest='value',
            type='int',
            default=50,
            help='Value of added bartabs'),
        make_option('--number',
            dest='num',
            type='int',
            default=10,
            help='Number of bartabs to add'),
    )

    def handle(self, *args, **options):
        for n in range(options['num']):
            while True:
                _code = ''.join(['%x' % (random.randint(0, 16)) for x in range(32)])
                try:
                    BarTab.objects.get(code=_code)
                except BarTab.DoesNotExist:
                    break
            while True:
                _confirmation = ''.join([random.choice(string.ascii_lowercase) for x in range(8)])
                try:
                    BarTab.objects.get(confirmation=_confirmation)
                except BarTab.DoesNotExist:
                    break
            bt = BarTab(code=_code, confirmation=_confirmation, value=options['value'])
            bt.save()
