import requests
import json

from payloads.datas import randomdata


base_url=randomdata.base_url
b1=randomdata.data1
b2=randomdata.data2
b6=randomdata.data6
b7=randomdata.data7
b8=randomdata.data8
file =randomdata.files
json_data1=randomdata.json_data
json_data=json.load(json_data1)
b5=randomdata.data5


def loginRequest():
    randomdata.generate_data()
    url=base_url+ "/login" 
    res=requests.post(url, data=b1)
    print(res)
    assert res.status_code==200, "Login Failed "
    resp= res.json()
    t1= resp['user']['firstName']
    t2= resp['user']['lastName'] 
    assert t1=="super" and t2=="admin", "Login failed or login error"
    # print(json.dumps(resp, indent=4))
    token1 =resp['access_token']
    # print(token1)
    head1 = {"Authorization": f"Bearer {token1}"}
    return head1
    
def checkOrgname(head):
    organizationName =json_data['organizationName']
    url=base_url+ f"/checkorgname?organizationName={organizationName}"
    res=requests.get(url, headers=head)
    print(res)
    resp=res.json()
    # print(json.dumps(resp, indent=4))
    assert resp['data']['result']['isAvailable']== True , "The organization name is already exists"
      
def domainRequest(head1):
    domaimName =json_data['subDomain']
    url=base_url+ f"/checkdomain?domain={domaimName}"
    res=requests.get(url, headers=head1)
    print(res)
    resp=res.json()
    # print(json.dumps(resp, indent=4))
    assert resp['data']['result']['isAvailable']== True , "The subdomain name is already exists"
     
def countryId(head):
    url=base_url+ "/countries" 
    res=requests.get(url, headers=head)
    # print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    assert res.status_code==200 ,"country list display failure"  # verybig list 

def logoRequest(head):
    url =base_url+ "/org/logoupload"
    res = requests.post(url, data=b6,files=file, headers=head)
    resp=res.json() 
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    assert resp['message']=='File uploaded successfully.', "Logo upload failiure"
    logopath=resp['data']['result']['logoPath']
    randomdata.modifyJsonfile(logopath)
    # print(logopath)
     
def addOrganization(head):
    url =base_url+ "/addorganization"
    res = requests.post(url, json=json_data, headers=head)
    # print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    assert resp['data']['result']['organization']['organizationName']==json_data['organizationName'] and resp['data']['result']['organization']['subDomain']==json_data['subDomain'], "Org name entered wrongly "
    resp= res.json()
    appkey=resp['data']['result']['organization']['appKey']
    return appkey
 
def getAppkeyRequest(head, appkey):
    url=base_url+"/org/" +appkey
    res=requests.get(url, headers=head)
    print(res)
    resp= res.json()
    assert resp['data']['organizationName']==json_data['organizationName'] and resp['data']['subDomain']==json_data['subDomain'], "Org name entered wrongly "
    # print(json.dumps(resp, indent=4))
    assert res.status_code==200, "Get Request Failed "

def listdb(head):
    url=base_url+ "/allorganization?page=1&limit=10"
    res=requests.get(url, headers=head)
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    assert resp['message']=="Organizations and Users fetched successfully.", "Get Request Failed "

def desRequest(head):#long response 
    url=base_url+"/designation"
    res=requests.get(url, headers=head)
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    assert res.status_code==200, "Designation display request failed "
    # print(res.content)

def addDes(head):
    url=base_url+"/designation"
    b4=randomdata.data4
    res=requests.post(url, json=b4, headers=head)
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    assert resp['data']['result'][0]['designation']==b4['designation'][0], "Adding designation failed" 
 
def listRoles(head):
    url=base_url+"/roles"
    res=requests.get(url, headers=head)
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    assert res.status_code==200, "Roles display request failed"
    
def addRole(head):#response500 postman
    url=base_url+"/roles"
    res=requests.post(url, json=b5, headers=head)
    print(res) 
    # print(res.content)
    # resp= res.json()
    # print(json.dumps(resp, indent=4))
    # assert res.status_code==201, "Adding roles failed"

def alltemplates(head):# 404
    url = base_url+"email-services/allemailtemplate"
    res=requests.get(url,headers=head)
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    
def emailTofSES(head): #assertion doubt 
    url=base_url+"/email-services/email-templates"
    res=requests.get(url,data="1", headers=head)
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    assert res.status_code==200 , "Email template did't retrived "
    
def emailTofID(head):# Response 404
    url=base_url+"/email-services/" 
    res=requests.get(url, headers=head)
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    # assert res.status_code==200 , "Email template did't retrived "

def createPackage(head): 
    url=base_url+"/createpackage"
    res= requests.post(url, data=b7, headers=head)
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    iD=resp['data']['result']['id']
    assert resp['data']['result']['packageName']==b7['packageName'] , "creation of package failed"
    return iD
      
def getPackage(head ,iD):
    url=base_url+"/getpackages"
    res= requests.get(url, headers=head)
    print(res)
    resp= res.json()
    packagename = next((entry['packageName'] for entry in resp['data']['result'] if entry['id'] == iD), None)
    assert packagename==b7['packageName'] , "creation of package failed"

def getPakagebyID(head, iD):
    url=base_url+f"/getpackages?packageId={iD}"
    res= requests.get(url, headers=head)
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    assert resp['data']['result']['packageName']==b7['packageName'] , "unable to get file with ID"

def createFeatureP(head):# no validATION 
    url=base_url+"/createpackagefeature"
    res= requests.post(url,data=b8, headers=head)
    print(res)
    resp= res.json()
    ID=resp['data']['result']['id']
    # print(json.dumps(resp, indent=4))
    assert resp['data']['result']['featureName']==b8["featureName"] , "unable to create feature"  
    return ID
 
def getFeaturesforP(head,ID):
    url=base_url+"/getpackagefeatures"
    res= requests.get(url, headers=head)
    print(res)
    resp= res.json()
    featureName= next((entry['featureName'] for entry in resp['data']['result'] if entry['id'] == ID), None)
    # print(json.dumps(resp, indent=4))
    assert featureName==b8["featureName"] , "unable to get feature"    
    
def getFeaturesforPbyID(head, ID):
    url=base_url+f"/getpackagefeatures?packageId={ID}"
    res= requests.get(url, headers=head)
    print(res)
    resp= res.json()
    # print(json.dumps(resp, indent=4))
    assert resp['message']=="Package features fetched successfully." , "unable to get feature with ID" 


head=loginRequest() #.......................200
# checkOrgname(head) #........................200
# domainRequest(head) #.......................200
# countryId(head) #...........................200
# logoRequest(head) #.........................201
# appkey=addOrganization(head) #..............200
# getAppkeyRequest(head, appkey) #............200
# listdb(head) #..............................200
# desRequest(head) #..........................200
# addDes(head) #..............................201
# listRoles(head) #...........................200
# addRole(head) #.............................500
# # alltemplates(head) #........................404
# emailTofSES(head) #.........................200
# # emailTofID(head) #..........................404
# iD =createPackage(head) #.......................500
# getPackage(head, iD) #..........................200
# getPakagebyID(head,iD) #.......................200
# ID=createFeatureP(head) #......................405
# getFeaturesforP(head, ID) #.....................200
# getFeaturesforPbyID(head, ID) #.................200
