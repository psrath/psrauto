import json
import random
import string
import time

from src.XmlParser import XmlParser


def create_dynamic_search_list(api_client, other_params, calltype=None):
    title = ''.join(random.choice(random.choice(string.ascii_lowercase)) for _ in range(10))
    params = {
        "action": "create",
        "title": title,
        "global": "1",
        "comments": "Dynamic SL Created for QID Service"
    }
    params.update(other_params)
    res = api_client.qualys_api_call("POST", "/api/2.0/fo/abcd/search_list/dynamic/", params, calltype)
    if res.status_code != 200:
        if calltype == "qweb":
            print("Invalid Status Code returned byAPI")
        if calltype == "qid":
            print("Invalid Status Code returned by service API")
        print(res.text)
        return False
    return XmlParser(res.text).get_element_text('//VALUE')

def create_static_search_list(api_client, other_param,calltype):
    title = ''.join(random.choice(random.choice(string.ascii_lowercase)) for _ in range(10))
    params = {
        "action": "create",
        "title": title,
        "global": "1",
        "comments": "Static SL Created forService"
    }
    params.update(other_param)
    res = api_client.qualys_api_call("POST", "/api/2.0/fo/qid/search_list/static/", params, calltype)
    if res.status_code != 200:
        print("Invalid Status Code returned by API")
        print(res.text)
        return False
    return XmlParser(res.text).get_element_text('//VALUE')



def delete_dynamic_search_list(sl_id, api_client, calltype):
    params = {
        "action": "delete",
        "id": sl_id
    }
    res = api_client.qualys_api_call("POST", "/api/2.0/fo/abcd/search_list/dynamic/", params, calltype)
    if res.status_code != 200:
        print("Invalid Status Code returned by  API")
        print(res.text)
        return False
    return XmlParser(res.text).get_element_text('//VALUE')

def list_static_search_list(api_client,sl_id,callType):
    params = {
        "action": "list",
        "ids": sl_id
    }
    res = api_client.qualys_api_call("GET", "/api/2.0/fo/abc/search_list/static/", params, callType)
    cnt = XmlParser(res.text).get_element_count('//QID')
    if res.status_code != 200:
        print("Invalid Status Code returned by  API")
        print(res.text)
        return False
    return cnt

def delete_static_search_list(api_client,sl_id,callType):
    params = {
        "action": "delete",
        "ids": sl_id
    }
    res = api_client.qualys_api_call("GET", "/api/2.0/fo/abc/search_list/static/", params, callType)
    if res.status_code != 200:
        print("Invalid Status Code returned by API")
        return False
    return True

def update_static_search_list(api_client,other_params, sl_id, calltype):
    params = {
        "action": "update",
        "id": sl_id,
        "comments": "Static Serach List Updated",
        "global": "1"
    }
    params.update(other_params)
    res = api_client.qualys_api_call("POST", "/api/2.0/fo/abc/search_list/static/", params,calltype)
    if res.status_code != 200:
        print("Invalid Status Code returned by  API")
        print(res.text)
        return False
    return True

def get_qweb_search_list(api_client, sl_id, calltype):
    params = {
        "action": "list",
        "ids": sl_id,
        #"show_qids": "1"
    }
    if calltype=="qweb":
        print("Calling  API------------\n")
    else:
        print("Calling Service API------------\n")

    res = api_client.qualys_api_call("GET", "/api/2.0/fo/abbc/search_list/dynamic/index.php", params, calltype)
    if res.status_code != 200:
        print("Invalid Status Code returned by  API\n")
        print(res.text)
        return False
    return res.text

def qid_update_or_list_reset(api_client, qid, calltype, action_value, sevirity=None, update_params=None):
    params = {
        "action": action_value,
        "params": qid,
        "severity": sevirity
    }
    if update_params != None:
        params.update(update_params)
    if action_value == "list":
        params["ids"] = params.pop("params")
        params.pop("severity")
    if action_value == "edit":
        params["qid"] = params.pop("params")
    if action_value == "reset":
        params["qid"] = params.pop("params")
        params.pop("severity")
    if calltype=='qweb':
        print("Calling  API------------\n")
    else:
        print("Calling Service API------------\n")
    res = api_client.qualys_api_call("POST", "/api/2.0/fo/base/vuln/", params, calltype)
    if res.status_code != 200:
        print("Invalid Status Code returned by  API")
        print(res.text)
        return False
    return res.text


def get_criteria_list(xml_data):
    return XmlParser(xml_data).get_all_child_tags_tostring('.//CRITERIA')


def get_qid_sevirity(xml_data):
    return XmlParser(xml_data).get_all_child_tags_tostring('.//SEVERITY_LEVEL')

def verify_qid_service_API_call(api_client,common_functions,tested_params,url):
    params = {
        "customerUuid": common_functions.get_customer_uuid(),
        "lang": "en",
        "noCache": "true",
        #"qid": qids,
        #"noCache": "true",
        #"scope": "All"
    }
    print("CustomerUUID is::::::::"+params["customerUuid"])
    params.update(tested_params)
    res = api_client.qid_service_api_call("GET",url,params,"qid")
    print(res)
    result= res.status_code
    print("Status Code Return by QID-service::{}".format(+res.status_code))
    assert res.status_code == 200, "Invalid Status Code returned by QID-Service API"
    return res.text

def verify_qid_service_CVE_call(api_client,common_functions,tested_params,url):
    # params = {
    #     "customerUuid": common_functions.get_customer_uuid(),
    #     #"lang": "en",
    #     #"noCache": "true",
    #     #"qid": qids,
    #     #"noCache": "true",
    #     #"scope": "All"
    # }
    #print("CustomerUUID is::::::::"+params["customerUuid"])
    #params.update(tested_params)
    res = api_client.qid_service_api_call("POST",url,tested_params,"qid")
    print(res)
    print("Status Code Return by QID-service::{}".format(+res.status_code))
    try:
        assert res.status_code == 200, "Invalid Status Code returned by QID-Service API"
    except AssertionError as e:
        print(repr(e))
    return res.text

def get_qid_service_search_list(api_client, common_functions, sl_id):
    access_token = common_functions.access_token
    params = {
        "customerUuid": common_functions.get_customer_uuid(),
        "lang": "en",
        "searchListId": sl_id,
        "noCache": "true"
    }
    headers = {
        "Accept": "application/json",
        "X-Access-Token": access_token
    }
    res = api_client.qid_service_api_call("GET", "/resolve", params, headers)
    assert res.status_code == 200, "Invalid Status Code returned by Service API"
    return res.text

def get_qid_service_search_list_bulk(api_client, common_functions, sl_id):
    access_token = common_functions.access_token
    params = {
        "customerUuid": common_functions.get_customer_uuid(),
        "lang": "en",
        "searchListIds": sl_id,
        "noCache": "true"
    }
    # headers = {
    #     "Accept": "application/json",
    #     "X-Access-Token": access_token,
    #     "Accept-Chargeset": "UTF-8",
    #     "X-Requested-With": access_token
    # }
    res = api_client.qid_service_api_call("GET", "/resolve/bulk", params)
    assert res.status_code == 200, "Invalid Status Code returned by  API"
    return res.text

def get_qid_service_search_list_resolvecall(api_client, common_functions, sl_id):
    access_token = common_functions.access_token
    params = {
        "customerUuid": common_functions.get_customer_uuid(),
        "lang": "en",
        "searchListIds": sl_id,
        "noCache": "true"
    }
    # headers = {
    #     "Accept": "application/json",
    #     "X-Access-Token": access_token,
    #     "Accept-Chargeset": "UTF-8",
    #     "X-Requested-With": access_token
    # }
    res = api_client.qid_service_api_call("GET", "/resolve/paged", params)
    assert res.status_code == 200, "Invalid Status Code returned by API"
    return res.text


def get_qid_list_from_xml(xml_data):
    list_qid = []
    qids = XmlParser(xml_data).get_elements('.//QID')
    for qid in qids:
        list_qid.append(qid.text)
    print("QWEB QID count:", len(list_qid))
    return list_qid

def get_qid_list_from_xml(xml_data,service_type):
    list_qid = []
    qids = XmlParser(xml_data).get_elements('.//QID')
    for qid in qids:
        list_qid.append(qid.text)
    if service_type == "qweb":
        print("QWEB QID count:", len(list_qid))
    else:
        print("Service QID count:", len(list_qid))
    return list_qid


def get_qid_list_from_json(json_data):
    list_qid = []
    json_decoded = json.loads(json_data)
    qids = json_decoded["data"]
    for qid, flag in qids.items():
        list_qid.append(qid)
    print("QID Service count:", len(list_qid))
    return list_qid


def compare_qweb_qids_and_service_qids(qweb_qids, service_qids):
    is_failed = False
    diff_qids = set(qweb_qids).difference(set(service_qids))
    if len(diff_qids) > 0:
        print("Extra QID Found in QWEB SL", diff_qids)
        is_failed = True
    diff_qids = set(service_qids).difference(set(qweb_qids))
    if len(diff_qids) > 0:
        print("Extra QID Found in QID Service SL", diff_qids)
        is_failed = True

    if is_failed:
        return False

    return True

def verify_qids_bulk_resolve(sl_id, api_client, common_functions):
    print("Searchlist IDs "+sl_id)
    qweb_sl = get_qweb_search_list(api_client, sl_id)
    print("---Criteria---")
    print(get_criteria_list(qweb_sl))
    print("--------------")
    qweb_qids = get_qid_list_from_xml(qweb_sl)
    qid_service_sl = get_qid_service_search_list_bulk(api_client, common_functions, sl_id)
    qid_service_qids = get_qid_list_from_json(qid_service_sl)
    if not compare_qweb_qids_and_service_qids(qweb_qids, qid_service_qids):
        return False
    return True


def verify_qids(sl_id, api_client, common_functions):
    qweb_sl = get_qweb_search_list(api_client, sl_id)
    print("---Criteria---")
    print(get_criteria_list(qweb_sl))
    print("--------------")
    qweb_qids = get_qid_list_from_xml(qweb_sl)
    qid_service_sl = get_qid_service_search_list(api_client, common_functions, sl_id)
    qid_service_qids = get_qid_list_from_json(qid_service_sl)
    if not compare_qweb_qids_and_service_qids(qweb_qids, qid_service_qids):
        return False
    return True

def verify_qids_qweb_service(sl_id_qweb, sl_id_qid, api_client, common_functions):
    qweb_sl = get_qweb_search_list(api_client, sl_id_qweb,'qweb')
    print("---Criteria-QWEB---")
    print(get_criteria_list(qweb_sl))
    print("------------------------")
    servc_sl = get_qweb_search_list(api_client, sl_id_qid,'qid')
    print("---Criteria-SERVICE---")
    print(get_criteria_list(servc_sl))
    print("--------------")
    qweb_qids = get_qid_list_from_xml(qweb_sl,"qweb")
    srvc_qids = get_qid_list_from_xml(servc_sl,"service")
    if not compare_qweb_qids_and_service_qids(qweb_qids, srvc_qids):
        return False
    return True



def verify_qids_static(sl_id, api_client, common_functions, calltype):
    qweb_sl = get_qweb_search_list_static(api_client, sl_id, 'qweb')
    print("---Criteria---")
    print(get_criteria_list(qweb_sl))
    print("--------------")
    qweb_qids = get_qid_list_from_xml(qweb_sl)
    qid_service_sl = get_qid_service_search_list(api_client, common_functions, sl_id,'qid')
    qid_service_qids = get_qid_list_from_json(qid_service_sl)
    if not compare_qweb_qids_and_service_qids(qweb_qids, qid_service_qids):
        return False
    return True


def verify_all_dynamic_sl_in_subscription(api_client, common_functions, dbo):
    sub_id = common_functions.get_subscription_id()
    query_str = "select ID from SEARCH_LIST where SUBSCRIPTION_ID=:sub_id and SEARCH_LIST_DYNAMIC_ID is not null and " \
                "IS_SYSTEM = 0"
    sl_ids = dbo.execute_query(query_str, {'sub_id': sub_id})
    is_failed = False
    cnt_passed = 0
    cnt_failed = 0
    for sl_id in sl_ids:
        print("================================================================================")
        print("Verifying for Search List:", sl_id[0])
        if not verify_qids(sl_id[0], api_client, common_functions):
            print("FAILED: Search List Validation for ID:", sl_id[0])
            is_failed = True
            cnt_failed += 1
        else:
            print("PASSED: Search List Validation for ID:", sl_id[0])
            cnt_passed += 1

    print("************** Summary of all search list ************")
    print("Total Passed: " + str(cnt_passed))
    print("Total Failed: " + str(cnt_failed))
    print("******************************************************")
    if is_failed:
        return False
    return True
