"""Testing utilities for code that runs against an Ovation database"""

import ovation as ov

def local_stack_dsc():
    """Builds a local database stack and returns a DatabaseCoordinator and user credentials
    
    
    Returns
    -------
    (dsc, userIdentity, userPassword) : tuple
        Tuple of DataStoreCoordinator instance, userIdentity (string) and userPassword (string)
    """
    
    injector = LocalDatabaseStack.getInjector(OvationApiModule())
    localDatabaseStack = injector.getInstance(LocalDatabaseStack)
    
    port = LocalDatabaseStack.getNamedString(injector, OvationCouchModule.COUCH_PORT)
    host = LocalDatabaseStack.getNamedString(injector, OvationCouchModule.COUCH_HOST)
    localCouchUserName = LocalDatabaseStack.getNamedString(injector, OvationCouchModule.COUCH_PROCESS_OWNER)
    localCouchKeyStoreServiceName = LocalDatabaseStack.getNamedString(injector, OvationCouchModule.LOCAL_COUCH_KEY_STORE_SERVICE_NAME)
    
    keyStore = injector.getInstance(AccountKeyStore)
    
    userId = UUID.randomUUID();
    userIdentity = str(userId) + "@email.com"
    userPassword = "password"
    
    databaseName = userIdentity.replace("@", "-").replace(".", "-")
    
    localStack = localDatabaseStack.createLocalDatabaseStack(databaseName,
                userIdentity,
                userPassword,
                localCouchUserName,
                localCouchKeyStoreServiceName,
                host,
                port,
                userId,
                keyStore)
    
    dsc = localStack.getInjector(new OvationApiModule()).getInstance(DataStoreCoordinator)
    
    return (dsc, userIdentity, userPassword)