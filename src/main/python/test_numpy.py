import numpy as np
import quantities as pq

from nose.tools import istest, assert_equals

from numpy import asarray, as_numeric_data

@istest
def should_round_trip_1D_floating_point():
    
    expected = np.random.randn(10) * pq.s
    expected.labels = 'volts'
    actual = asarray(as_numeric_data(expected))
    
    assert_equals(expected, actual)
