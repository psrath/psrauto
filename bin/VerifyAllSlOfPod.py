import json
import time
import curlify
import cx_Oracle
import sys
import requests
from lxml import etree
import logging


class XmlParser:
    ''' XML Parser '''

    def __init__(self, xmlSource):
        self.xmlSource = xmlSource
        parser = etree.XMLParser(strip_cdata=False, remove_blank_text=True)
        self.root = etree.XML(bytes(bytearray(self.xmlSource, encoding='utf-8')), parser)

    def get_elements(self, xpath):
        return self.root.findall(xpath)

    def get_element_count(self, xpath):
        count = len(self.root.xpath(xpath))
        return count

    def get_element(self, xpath):
        return self.root.find(xpath)

    def get_element_text(self, xpath):
        # print xpath
        return self.root.xpath(xpath)[0].text

    def get_all_child_tags_tostring(self, xpath):
        el = self.get_element(xpath)
        if el is not None:
            return etree.tostring(el, method='xml', pretty_print=True).decode()
        return None

    def get_element_attribute(self, name, xpath='.', default=None):
        return self.root.find(xpath).get(name, default)


class VerifyAllSL:

    def __init__(self, config, logging):
        if "sub_id" in config:
            self.sub_id = config["sub_id"]
        else:
            self.sub_id = None
        self.db_host = config["db_host"]
        self.db_user = config["db_user"]
        self.db_pass = config["db_pass"]
        self.db_service = config["db_service"]
        self.qid_service_api = config["qid_service_api"]
        self.qualys_api = config["qualys_api"]
        self.connect = self.db()
        self.logging = logging

    def db(self):
        conn_str = self.db_user + "/" + self.db_pass + "@" + self.db_host + "/" + self.db_service
        return cx_Oracle.connect(conn_str)

    def execute_query(self, query, params=None):
        cursor = self.connect.cursor()
        result = cursor.execute(query, params).fetchall()
        cursor.close()
        return result

    def update_query(self, query, params=None):
        cursor = self.connect.cursor()
        cursor.execute(query, params)
        self.connect.commit()
        cursor.close()

    def get_customer_uuid(self, sub_id):
        query_str = "select UUID from subscription where SUBSCRIPTION_ID =:sub_id"
        results = self.execute_query(query_str, {'sub_id': sub_id})
        for result in results:
            return result[0]

    def get_qweb_search_list_through_infra_api(self, sl_id, sub_id):
        requests.packages.urllib3.disable_warnings()
        address = self.qualys_api + "/api/2.0/infra/portal/search_list/"
        headers_data = {'X-Requested-With': 'curl'}
        params = {
            "action": "list",
            "ids": sl_id,
            "show_qids": "1",
            "subscription_id": sub_id
        }
        res = requests.get(address, params=params, headers=headers_data, verify=False)
        print(curlify.to_curl(res.request))
        return res.text

    def verify_qids_pod(self, sl_id, sub_id):
        qweb_sl = self.get_qweb_search_list_through_infra_api(sl_id, sub_id)
        print("---Criteria---")
        print(self.get_criteria_list(qweb_sl))
        print("--------------")
        qweb_qids = self.get_qid_list_from_xml(qweb_sl)
        qid_service_sl = self.get_qid_service_search_list(sl_id, sub_id)
        qid_service_qids = self.get_qid_list_from_json(qid_service_sl)
        if not self.compare_qweb_qids_and_service_qids(qweb_qids, qid_service_qids):
            return False
        return True

    def get_criteria_list(self, xml_data):
        return XmlParser(xml_data).get_all_child_tags_tostring('.//CRITERIA')

    def get_qid_service_search_list(self, sl_id, sub_id):
        requests.packages.urllib3.disable_warnings()
        address = self.qid_service_api + "/resolve"
        headers_data = {'X-Requested-With': 'curl'}
        params = {
            "customerUuid": self.get_customer_uuid(sub_id),
            "lang": "en",
            "searchListId": sl_id,
            "noCache": "true"
        }
        res = requests.get(address, params=params, headers=headers_data, verify=False)
        print(curlify.to_curl(res.request))
        return res.text

    def get_qid_list_from_xml(self, xml_data):
        list_qid = []
        qids = XmlParser(xml_data).get_elements('.//QID')
        for qid in qids:
            list_qid.append(qid.text)
        print("QWEB QID count:", len(list_qid))
        return list_qid

    def get_qid_list_from_json(self, json_data):
        list_qid = []
        json_decoded = json.loads(json_data)
        qids = json_decoded["data"]
        for qid, flag in qids.items():
            list_qid.append(qid)
        print("QID Service count:", len(list_qid))
        return list_qid

    def compare_qweb_qids_and_service_qids(self, qweb_qids, service_qids):
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

    def verify_all_dynamic_sl_of_pod(self):
        if self.sub_id is not None:
            query_str = "select ID,SUBSCRIPTION_ID from SEARCH_LIST where SUBSCRIPTION_ID=:sub_id and SEARCH_LIST_DYNAMIC_ID is not null and " \
                        "IS_SYSTEM = 0"
            sl_ids = self.execute_query(query_str, {'sub_id': self.sub_id})
        else:
            query_str = "select ID,SUBSCRIPTION_ID from SEARCH_LIST where SEARCH_LIST_DYNAMIC_ID is not null and " \
                        "IS_SYSTEM = 0"
            sl_ids = self.execute_query(query_str)
        is_failed = False
        cnt_passed = 0
        cnt_failed = 0
        for sl_id in sl_ids:
            print("================================================================================")
            print("Verifying for Search List:", sl_id[0])
            if not self.verify_qids_pod(sl_id[0], sl_id[1]):
                print("FAILED: Search List Validation for ID:", sl_id[0])
                logging.info(str(sl_id[1]) + "," + str(sl_id[0]) + ",FAILED")
                is_failed = True
                cnt_failed += 1
            else:
                logging.info(str(sl_id[1]) + "," + str(sl_id[0]) + ",PASSED")
                print("PASSED: Search List Validation for ID:", sl_id[0])
                cnt_passed += 1

        print("************** Summary of all search list ************")
        print("Total Passed: " + str(cnt_passed))
        print("Total Failed: " + str(cnt_failed))
        print("******************************************************")
        if is_failed:
            return False
        return True

    def verified_only_faild_cases(self, filename):
        cnt_passed = 0
        cnt_failed = 0
        is_failed = False
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                data = line.split(":")[-1].rstrip('\r\n')
                sub_id = data.split(",")[0]
                sl_id = data.split(",")[1]
                status = data.split(",")[2]
                if status == "FAILED":
                    print("Verifying for sub_id:", sub_id, "sl_id:", sl_id, "Previous status:", status)
                    if not self.verify_qids_pod(sl_id, sub_id):
                        print("FAILED: Search List Validation for ID:", sl_id)
                        logging.info(str(sub_id) + "," + str(sl_id) + ",FAILED")
                        is_failed = True
                        cnt_failed += 1
                    else:
                        logging.info(str(sub_id) + "," + str(sl_id) + ",PASSED")
                        print("PASSED: Search List Validation for ID:", sl_id)
                        cnt_passed += 1
            print("************** Summary of all search list ************")
            print("Total Passed: " + str(cnt_passed))
            print("Total Failed: " + str(cnt_failed))
            print("******************************************************")
            if is_failed:
                return False
            return True


if __name__ == "__main__":
    config = {
        "db_host": 'qdb01.p04.eng.sjc01.qualys.com',
        "db_user": 'QWEB29_USER',
        "db_pass": 'qualys2005!2',
        "db_service": 'QWEB',
        "sub_id": 44,
        "qid_service_api": "http://qbep03.p04.eng.sjc01.qualys.com:50261/searchlist/1.0",
        "qualys_api": "https://qualysapi.p04.eng.sjc01.qualys.com"
    }
    logdatetime = time.strftime("%Y%m%d%I%M%S")
    log_file_name = 'sl_' + logdatetime + '.log'
    print("Logging File:" + log_file_name)
    logging.basicConfig(filename=log_file_name, level=logging.INFO)
    vsl = VerifyAllSL(config, logging)
    if len(sys.argv) > 1:
        print("Executing only Failed Cases")
        file_name = sys.argv[1]
        print(file_name)
        vsl.verified_only_faild_cases(file_name)
    else:
        vsl.verify_all_dynamic_sl_of_pod()
