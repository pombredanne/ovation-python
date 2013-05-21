import collections

import numpy as np
import quantities as pq

from scipy.io import netcdf

from ovation import JArray_double, JArray_int, JArray_object, Maps, Map, String, Object
from ovation.core import NumericData, NumericMeasurementUtils

class NumericMeasurementException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

def as_data_frame(measurement):
    if not NumericMeasurementUtils.isNumericMeasurement(measurement):
        raise NumericMeasurementException("")

    file = measurement.getData().get()
    ncf = netcdf.netcdf_file(file.getAbsolutePath(), mode='r')
    try:
        pass
    finally:
        ncf.close()




def as_array(numeric_data):
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
        arr.sampling_rates = tuple(pq.Quantity(rate, unit) for (rate, unit) in zip(sampling_rates, sampling_rate_units))

    arr.labels = dimension_labels
    arr.name = numeric_data.getName()

    return arr


def as_numeric_data(arr):
    """Converts a Quantities (NumPy) array to an Ovation NumericData, copying the array data.
    
    Parameters
    ----------
    arr : pq.Quantity
        Quantity (NumPy) array with `labels` and `sampling_rate` properties
        
    Returns
    -------
    numeric_data : ovation.NumericData
         `ovation.NumericData` instance copying the provided quantity
    """

    dtype_to_java = {
        np.float32: JArray_double,
        np.float64: JArray_double,
        np.int32: JArray_int
    }

    result = NumericData()
    if arr.ndim == 1:
        data = dtype_to_java[arr.dtype.type](np.asarray(arr).tolist())
        result.addData(arr.name,
                       data,
                       arr.dimensionality.unicode,
                       float(arr.sampling_rate),
                       arr.sampling_rate.dimensionality.unicode)
    elif arr.ndim == 2:
        data = JArray_object([dtype_to_java[arr.dtype.type](r) for r in np.asarray(arr).tolist()])
        try:
            dimension_labels = arr.labels
        except AttributeError:
            dimension_labels = ["", ""]

        result.addData(arr.name,
                       data,
                       dimension_labels,
                       arr.dimensionality.unicode,
                       [float(arr.sampling_rate) for i in xrange(arr.ndim)],
                       [arr.sampling_rate.dimensionality.unicode for i in xrange(arr.ndim)]
        )
    else:
        raise NotImplementedError("NumericData does not support rank-" + str(arr.ndim) + " arrays")

    return result


def create_variable(ncf, data, dtype, dimensions, **attributes):
    shape = tuple([ncf.dimensions[dim] for dim in dimensions])
    shape_ = tuple([dim or 0 for dim in shape])  # replace None with 0 for numpy

    typecode, size = dtype.char, dtype.itemsize
    if (typecode, size) not in netcdf.REVERSE:
        raise ValueError("NetCDF 3 does not support type {}".format(dtype))

    data_array = np.empty(shape_, dtype=dtype.newbyteorder("B")) #convert to big endian always for NetCDF 3
    ncf.variables[name] = netcdf_variable(data_array, typecode, size, shape, dimensions, attributes=attributes)
    return ncf.variables[name]


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
