from django.http import HttpResponse

from umls.resources import CodeResource
from umls.resources import RelResource
from umls.resources import MapResource
from umls.resources import ConceptResource
from umls.resources import ConceptListResource

import json


def code_resource_view(request, vocab, code_val):
    """Get the full display name of a code for a given vocabz

    GET /code/<vocab>/<code_val>

    Parameters:

    vocab: The vocabularly abbreviation or short name, e.g. SNOMEDCT, LOINC.
    The full list of vocabulary abbreviations is available here
    code_val: The value of code to be looked up, e.g. 111-ABC

    """

    rterms = CodeResource()._get(vocab, code_val)

    # Handle AJAX Requests
    response = json.dumps(rterms)
    if 'callback' in request.GET:
        response = request.GET["callback"] + "(" + response + ")"

    return HttpResponse(response)


def rel_resource_view(request, vocab, code_val, rel_type):
    """Get all target codes related to a given vocab/code pair by
        relationship rel_type

    GET /rel/<vocab>/<code_val>/<rel_type>

    Parameters:

        vocab: The vocabulary abbreviation or short name, e.g. SNOMEDCT, LOINC.
        The full list of vocabulary abbreviations is available here
        code_val: The value of code to be looked up, e.g. 111-ABC
        rel_type: The relationship to be looked up, e.g. is_diagnosed_by,
        causative_agent_of. The full list of rel_type abbreviations
        are available here

    """

    # Return the list of relationship/codes
    rels_list = RelResource()._get(vocab, code_val, rel_type)

    response = json.dumps(rels_list)

    # Handle AJAX Requests
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def map_resource_view(request, source_vocab, code_val, target_vocab):
    """Get a "semantically equivalent" code in target vocabulary for a given code_val in source vocabulary

       GET /map/<source_vocab>/<code_val>/<target_vocab>

       Parameters:
        source_vocab, target_vocab: The vocabulary abbreviation or short name, e.g. SNOMEDCT, LOINC. The full list of vocabulary abbreviations is available here
        code_val: The value of code to be looked up, e.g. 111-ABC

    """

    # Get the mappings
    rterms = MapResource()._get(source_vocab, code_val, target_vocab)

    response = json.dumps(rterms)

    # Handle AJAX Requests
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def concept_resource_view(request, cui):
    """Get the full display name of a code for a given concept

    GET /concept/<cui>

    Parameters:

    cui: The Concept code.

    """
    print "GET /concept/<cui>"

    rterms = ConceptResource()._get(cui)

    # Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    print response
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def concept_term_resource_view(request):
    """Get the full display name of a code for a given concept

    GET /concepts?term=term&sabs=sabs

    Parameters:

    str: Term
    sab: Source Vocab

    """
    term = None
    sab = None
    partial = False
    tty = None
    sty = None

    if 'term' in request.GET:
        term = request.GET['term']
    if 'sabs' in request.GET:
        sab = request.GET['sabs']
    if 'partial' in request.GET:
        pint = request.GET['partial']
        if pint == "1":
            partial = True
    if 'tty' in request.GET:
        tty = request.GET['tty']
    if 'sty' in request.GET:
        sty = request.GET['sty']

    rterms = ConceptListResource()._get(term, sab, tty, partial, sty)

    # Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def concept_child_resource_view(request, cui):
    """Get the full display name of a code for a given concept-children

    GET /concepts/<cui>/children

    Parameters:

    cui: cui
    sab: Source Vocab

    """
    sab = request.GET.get('sab', None)

    explode = False
    eint = request.GET.get('explode', None)
    if eint and eint == "1":
        explode = True

    rterms = ConceptListResource()._get_children(cui, sab, explode)

    # Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def concept_par_resource_view(request, cui):
    """Get the full display name of a code for a given concept-parent

    GET /concepts/<cui>/parent

    Parameters:

    cui: cui
    sab: Source Vocab

    """
    sab = request.GET.get('sab')
    explode = False
    eint = request.GET.get('explode', None)
    if eint and eint == "1":
        explode = True

    # if sab:
    #    print request.GET['chd_sab']
    rterms = ConceptListResource()._get_parent(cui, sab, explode)

    # Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def concept_synonyms_resource_view(request, cui):
    """Get the full display name of a code for a given concept-synonyms

    GET /concepts/<cui>/synonyms

    Parameters:

    cui: cui
    sab: Source Vocab

    """
    print 'synonyms'
    sab = request.GET.get('sab')
    print sab
    rterms = ConceptResource()._get_synonyms(cui, sab)

    # Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def code_res_view(request):
    """Get the full display name of a code for a given code

    GET /codes

    Parameters:

    cui: code
    sab: Source Vocab

    """
    code = request.GET.get('code')
    sab = request.GET.get('sab')
    rterms = CodeResource()._get_code(code, sab)

    # Handle AJAX Requests

    response = json.dumps(rterms, sort_keys=True)
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def code_det_view(request, code, sab):
    """Get the full display name of a code for a given code

    GET /codes/<cui>/sab/<sab>

    Parameters:

    cui: code
    sab: Source Vocab

    """

    rterms = CodeResource()._get_code_det(code, sab)

    # Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def concepts_bulk_resource_view(request):
    """Get the list of concepts for a given list of terms
    GET /concepts_bulk?terms=term1,term2
    Parameters:
    terms: List of Terms
    sab: Source Vocab
    delimiter: delimiter between terms, default = ','
    """
    terms = None
    sab = None
    partial = None
    delimiter = ','

    if 'delimiter' in request.GET:
        delimiter = request.GET['delimiter']
    if 'terms' in request.GET:
        terms = request.GET['terms']
        terms = set(terms.split(delimiter))
    if 'sab' in request.GET:
        sab = request.GET['sab']
    if 'partial' in request.GET:
        pint = request.GET['partial']
        if pint == "1":
            partial = True
    
    rterms = []
    for term in terms:
            rterms.extend(ConceptListResource()._get(term,sab,partial))

    # Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def concepts_bulk_par_resource_view(request, cui_list):
    """Get the list of parents for a given concept-parent list
    GET /concepts_bulk/<cui1>,<cui2>,<cui3>,..,<cuiN>/parent
    Parameters:
    cui_list: list of cuis
    sab: Source Vocab
    """
    sab = request.GET.get('sab')
    explode = False
    eint = request.GET.get('explode', None)
    if eint and eint == "1":
        explode = True
    cui_list = cui_list.split(',')
    cui_list = set(cui_list)
    
    rterms = {}
    for cui in cui_list:
        value = ConceptListResource()._get_parent(cui,sab,explode)
        # Removing duplicates
        rterms[cui] = { d['cui']:d for d in value }.values()
        
    # Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if 'callback' in request.GET:
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)