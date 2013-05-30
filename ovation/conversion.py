import collections

from ovation import Sets, Maps, Map, String, Object


def to_map(d):
    result = Maps.newHashMap().of_(String, Object)
    for (k, v) in d.iteritems():
        if not isinstance(k, basestring):
            k = unicode(k)
        if isinstance(v, collections.Mapping):
            result.put(k, to_map(v))
        else:
            result.put(k, v)

    return result


def to_dict(m):
    return {key: m.get(key) for key in m.keySet()}

def to_java_set(s):
    result = Sets.newHashSet()
    for item in s:
        result.add(item)

    return result
