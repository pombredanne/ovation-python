import collections
from ovation import Maps, String, Object

def to_map(d):
    result = Maps.newHashMap().of_(String,Object)
    for (k,v) in d.iteritems():
        if not isinstance(k, basestring):
            k = unicode(k)
        if isinstance(v, collections.Mapping):
            result.put(k, to_map(v))
        else:
            result.put(k, v)
