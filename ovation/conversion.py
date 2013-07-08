import collections
import numbers

from ovation import Maps, Sets, autoclass

class Iterator(object):
    def __init__(self, jiterator):
        self.java_iterator = jiterator
    
    def __iter__(self):
        return self
    
    def next(self):
        if(self.java_iterator.hasNext()):
            return self.java_iterator.next()
        
        raise StopIteration()
        
class IterableWrapper(object):
    def __init__(self, jiterable):
        self.java_iterable = jiterable
    
    def __iter__(self):
        return Iterator(self.java_iterable.iterator())
            
def iterable(java_iterable):
            
    return IterableWrapper(java_iterable)
    
def to_map(d):
    result = Maps.newHashMap()
    for (k, v) in d.iteritems():
        if not isinstance(k, basestring):
            k = unicode(k)
        if isinstance(v, collections.Mapping):
            nested_value = to_map(v)
            result.put(k, nested_value)
        else:
            result.put(k, _box_numbers(v))

    return result


def to_dict(m):
    return {key: m.get(key) for key in iterable(m.keySet())}


def _box_numbers(item):
    if isinstance(item, numbers.Number):
        if isinstance(item, numbers.Integral):
            value = autoclass("java.lang.Integer")(item)
        else:
            value = autoclass("java.lang.Double")(item)
    else:
        value = item
    return value


def to_java_set(s):
    result = Sets.newHashSet()
    for item in s:
        result.add(_box_numbers(item))

    return result


