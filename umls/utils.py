from umls.models import MRCONSO

def get_cui(vocab, code_val):
    """ Get the UMLS concept unique identifier for a given code_val in vocabulary vocab
        Parameters:
            vocab: the source vocabulary
            code_val: the coded value
    """
    cuis    = MRCONSO.objects.filter(SAB=vocab, CODE=code_val)
    cui     = None
    if len(cuis)>0:
        cui = cuis[0].CUI
    
    return cui

def get_code(vocab, cui):
    """ Get the terminology code_val for a given UMLS concept unique identifier
        Parameters:
            cui: the unique concept identifier
    """
    codes    = MRCONSO.objects.filter(CUI=cui, SAB=vocab)
    code     = None
    if len(codes)>0:
        code = codes[0].CODE
    
    return code
