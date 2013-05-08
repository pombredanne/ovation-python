"""
NumPy utilties for the Ovation Python API

This modules provides functions for converting DataElements to and from NumPy arrays
"""

import numpy as np
import quantities as pq

def to_ndarray(data_element):
    """Converts a numeric Ovation NumericData.Data to a Quantities (NumPy) array"""
    
    units = pq.Quantity([1], data_element.getUnits())
    shape = data_element.getShape()
    sampling_rates = data_element.getSamplingRates()
    sampling_rate_units = data_element.getSamplingRateUnits()
    dimension_labels = data_element.getDimensionLabels()
    
    arr = np.reshape(np.array(data_element.getData()) * units, shape)
    if len(sampling_rate_units) == 1:
        arr.sampling_rate = pq.Quantity(sampling_rates, sampling_rate_units[0]) 
    else:
        arr.sampling_rates = tuple(pq.Quantity(rate, unit) for (rate,unit) in zip(sampling_rates, sampling_rate_units))
    
    arr.labels = dimension_labels
    
    
def to_data_element(ndarr):
    """Converts a Quantities (NumPy) array to an Ovation DataElement"""
    
    pass