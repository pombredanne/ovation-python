"""
NumPy utilties for the Ovation Python API

This modules provides functions for converting DataElements to and from NumPy arrays
"""

import numpy as np
import quantities as pq

def asarray(numeric_data):
    """Converts a numeric Ovation NumericData.Data to a Quantities (NumPy) array
    
    Parameters
    ----------
    numeric_data : ovation.NumericData
        `NumericData` instance to convert to a `quantities` array
        
    Return
    ------
    `quantities.Quantity` with additional `labels`, `sampling_rate` properties
    """
    
    units = pq.Quantity([1], numeric_data.getUnits())
    shape = numeric_data.getShape()
    sampling_rates = numeric_data.getSamplingRates()
    sampling_rate_units = numeric_data.getSamplingRateUnits()
    dimension_labels = numeric_data.getDimensionLabels()
    
    arr = np.reshape(np.array(JArray_double.cast_(numeric_data.getData())) * units, shape)
    if len(sampling_rate_units) == 1:
        arr.sampling_rate = pq.Quantity(sampling_rates, sampling_rate_units[0]) 
    else:
        arr.sampling_rates = tuple(pq.Quantity(rate, unit) for (rate,unit) in zip(sampling_rates, sampling_rate_units))
    
    arr.labels = dimension_labels


def as_numeric_data(quantity):
    """Converts a Quantities (NumPy) array to an Ovation NumericData
    
    Parameters
    ----------
    quantity : pq.Quantity
        Quantity (NumPy) array with `labels` and `sampling_rate` properties
        
    Return
    ------
    `ovation.NumericData` instance copying the provided quantity
    """
    
    pass
    
