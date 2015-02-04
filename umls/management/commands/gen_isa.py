from collections import defaultict
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from umls.models import MRREL

class Command(BaseCommand):
    args = 'SAB'
    help = 'The terminology for which we need to generate a ISA hierarchy'

    def handle(self, *args, **options):

	parents = defaultdict(list)
	mrrels = MRREL.objects.all()			
	for mrrel in mrrels:
		parents[mrrel.CHILD_CUI].append(mrrel.PARENT_CUI)

	


