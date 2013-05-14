"""
NumPy utilties for the Ovation Python API

This modules provides functions for converting DataElements to and from NumPy arrays
"""

import numpy as np
import quantities as pq

from ovation import *

def asarray(numeric_data):
    """Converts a numeric Ovation NumericData.Data to a Quantities (NumPy) array
    
    Parameters
    ----------
    numeric_data : ovation.NumericData.Data
        `NumericData` instance to convert to a `quantities` array
        
    Returns
    -------
    array : quantities.Quantity 
        Quantity array with additional `labels`, `sampling_rate` properties
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
    """Converts a Quantities (NumPy) array to an Ovation NumericData, copying the array data.
    
    Parameters
    ----------
    quantity : pq.Quantity
        Quantity (NumPy) array with `labels` and `sampling_rate` properties
        
    Returns
    -------
    numeric_data : ovation.NumericData
         `ovation.NumericData` instance copying the provided quantity
    """
    
    dtype_to_java = {
        np.float32 :    JArray_double,
        np.float64 :    JArray_double,
        np.int32 :      JArray_int
    }
    
    result = NumericData()
    if a.ndim == 1:
        data = dtype_to_java[a.dtype.type](np.asarray(a).tolist())
        result.addData(quantity.name, 
                        data,
                        a.dimensionality.unicode,
                        float(a.sampling_rate),
                        a.sampling_rate.dimensionality.unicode)
    elif a.ndim == 2:
        data = JArray_object([dtype_to_java[a.dtype.type](r) for r in np.asarray(a).tolist()])
        try:
            dimension_labels = quantity.labels
        except AttributeError:
            dimension_lablels = ["", ""]
        
        result.addData(quantity.name,
                        data,
                        dimension_labels,
                        a.dimensionality.unicode,
                        float(a.sampling_rate),
                        [a.sampling_rate.dimensionality.unicode for i in xrange(a.ndim)]
                        )
    else:
        raise NotImplementedError("NumericData does not support rank-" + str(a.ndim) +" arrays")
        
    return result
    
    
    
