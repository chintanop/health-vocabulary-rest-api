import copy
from collections import defaultdict
from django.core.management.base import BaseCommand
from umls.models import MRREL
from umls.models import ISA


class Command(BaseCommand):
    args = 'SAB'
    help = 'The terminology for which we need to generate a ISA hierarchy'

    parents = defaultdict(list)

    def handle(self, *args, **options):
        """ Create a exploded hierarchy for a given SAB"""
        sab = args[0]
        mrrels = MRREL.objects.filter(SAB=sab, REL="PAR")
        for mrrel in mrrels:  # CUI1_parent PAR child_CUI2
            # parents of cui2, add to an in-memory dictionary
            if mrrel.CUI1 and mrrel.CUI2:
                self.parents[mrrel.CUI2].append(mrrel.CUI1)
            else:
                print mrrel.CUI1, mrrel.CUI2

        self.explode_store_ISA_hierarchy(sab)

    def explode_store_ISA_hierarchy(self, sab):
        """ Explode and store the ISA hierarchy
            from the in-memory hierarchy dict, get all childrens a
            and store to DB
        """
        for child in self.parents.keys():
            #all_parents = self.get_all_parents(child, defaultdict(int))
            all_parents = self.get_all_parents(child, [child,])
            for parent in all_parents:
                isa = ISA(CHILD_CUI=child, PARENT_CUI=parent, SAB=sab)
                isa.save()

    def get_all_parents(self, child, traversed):
        """ Recursively get all parents for the child """

        if child in self.parents:
            myparents = []
            for parent in self.parents[child]:
                myparents.append(parent)
                if parent in traversed:
                    continue
                traversed.append(parent)
                myparents.extend(self.get_all_parents(parent,
                                                      copy.copy(traversed)))
            return myparents
        else:
            return []

