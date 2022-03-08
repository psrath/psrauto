import json

import requests
import curlify
from src.ConfigParser import ConfigParser


class ApiClient(object):

    def __init__(self, config_file):
        self.config_file = config_file
        cfg = ConfigParser(config_file)
        #self.pod = ConfigParser(config_file).safe_get('AUTOMATION.RUN', 'URL')
        self.authentication_qweb = (cfg.safe_get('AUTOMATION.RUN', 'USERNAME'), cfg.safe_get('AUTOMATION.RUN', 'PASSWORD'))
        self.authentication_qid = (cfg.safe_get('AUTOMATION.RUN', 'USERNAME_QID'), cfg.safe_get('AUTOMATION.RUN', 'PASSWORD_QID'))
        self.access_token = cfg.safe_get('AUTOMATION.RUN', 'ACCESS_TOKEN')

    def api_call(self, pod_url, method, uri, params=None, calltype=None, request_headers=None, op_filename=None, ):
        requests.packages.urllib3.disable_warnings()
        self.headers = {'X-Requested-With': 'curl', 'X-Access-Token': 'automation'}
        if (calltype == "qweb") or (calltype == None):
            authprofile = self.authentication_qweb
        elif calltype == "qid":
            authprofile = self.authentication_qid
        else:
            authprofile = None
        self.url = pod_url + "" + uri
        self.method = method
        self.params = None
        self.data = None
        self.json = None

        if request_headers != None:
            self.headers.update(request_headers)
        self._types = {"GET": requests.get, "POST": requests.post, "DELETE": requests.delete}
        if self.method == "GET":
            self.params = params
        if self.method == "POST":
            self.json = params
        else:
            self.data = json.dumps(params)
        if method not in self._types:
            raise ValueError("Wrong method")
        self.response = self._types[self.method](url=self.url, headers=self.headers, params=self.params, data=self.data, json=self.json, auth=authprofile, verify=False)
        self.op_filename = op_filename

        if self.op_filename != None:
            with open(self.op_filename, 'wb') as handle:
                for block in self.response.iter_content(1024):
                    handle.write(block)
        print(curlify.to_curl(self.response.request))
        return self.response

    def qualys_api_call(self, method, uri, params=None, calltype=None, request_headers=None, op_filename=None):
        pod_url = ConfigParser(self.config_file).safe_get('AUTOMATION.RUN', 'QUALYSAPI_URL')
        return self.api_call(pod_url, method, uri, params, calltype, request_headers, op_filename)


    def bfss_api_call(self, method, uri, params=None, request_headers=None, op_filename=None):
        pod_url = ConfigParser(self.config_file).safe_get('AUTOMATION.RUN', 'BFSS_URL')
        return self.api_call(pod_url, method, uri, params, request_headers, op_filename)

    def qid_service_api_call(self, method, url=None, params=None, calltype=None, request_headers=None):
        print("=========URL passed:"+url)
        if url is not None:
            pod_url = ConfigParser(self.config_file).safe_get('AUTOMATION.RUN', 'QID_SERVICE_URL')
        else:
            pod_url = ConfigParser(self.config_file).safe_get('AUTOMATION.RUN', 'QID_SERVICE_API')
        request_headers = {'Accept': 'application/json', 'X-Access-Token': self.access_token, 'Accept-Chargeset': 'UTF-8', 'X-Requested-With': self.access_token}
        print("CallType params value::"+calltype)
        print("Params=========", params)
        return self.api_call(pod_url, method, url, params, calltype, request_headers)

    def print_request(self):
        return (curlify.to_curl(self.response.request))

# a = ApiClient("https://qualysguard.p04.eng.sjc01.qualys.com", auth=('mayur_mm', 'qatemp'))
# res=a.api_call("GET","/msp/about.php",request_headers={'Content-Type': 'application/json'})
# res = a.api_call("GET", "/msp/about.php")
# print ("================== Request Body ================\n")
# print (res.request.body)
# print ("================== Request Headers ================\n")
# print (res.request.headers)
# print ("================== URL ================\n")
# print (res.request.url)
# print ("================== Response ================\n")
# print (res.text)
# print (a.print_request())

# # ###### Schedule Scan List
# params = {'action': 'list'}
# res = a.api_call("GET", "/api/2.0/fo/schedule/scan/", params)
# print ("================== Response ================\n")
# print (res.text)
# print (a.print_request())
#
# # ###### Schedule Scan List
# params = {'action': 'list'}
# res = a.api_call("POST", "/api/2.0/fo/scan/", params)
# print ("================== Response ================\n")
# print (res.text)
# print (a.print_request())
# print (res.status_code)


# ##   Example with JSON Input data
#
# json_data="""{
#   "AgentId": "string",
#   "ChirpType": "Chirper.ChirpReportTypeVMPCDelta",
#   "CustomerId": "string",
#   "InBoundIPAddress": "string",
#   "Occurred": "string",
#   "ReportData": "string",
#   "StateId": "string",
#   "occuredDate": "2018-10-09T10:31:51.687Z"
# }"""
#
# a = ApiClient("http://10.114.69.158:50260")
# res = a.api_call("POST", "/vmsp/1.0/tests/process/agent", json_data,request_headers={'Content-Type': 'application/json'})
# print ("================== Response ================\n")
# print (res.text)
# print (a.print_request())
