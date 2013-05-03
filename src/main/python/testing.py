"""Testing utilities for code that runs against an Ovation database"""

from ovation import TestUtils, OvationApiModule
from contextlib import contextmanager

def __make_authenticated_dsc(local_stack):
    """Builds an authenticated DataStoreCoordinator for the given LocalStack
    
    Parameters
    ----------
    
    local_stack : LocalStack
    
    Returns
    -------
    Authenticated DataStoreCoordinator
    """
    
    dsc = local_stack.getDataStoreCoordinator()
    dsc.authenticateUser(userIdentity, userPassword, False).get()
    
    return dsc


def __make_local_stack():
    """Builds a local database stack"""
    
    testUtils = TestUtils(OvationApiModule())
    stackBuilder = testUtils.getLocalDatabaseStackBuilder()
    
    userId = UUID.randomUUID();
    userIdentity = str(userId) + "@email.com"
    userPassword = "password"
    
    databaseName = userIdentity.replace("@", "-").replace(".", "-")
    
    localStack = stackBuilder.build(databaseName, userIdentity, userPassword)
    
    return localStack

    
@contextmanager
def local_stack():
    """Context manager wrapping a local database stack. This stack uses a local, transient cloud storage endpoint and
    a local CouchDB database in place of a normal ovation.io account database.
    
    This manager yields an authenticated DataStoreCoordinator for the local stack.
    
    Upon cleanup, the manager deletes the local database(s) associated with this stack
    
    Usage
    -----
    
    :
        with(local_stack()) as dsc:
            context = dsc.getContext()
            # ...
    
    """
    
    stack = None
    try:
        stack = __make_local_stack()
        yield __make_authenticated_dsc(stack)
    finally:
        if stack is not None:
            stack.cleanUp()