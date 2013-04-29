"""
Connection utilities for the Ovation Python API
"""

from ovation import Ovation

def new_data_store_coodinator(email, password=None):
    """Creates a new authenticated DataStoreCoordinator.
    
    Arguments
    ---------
    email : string
        Ovation.io account email
    
    password : string [optional]
        Ovation.io account passowrd. If ommited, the password will be prompted at the command prompt
    
    Return
    ------
    A new authenticated DataStoreCoordinator
    
    """
    
    if password is None:
        pw = getpass.getpass("Ovation password: ")
    else:
        pw = password
    
    return Ovation.newDataStoreCoordinator(email, pw)
