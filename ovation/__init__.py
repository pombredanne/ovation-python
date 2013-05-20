import logging as pylogging

from ovation-api import initVM, JArray
import us.physion.ovation.api as api
import us.physion.ovation.domain as core
import us.physion.ovation.logging as logging
import us.physion.ovation.test.util as testing

from com.google.common.collect import *
from java.util import *
from java.lang import *

LOGGER = pylogging.getLogger('ovation')

logFileHandler = pylogging.FileHandler('ovation-python')
# formatter = pylogging.Formatter('%(asctime)s %(levelname)s %(message)s')
# hdlr.setFormatter(formatter)
LOGGER.addHandler(logFileHandler) 
LOGGER.setLevel(pylogging.DEBUG)

try:
    initVM()
except Exception, e:
    LOGGER.error("Unable to initialize Java VM", e)