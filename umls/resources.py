from umls.models import MRCONSO
from umls.models import MRREL

from umls.utils import get_cui
from umls.utils import get_code
from django.db.models import Q
from django.db import connection


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

        return rels_list

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

class ConceptResource:
    """ The Terminology Code resource """

    def _get(self, cui):
        terms = MRCONSO.objects.filter(CUI=cui)
        rterms = []
        for term in terms:
            rterms.append({
                'concept':term.CUI,
                'terms':term.STR,
                'sabs':term.SAB,
            })

        return rterms

    def _get_term(self, str, sab):
        if sab == 'none':
            terms = MRCONSO.objects.filter(STR__contains=str)
        else:
            sablist = sab.split(',')
            terms = MRCONSO.objects.filter(STR__contains=str).filter(SAB__in=sablist)
        rterms = []

        for term in terms:
            rterms.append({
                'concept':term.CUI,
                'terms':term.STR,
                'sabs':term.SAB,
            })

        return rterms

    def _get_children(self, sab):
        cursor = connection.cursor()
        cursor.execute("SELECT rel.cui1 as CUI, rel.sab as SAB, conso.str as STR FROM `MRREL` rel, MRCONSO conso WHERE rel.cui2 = conso.cui AND rel.rel = 'CHD' AND rel.rela = 'ISA' AND STYPE1 = 'SCUI' AND rel.sab = %s GROUP BY rel.cui1, rel.sab, conso.str", [sab])
        terms = cursor.fetchall()
        x = cursor.description
        rterms = []

        for r in terms:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            rterms.append(d)

        return rterms

