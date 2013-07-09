from django.http import HttpResponse

from umls.resources import CodeResource
from umls.resources import RelResource
from umls.resources import MapResource

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
