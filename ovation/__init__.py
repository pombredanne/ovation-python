import logging as pylogging

from ovation_api import initVM, JArray
import us.physion.ovation.api as api
import us.physion.ovation.domain as core
import us.physion.ovation.logging as logging
import us.physion.ovation.test.util as testing

from com.google.common.collect import *
from java.util import *
from java.lang import *

try:
    initVM()
except Exception, e:
    LOGGER = pylogging.getLogger('ovation')

    logFileHandler = pylogging.FileHandler('ovation-python.log')
    LOGGER.addHandler(logFileHandler) 
    LOGGER.setLevel(pylogging.DEBUG)
    
    LOGGER.error("Unable to initialize Java VM", e)