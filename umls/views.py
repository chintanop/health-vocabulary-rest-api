from django.http import HttpResponse

from umls.resources import CodeResource
from umls.resources import RelResource
from umls.resources import MapResource
from umls.resources import ConceptResource

import json

def code_resource_view(request, vocab, code_val):
    """Get the full display name of a code for a given vocabz

    GET /code/<vocab>/<code_val>

    Parameters:

    vocab: The vocabularly abbreviation or short name, e.g. SNOMEDCT, LOINC. The full list of vocabulary abbreviations is available here
    code_val: The value of code to be looked up, e.g. 111-ABC

    """

    rterms =  CodeResource()._get(vocab, code_val)
   
    #Handle AJAX Requests
    response = json.dumps(rterms)
    if request.GET.has_key("callback"):
          response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)

def rel_resource_view(request, vocab, code_val, rel_type):
    """Get all target codes related to a given vocab/code pair by relationship rel_type

    GET /rel/<vocab>/<code_val>/<rel_type>
    
    Parameters:

        vocab: The vocabulary abbreviation or short name, e.g. SNOMEDCT, LOINC. The full list of vocabulary abbreviations is available here
        code_val: The value of code to be looked up, e.g. 111-ABC
        rel_type: The relationship to be looked up, e.g. is_diagnosed_by, causative_agent_of. The full list of rel_type abbreviations are available here
    
    """

    #Return the list of relationship/codes
    rels_list = RelResource()._get(vocab, code_val, rel_type)

    response = json.dumps(rels_list)
    
    #Handle AJAX Requests
    if request.GET.has_key("callback"):
          response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)

def map_resource_view(request, source_vocab, code_val, target_vocab):
    """Get a "semantically equivalent" code in target vocabulary for a given code_val in source vocabulary
       
       GET /map/<source_vocab>/<code_val>/<target_vocab>

       Parameters:
        source_vocab, target_vocab: The vocabulary abbreviation or short name, e.g. SNOMEDCT, LOINC. The full list of vocabulary abbreviations is available here
        code_val: The value of code to be looked up, e.g. 111-ABC

    """

    #Get the mappings
    rterms      = MapResource()._get(source_vocab, code_val, target_vocab)
       
    response    = json.dumps(rterms)

    #Handle AJAX Requests
    if request.GET.has_key("callback"):
          response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)

def concept_resource_view(request, cui):
    """Get the full display name of a code for a given concept

    GET /concept/<cui>

    Parameters:

    cui: The Concept code.

    """
    print "GET /concept/<cui>"

    rterms =  ConceptResource()._get(cui)

    #Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    print response
    if request.GET.has_key("callback"):
        response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)

def concept_term_resource_view(request):
    """Get the full display name of a code for a given concept

    GET /concepts?term=term&sabs=sabs

    Parameters:

    str: Term
    sab: Source Vocab

    """
    print 'term'
    term = None
    sab = None
    if request.GET['term']:
        term = request.GET['term']
        print request.GET['term']
    if request.GET['sabs']:
        sab = request.GET['sabs']
        print request.GET['sabs']
    rterms =  ConceptResource()._get_term(term, sab)


    #Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if request.GET.has_key("callback"):
          response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)

def concept_child_resource_view(request, cui):
    """Get the full display name of a code for a given concept-children

    GET /concepts/<cui>/children

    Parameters:

    cui: cui
    sab: Source Vocab

    """
    print 'child11111'
    sab = request.GET.get('sab')
    print sab
    #if sab:
    #    print request.GET['chd_sab']
    rterms =  ConceptResource()._get_children(cui, sab)


    #Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if request.GET.has_key("callback"):
          response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)

def concept_par_resource_view(request, cui):
    """Get the full display name of a code for a given concept-parent

    GET /concepts/<cui>/parent

    Parameters:

    cui: cui
    sab: Source Vocab

    """
    print 'par11111'
    sab = request.GET.get('sab')
    print sab
    #if sab:
    #    print request.GET['chd_sab']
    rterms =  ConceptResource()._get_parent(cui, sab)


    #Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if request.GET.has_key("callback"):
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
    rterms =  ConceptResource()._get_synonyms(cui, sab)


    #Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if request.GET.has_key("callback"):
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
    rterms =  CodeResource()._get_code(code, sab)

    #Handle AJAX Requests

    response = json.dumps(rterms, sort_keys=True)
    if request.GET.has_key("callback"):
          response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)


def code_det_view(request, code, sab):
    """Get the full display name of a code for a given code

    GET /codes/<cui>/sab/<sab>

    Parameters:

    cui: code
    sab: Source Vocab

    """

    rterms =  CodeResource()._get_code_det(code, sab)

    #Handle AJAX Requests
    response = json.dumps(rterms, sort_keys=True)
    if request.GET.has_key("callback"):
          response = request.GET["callback"]+"("+response+")"

    return HttpResponse(response)
