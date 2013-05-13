import collections
from nose.tools import istest, assert_equals

from ovation import Maps, initVM


def to_map(d):
    result = Maps.newHashMap()
    for (k,v) in d.iteritems():
        if not isinstance(k, basestring):
            k = unicode(k)
        if isinstance(v, collections.Mapping):
            result.put(k, to_map(v))
        else:
            result.put(k, v)

  
def setup_module():
    initVM()

@istest
def __to_map_should_convert_flat_dict():
    d = {   'key1' : 'value1',
            'key2' : 2,
            3 : 'value3',
            4 : 5 }
            
            
    m = to_map(d)
    
    __check_dict(d, m)


def __check_dict(d, m):
    for (k,v) in d.iteritems():
        if not isinstance(k, basestring):
            k = unicode(k)
        
        if isinstance(v, collections.Mapping):
            yield __check_dict(v, m.get(k))
        else:
            yield assert_equals(v, m.get(k))
    
@istest
def __to_map_should_convert_nested_dict():
    d = {   'key1' : 'value1',
            'nested' : {'key2' : 2,
                        3 : 'value3',
                        4 : 5 }}
            
            
    m = to_map(d)
            
    __check_dict(d, m)   