
from ovation import *

def tag(entity):
    return Taggable.cast_(entity)


def prop(entity):
    return PropertyAnnotatable.cast_(entity)
    
def rsrc(entity):
    return ResourceContainer.cast_(entity)