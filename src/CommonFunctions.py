import datetime
import json
import random
import re
import uuid
import string
import time
from src.ConfigParser import ConfigParser
from random import getrandbits
from ipaddress import IPv4Network, IPv4Address
from src.NormalizeData import NormalizeData
from ipaddress import IPv6Network, IPv6Address


class CommonFunctions(NormalizeData):

    def __init__(self, dbo, config_file):
        self.config_file = config_file
        self.cfg = ConfigParser(config_file)
        self.access_token = self.cfg.safe_get('AUTOMATION.RUN', 'ACCESS_TOKEN')
        self.message_unique_key = self.cfg.safe_get('QA.UNIQUE_KEY', 'UNIQUE_KEY')
        self.db = dbo
        self.subscription_id = None
        self.user_id = None
        self.customer_uuid = None
        self.username = self.cfg.safe_get('AUTOMATION.RUN', 'USERNAME')
        self.username_qid = self.cfg.safe_get('AUTOMATION.RUN', 'USERNAME_QID')
        self.has_network_enabled = self.is_network_enabled(self.username)
        self.subscription_id = self.get_subscription_id(self.username)
        self.user_id = self.get_user_id(self.username)
        self.customer_uuid = self.get_customer_uuid(self.username)


    def generate_uuid(self):
        return str(uuid.uuid4())

    def generate_instance_id(self):
        return "i-" + uuid.uuid4().hex[:16]

    def generate_random_number(self):
        return random.randint(1000, 99999)

    def generate_random_ipv4(self):
        # network containing all addresses from 10.0.0.0 to 10.255.255.255
        subnet = IPv4Network("10.0.0.0/8")
        # subnet.max_prefixlen contains 32 for IPv4 subnets and 128 for IPv6 subnets
        # subnet.prefixlen is 24 in this case, so we'll generate only 8 random bits
        bits = getrandbits(subnet.max_prefixlen - subnet.prefixlen)
        # here, we combine the subnet and the random bits
        # to get an IP address from the previously specified subnet
        addr = IPv4Address(subnet.network_address + bits)
        return str(addr)

    def generate_random_ipv6(self):
        subnet = '2001:db8:100::/64'
        network = IPv6Network(subnet)
        ipv6address = IPv6Address(network.network_address + getrandbits(network.max_prefixlen - network.prefixlen))
        return str(ipv6address)

    def get_customer_uuid(self, username=None):
        if self.customer_uuid is not None:
            return self.customer_uuid
        #username = self.username_qid if username is None else username
        username = self.username_qid
        #print("=====***********UserName is"+username)

        query_str = "select UUID from subscription where SUBSCRIPTION_ID = (select SUBSCRIPTION_ID from FO_ACCOUNT where " \
                    "USERNAME=:username)"
        results = self.db.execute_query(query_str, {'username': username})
        for result in results:
            return result[0]

    def get_subscription_id(self, username=None):
        if self.subscription_id is not None:
            return self.subscription_id
        username = self.username if username is None else username
        query_str = "select SUBSCRIPTION_ID from FO_ACCOUNT where USERNAME=:username"
        results = self.db.execute_query(query_str, {'username': username})
        for result in results:
            return result[0]

    def get_portal_id_type(self, hostid):
        query = "select PORTAL_ID_TYPE from USER_HOST where ID=:hostid"
        results = self.db.execute_query(query, {'hostid': hostid})
        for result in results:
            return str(result[0])

    def is_network_enabled(self, username):
        query_str = "select count(1) from ADDONS_SUBSCRIPTION aa inner join ADDONS a on aa.ADDON_ID=a.ID where " \
                    "SUBSCRIPTION_ID=(select SUBSCRIPTION_ID from FO_ACCOUNT where USERNAME=:username) and a.ADDON_NAME " \
                    "='NETWORK SUPPORT'"
        results = self.db.execute_query(query_str, {'username': username})
        for result in results:
            return result[0]

    def get_ec2_network_id(self, username):
        query = "select ID from NETWORK where NAME='Global EC2 Network' and SUBSCRIPTION_ID = (select SUBSCRIPTION_ID from FO_ACCOUNT where USERNAME=:username)"
        results = self.db.execute_query(query, {'username': username})
        for result in results:
            return str(result[0])

    def agent_activation(self, requestId, ip, module, agentUuid=None, hostname=None, netbios=None, os="None",
                         networkId=None,
                         providerName=None, instanceId=None):
        tags = ""
        if agentUuid == None:
            agentUuid = self.generate_uuid()
        assetId = self.generate_random_number()
        manifestUuid = self.generate_uuid()
        customerUuid = self.get_customer_uuid(self.username)
        self.agentActivation_Dict = {}
        self.agentActivation_Dict[self.message_unique_key] = requestId
        self.agentActivation_Dict["customerUuid"] = customerUuid
        self.agentActivation_Dict["action"] = "ACTIVATION"
        self.agentActivation_Dict["assetId"] = assetId
        self.agentActivation_Dict["agentUuid"] = agentUuid
        self.agentActivation_Dict["module"] = module
        self.agentActivation_Dict["manifestUuid"] = manifestUuid
        self.agentActivation_Dict["trackingMethod"] = "QAGENT"
        self.agentActivation_Dict["ip"] = ip
        self.agentActivation_Dict["hostname"] = hostname
        self.agentActivation_Dict["netbios"] = netbios
        self.agentActivation_Dict["os"] = os
        self.agentActivation_Dict["tags"] = tags
        self.agentActivation_Dict["networkId"] = networkId
        if (providerName != None and instanceId != None):
            self.agentActivation_Dict["providerName"] = providerName
            self.agentActivation_Dict["instanceId"] = instanceId
        return (json.dumps(self.agentActivation_Dict))

    def agent_deactivation(self, requestId, ip, module, userHostId, agentUuid=None, networkId=None):
        if agentUuid == None:
            agentUuid = self.generate_uuid()
        assetId = self.generate_random_number()
        customerUuid = self.get_customer_uuid(self.username)
        agentActivation_Dict = {}
        agentActivation_Dict[self.message_unique_key] = requestId
        agentActivation_Dict["customerUuid"] = customerUuid
        agentActivation_Dict["action"] = "DEACTIVATION"
        agentActivation_Dict["assetId"] = assetId
        agentActivation_Dict["agentUuid"] = agentUuid
        agentActivation_Dict["userHostId"] = userHostId
        agentActivation_Dict["module"] = module
        agentActivation_Dict["trackingMethod"] = "QAGENT"
        agentActivation_Dict["ip"] = ip
        agentActivation_Dict["networkId"] = networkId
        return (json.dumps(agentActivation_Dict))

    def activate_vm_agent(self, requestUUID, ip, QAUuid=None, providerName=None, instanceId=None, hostname=None,
                          netbios=None,
                          os=None):
        if hostname == None:
            hostname = "HOST_NAME_" + re.sub(r"\.", "_", ip)
        if netbios == None:
            netbios = "NETBIOS_NAME_" + re.sub(r"\.", "_", ip)
        if os == None:
            os = random.choice(self.OS_NAMES)
        return self.agent_activation(requestUUID, ip, "VM", QAUuid, hostname, netbios, os, None, providerName,
                                     instanceId)

    def deactivate_vm_agent(self, requestUUID, ip, userHostId, agentUuid=None):
        return self.agent_deactivation(requestUUID, ip, "VM", userHostId, agentUuid)

    def activate_pc_agent(self, requestUUID, ip, QAUuid=None, providerName=None, instanceId=None, hostname=None,
                          netbios=None,
                          os=None):
        if hostname == None:
            hostname = "HOST_NAME_" + re.sub(r"\.", "_", ip)
        if netbios == None:
            netbios = "NETBIOS_NAME_" + re.sub(r"\.", "_", ip)
        if os == None:
            os = random.choice(self.OS_NAMES)
        return self.agent_activation(requestUUID, ip, "PC", QAUuid, hostname, netbios, os, None, providerName,
                                     instanceId)

    def deactivate_pc_agent(self, requestUUID, ip, userHostId, agentUuid=None):
        return self.agent_deactivation(requestUUID, ip, "PC", userHostId, agentUuid)

    def activate_sca_agent(self, requestUUID, ip, QAUuid=None, providerName=None, instanceId=None, hostname=None,
                           netbios=None,
                           os=None):
        if hostname == None:
            hostname = "HOST_NAME_" + re.sub(r"\.", "_", ip)
        if netbios == None:
            netbios = "NETBIOS_NAME_" + re.sub(r"\.", "_", ip)
        if os == None:
            os = random.choice(self.OS_NAMES)
        return self.agent_activation(requestUUID, ip, "SCA", QAUuid, hostname, netbios, os, None, providerName,
                                     instanceId)

    def deactivate_sca_agent(self, requestUUID, ip, userHostId, agentUuid=None):
        return self.agent_deactivation(requestUUID, ip, "SCA", userHostId, agentUuid)

    def validate_response(self, responseMessage, requestMessage):
        s1 = json.dumps(responseMessage)
        res_decode = json.loads(s1)
        req_decode = json.loads(requestMessage)
        if res_decode["response"] != "SUCCESS":
            print("Invalid Response Message Found")
            return False
        if res_decode["customerUuid"] != req_decode["customerUuid"]:
            print("Invalid customerUUID found in Response Message")
            return False
        if res_decode["assetId"] != req_decode["assetId"]:
            print("Invalid assetId found in Response Message")
            return False
        if req_decode["trackingMethod"] == "QAGENT":
            if res_decode["assetUuid"] != req_decode["agentUuid"]:
                print("Invalid agentUuid found in Response Message")
                return False
        return True

    def get_host_id(self, responseMessage):
        self.s1 = json.dumps(responseMessage)
        self.m = json.loads(self.s1)
        self.usr_host_id = self.m["userHostId"]
        return self.usr_host_id

    def validate_portal_id_type(self, responseMessage, expected_id):
        msg = json.loads(responseMessage)
        host_id = msg["userHostId"]
        actualID = self.get_portal_id_type(host_id)
        return ((actualID & expected_id) != 0)

    def update_last_vm_scan_date_agent(self, host_id):
        update_time = time.mktime((datetime.datetime.now() - datetime.timedelta(hours=24)).timetuple())
        query = "update AGENT_SCAN_INFO set SCAN_VALUE=:time where SCAN_KEY='_LAST_VM_SCAN_DATE' and " \
                "USER_HOST_ID=:host_id"
        self.db.update_query(query, {'time': update_time, 'host_id': host_id})

    def generate_chirp_request(self, ip, agent_uuid, customer_uuid, state_id,
                               chirp_type="Chirper.ReportTypeVulnerability", report_data=None):
        occured_chirp_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        chirp_request_dict = {}
        chirp_request_dict["ChirpType"] = chirp_type
        chirp_request_dict["Occurred"] = occured_chirp_time
        chirp_request_dict["CustomerId"] = customer_uuid
        chirp_request_dict["AgentId"] = agent_uuid
        chirp_request_dict["InBoundIPAddress"] = ip
        chirp_request_dict["StateId"] = state_id
        if report_data is not None:
            chirp_request_dict["ReportData"] = report_data
        return json.dumps(chirp_request_dict)

    def get_user_id(self, username=None):
        if self.user_id is not None:
            return self.user_id

        username = self.username if username is None else username
        query_str = "select USER_ID from FO_ACCOUNT where USERNAME=:username"
        return self.db.fetch_value(query_str, {'username': username})

    def get_kernel(self):
        return str(random.choice(list(NormalizeData.kernel_list.keys())))

    def get_device_flag(self, device_type):
        if device_type == NormalizeData.DEVICE_TYPE_WIN:
            return "n"
        else:
            return "u"

    def cleanup_vm_data(self, host_id):

        query = "DELETE FROM ticket where HOST_ID=:host_id"
        self.db.update_query(query, {'host_id': host_id})

        query = "DELETE FROM host_port_service where user_host_id=:host_id"
        self.db.update_query(query, {'host_id': host_id})

        query = "DELETE FROM host_application where user_host_id=:host_id"
        self.db.update_query(query, {'host_id': host_id})

        query = "DELETE FROM user_predicted_vuln where host_id=:host_id"
        self.db.update_query(query, {'host_id': host_id})

        query = "DELETE FROM host_authentication where host_id=:host_id"
        self.db.update_query(query, {'host_id': host_id})

        query = "DELETE FROM user_host_info where host_id=:host_id"
        self.db.update_query(query, {'host_id': host_id})

        query = "DELETE FROM USER_HOST_INTERFACE where user_host_id=:host_id"
        self.db.update_query(query, {'host_id': host_id})

        query = "DELETE FROM user_vuln_arf_rule_eval WHERE user_vuln_id IN (SELECT id FROM user_vuln  WHERE host_id " \
                "=:host_id)"
        self.db.update_query(query, {'host_id': host_id})

        query = "DELETE FROM user_vuln_cert WHERE user_vuln_id IN (SELECT id FROM user_vuln  WHERE host_id = :host_id)"
        self.db.update_query(query, {'host_id': host_id})

        query = "DELETE FROM user_vuln_info WHERE user_vuln_id IN (SELECT id FROM user_vuln  WHERE host_id = :host_id)"
        self.db.update_query(query, {'host_id': host_id})

        query = "DELETE FROM user_vuln where host_id=:host_id"
        self.db.update_query(query, {'host_id': host_id})
