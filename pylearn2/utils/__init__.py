import theano
import numpy

def make_name(variable, anon = "anonymous_variable"):
    """
    If variable has a name, returns that name.
    Otherwise, returns anon
    """

    if hasattr(variable,'name') and variable.name is not None:
        return variable.name

    return anon


def sharedX(value, name=None, borrow=False):
    """Transform value into a shared variable of type floatX"""
    return theano.shared(theano._asarray(value, dtype=theano.config.floatX),
                         name=name,
                         borrow=borrow)

def as_floatX(variable):
    """Casts a given variable into dtype config.floatX
        numpy ndarrays will remain numpy ndarrays
        all other types will be treated as theano tensors"""

    if isinstance(variable, numpy.ndarray):
        return numpy.cast[theano.config.floatX](variable)

    return theano.tensor.cast(variable, theano.config.floatX)

def subdict(d, keys):
    """ Create a subdictionary of d with the keys in keys """
    result = {}
    for key in keys:
        if key in d: result[key] = d[key]
    return result

"""
doesn't make sense to auto-import utlc code in a generic
pylearn2 module, especially
now that no one will probably use the utlc stuff ever again
from pylearn2.utils.utlc import (
        subdict,
        safe_update,
        getboth,
        load_data,
        save_submission,
        create_submission,
        compute_alc,
        lookup_alc,
        )"""

"""from pylearn2.utils.datasets import (
        do_3d_scatter,
        save_plot,
        filter_labels,
        filter_nonzero,
        nonzero_features,
        BatchIterator,
        blend,
        minibatch_map,
        )""" # this is making cluster jobs crash, and seems like kind of a lot of stuff to import by default anyway
