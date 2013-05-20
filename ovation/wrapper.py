
from ovation.core import Taggable, PropertyAnnotatable, ResourceContainer

def taggable(entity):
    return Taggable.cast_(entity)


def property_annotatable(entity):
    return PropertyAnnotatable.cast_(entity)
    
def resource_container(entity):
    return ResourceContainer.cast_(entity)
    