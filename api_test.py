#@title Beta port Forwarding 생성/삭제 TEST

import sys
import os
import hashlib
import hmac
import base64
import requests
import time
import requests
from threading import Thread
from multiprocessing import Process, Queue
from datetime import datetime, date, timezone
import json
import pdb



class Commander:
    self.uri=""
    self.method ="GET"
    self.access_key = "" 
    self.secret_key = ""
    self.signingKey = ""
    self.base_url = "https://ncloud.beta-apigw.ntruss.com"

    def	make_signature(timestamp):
        secret_key_byte= bytes(self.secret_key, 'UTF-8')
        message = self.method + " " + self.uri + "\n" + timestamp + "\n" + self.access_key
        message = bytes(message, 'UTF-8')    
        self.signingKey = base64.b64encode(hmac.new(secret_key_byte, message, digestmod=hashlib.sha256).digest())
      

    def api_requests(**kwargs):
        data = {}
        timestamp = int(time.time() * 1000)
        timestamp = str(timestamp)
        headers={
            'x-ncp-iam-access-key': self.access_key,
            'x-ncp-apigw-timestamp': timestamp ,
            'x-ncp-apigw-signature-v2': self.signingKey,
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        params ={}
        for name, value in kwargs.items():
            data.update({name: value})
        url = self.base_url+self.uri

        
        if(data["params"] != None ):
            params= data["params"]
        if(data["headers"] != None ):
            headers=data["headers"] 
        response = requests.request(self.method, surl, headers=headers, params=params)
        return response.json()
#params = {'param1': 'value1', 'param2': 'value'}
#requests.request("GET", url, headers=headers, params=params)


if __name__ == "__main__":
    base_url ="https://ncloud.beta-apigw.ntruss.com" #@param {type: "string"}	
    sub_uri="/server/v2/getServerInstanceList
    signature_key=make_signature(serverlisturi,access_key,secret_key,timestamp)
    serverListjson=api_requests(base_url,serverlisturi,signature_key)
           access_key = "TaO91DGIgtK9JTYat37U"			#@param {type: "string"}			# access key id (from portal or sub account)
        secret_key = "Pbzy4hWXyiAXz8a9X0qy7Lc35o4sIWlZ5ngSY94N" #@param {type: "string"}     
    #print (serverListjson)
    serverintanceID=[]
    for serverintance in serverListjson["getServerInstanceListResponse"]["serverInstanceList"]:
        serverintanceID.append(serverintance["serverInstanceNo"])
    #print (serverintanceID)
        
    portForarfingget="/server/v2/getPortForwardingRuleList?responseFormatType=json"
    signature_key=make_signature(portForarfingget,access_key,secret_key,timestamp)
    portForarfingget_json=api_requests(base_url,portForarfingget,signature_key)
    #print (portForarfingget_json)
    
    portFrordingNo = portForarfingget_json["getPortForwardingRuleListResponse"]["portForwardingConfigurationNo"]
    portno = range(1025,65535)
    for a, b in zip(portno,serverintanceID):
        portforwaring="/server/v2/addPortForwardingRules?responseFormatType=json&portForwardingConfigurationNo="+str(portFrordingNo)+"&portForwardingRuleList.1.serverInstanceNo="+str(b)+"&portForwardingRuleList.1.portForwardingExternalPort="+str(a)+"&portForwardingRuleList.1.portForwardingInternalPort=22"
        #print(portforwaring)
        signature_key=make_signature(portforwaring,access_key,secret_key,timestamp)
        portforwaring_json = api_requests(base_url,portforwaring,signature_key)
        time.sleep(10)
        print (str(a)+" ADD 결과 : "+str(portforwaring_json))
   # addPortForwardingRulesResponse': {'requestId': 'bb54b8db-307e-4201-ae7f-cff922133538', 'returnCode': '0', 'returnMessage': 'success'
    portFrordingrowno=0
    while int(portFrordingrowno) == len(serverintanceID):
        portForarfingget="/server/v2/getPortForwardingRuleList?responseFormatType=json"
        signature_key=make_signature(portForarfingget,access_key,secret_key,timestamp)
        portForarfingget_json=api_requests(base_url,portForarfingget,signature_key)
        portFrordingrowno = portForarfingget_json["getPortForwardingRuleListResponse"]["totalRows"]
        print ("["+datetime.now()+"] 총 개수 : " +str(portFrordingrowno))

    del_portno = range(1025 , 65535)
    for c, d in zip(del_portno,serverintanceID):
        portforwaring="/server/v2/deletePortForwardingRules?responseFormatType=json&portForwardingConfigurationNo="+str(portFrordingNo)+"&portForwardingRuleList.1.serverInstanceNo="+str(d)+"&portForwardingRuleList.1.portForwardingExternalPort="+str(c)+"&portForwardingRuleList.1.portForwardingInternalPort=22"
        #print(portforwaring)
        signature_key=make_signature(portforwaring,access_key,secret_key,timestamp)
        portforwaring_json = api_requests(base_url,portforwaring,signature_key)
        print (str(c)+" DEL 결과 : "+str(portforwaring_json))
    
    
