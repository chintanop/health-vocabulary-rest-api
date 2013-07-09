from umls.models import MRCONSO
from umls.models import MRREL

from umls.utils import get_cui
from umls.utils import get_code

class CodeResource:
    """ The Terminology Code resource """

    def _get(self, vocab, code_val):
        terms = MRCONSO.objects.filter(SAB=vocab, CODE=code_val)
        rterms = []
        for term in terms:
            rterms.append({
                'term':term.SAB,
                'code':term.CODE,
                'name':term.STR,
                'umls_cui':term.CUI,
                #'is_preferred':term.ISPERF
            })

        return rterms


class RelResource:
    """ The Terminology Relationship resource """

    def _get(self, vocab, code_val, rel_type):

        source_cui = get_cui(vocab, code_val)
   
        rels_list = []
        if source_cui:
            rels = MRREL.objects.filter(CUI1=source_cui, RELA=rel_type)
            for rel in rels:
                rels_list.append({
                    'umls_cui':rel.CUI2,
                    'code':get_code(rel.SAB, rel.CUI2),
                    'rel':rel.REL,
                    'rela':rel.RELA
                })

class MapResource:
    """ The Terminology Mapping resource """

    def _get(self, source_vocab, code_val, target_vocab):

        cui = get_cui(source_vocab, code_val)

        print cui
        terms = MRCONSO.objects.filter(CUI=cui, SAB=target_vocab)
        rterms = []
        for term in terms:
            rterms.append({
                'target_vocab':term.SAB,
                'code':term.CODE,
                'name':term.STR,
            })

        return rterms


        


