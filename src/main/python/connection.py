"""
Connection utilities for the Ovation Python API
"""

from getpass import getpass

from ovation import Ovation, Logging
# from us.physion.ovation.api import Ovation

def connect(email, password=None, logging=True):
    """Creates a new authenticated DataStoreCoordinator. d
    
    Arguments
    ---------
    email : string
        Ovation.io account email
    
    password : string [optional]
        Ovation.io account passowrd. If ommited, the password will be prompted at the command prompt
        
    logging : boolean [optional]
        If true, configures Ovation logging. Logs will be placed in the default application
        support directory, `~/Library/Application Support/us.physion.ovation/logs` on OS X, etc.
    
    Return
    ------
    A new authenticated DataStoreCoordinator
    
    """
    
    if logging:
        Logging.configureRootLoggerRollingAppender()
    
    if password is None:
        pw = getpass("Ovation password: ")
    else:
        pw = password
    
    return Ovation.connect(email, pw)
