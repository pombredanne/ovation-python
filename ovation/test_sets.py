import collections
from nose.tools import istest, assert_true

from ovation import Map, Maps, Integer
from conversion import to_java_set

@istest
def to_java_set_should_convert_set():
    s = set([1, 2, 'abc'])
    j = to_java_set(s)
    for item in s:
        assert_true(j.contains(item))
