import numpy as np
import quantities as pq

from nose.tools import istest, assert_equals

from conversion import as_array, as_numeric_data

import ovation
from ovation.core import *

def _round_trip():
    expected = np.random.randn(10) * pq.s
    expected.name = u'name'
    expected.sampling_rate = 1 * pq.Hz
    actual = as_array(as_numeric_data(expected).getData())

    return (expected,actual)

@istest
def should_round_trip_1D_floating_point():
    (expected,actual) = _round_trip()
    assert np.all(expected == actual)

@istest
def should_round_trip_labels():
    (expected,actual) = _round_trip()
    assert_equals(expected.name, actual.labels[0])

@istest
def should_round_trip_sampling_rate():
    (expected,actual) = _round_trip()
    assert_equals(expected.sampling_rate, actual.sampling_rate)

@istest
def should_round_trip_units():
    (expected,actual) = _round_trip()
    assert_equals(expected.units, actual.units)

@istest
def should_round_trip_name():
    (expected,actual) = _round_trip()
    assert_equals(expected.name, actual.name)

@istest
def should_round_trip_2D_floating_point():
    expected = np.random.randn(10,10) * pq.s
    expected.labels = [u'volts', u'other']
    expected.name = u'name'
    expected.sampling_rate = 1 * pq.Hz
    actual = as_array(as_numeric_data(expected).getData())

    assert np.all(np.all(expected == actual))
