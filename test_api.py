import pytest

from keel_API2 import (
    loginRequest,
    checkOrgname,
    domainRequest,
    logoRequest,
    countryId,
    addOrganization,
    getAppkeyRequest,
    listdb,
    desRequest,
    addDes, 
    listRoles,
    addRole, 
    emailTofSES,
    createPackage,
    getPackage,
    getPakagebyID,
    createFeatureP,
    getFeaturesforP,
    getFeaturesforPbyID
)

@pytest.fixture()
def login():
    global head
    head=loginRequest()
    yield
    
def test_1(login):
    checkOrgname(head)
    domainRequest(head)
    
def test_2(login):
    logoRequest(head)
    appkey=addOrganization(head)
    getAppkeyRequest(head,appkey)
    listdb(head)
    
def test_3(login):
    countryId(head)
    emailTofSES(head)
    
def test_4(login):
    desRequest(head)
    addDes(head)
    
def test_5(login):
    addRole(head)
    listRoles(head)
    
def test_6(login):
    iD=createPackage(head)
    getPackage(head ,iD)
    getPakagebyID(head,iD)
    
def test_7(login):
    ID=createFeatureP(head)
    getFeaturesforP(head, ID)
    getFeaturesforPbyID(head, ID)

    
