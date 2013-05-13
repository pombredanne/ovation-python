import collections
from nose.tools import istest, assert_equals

from maps import to_map
from ovation import initVM


def setup_module():
    initVM()

@istest
def to_map_should_convert_flat_dict():
    d = {   'key1' : 'value1',
            'key2' : 2,
            3 : 'value3',
            4 : 5 }
            
            
    m = to_map(d)
    
    check_dict(d, m)


def check_dict(d, m):
    for (k,v) in d.iteritems():
        if not isinstance(k, basestring):
            k = unicode(k)
        
        if isinstance(v, collections.Mapping):
            yield check_dict(v, m.get(k))
        else:
            yield assert_equals(v, m.get(k))
    
@istest
def to_map_should_convert_nested_dict():
    d = {   'key1' : 'value1',
            'nested' : {'key2' : 2,
                        3 : 'value3',
                        4 : 5 }}
            
            
    m = to_map(d)
            
    check_dict(d, m)   