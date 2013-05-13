import collections
from ovation import Maps, Map, String, Object

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