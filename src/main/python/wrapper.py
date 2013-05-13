
from ovation import *

def tag(entity):
    return Taggable.cast_(entity)


def prop(entity):
    return PropertyAnnotatable.cast_(entity)
    
def rsrc(entity):
    return ResourceContainer.cast_(entity)
    
def to_map(d):
    result = Maps.newHashMap().of_(String,Object)
    for (k,v) in d.iteritems():
        if not isinstance(k, basestring):
            k = unicode(k)
        if isinstance(v, collections.Mapping):
            result.put(k, to_map(v))
        else:
            result.put(k, v)
    
    return result

def to_dict(m):
    return Map.cast_(m)