from .load_model import load_checkpoint
from .save_model import save_checkpoint


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def combine_model(prefix1, epoch1, prefix2, epoch2, prefix_out, epoch_out):
    args1, auxs1 = load_checkpoint(prefix1, epoch1)
    args2, auxs2 = load_checkpoint(prefix2, epoch2)
    #arg_names = args1.keys() + args2.keys()
    #aux_names = auxs1.keys() + auxs2.keys()
    
    arg_names = list(args1.keys()) + list(args2.keys())
    aux_names = list(auxs1.keys()) + list(auxs2.keys())
    
    args = dict()
    for arg in arg_names:
        if arg in args1:
            args[arg] = args1[arg]
        else:
            args[arg] = args2[arg]
    auxs = dict()
    for aux in aux_names:
        if aux in auxs1:
            auxs[aux] = auxs1[aux]
        else:
            auxs[aux] = auxs2[aux]
    save_checkpoint(prefix_out, epoch_out, args, auxs)
