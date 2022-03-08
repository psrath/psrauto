
import pytest
from src.XmlParser import XmlParser

@pytest.mark.TestSeachListResolve578
class TestSeachListResolve578:
    """XML file comparison -"""

    def get_qid_list_from_xml(self,xml_data, calltype):
        list_qid = []
        qids = XmlParser(xml_data).get_elements('.//QID')
        for qid in qids:
            list_qid.append(qid.text)
        if calltype == "qweb":
            print("QWEB QID count:", len(list_qid))
        else:
            print("Service QID count:", len(list_qid))

        return list_qid

    def compare_qweb_qids_and_service_qids(self,qweb_qids, service_qids):
        is_failed = False
        diff_qids = set(qweb_qids).difference(set(service_qids))
        if len(diff_qids) > 0:
            print("Extra QID Found in QWEB", diff_qids)
            is_failed = True
        diff_qids = set(service_qids).difference(set(qweb_qids))
        if len(diff_qids) > 0:
            print("Extra QID Found in QID Service", diff_qids)
            is_failed = True
        if is_failed:
            return False
        return True

    def test_xml_1(self, api_client, common_functions, op_path, dbo):
        """TC 160 - Compare kblist API service enable and disable subscription"""
        params = {"action": "list", "details": "All", "show_supported_modules_info": "1"}
        res_qweb = api_client.qualys_api_call("GET", "/api/2.0/fo/knowledge_base/vuln/", params,"qweb")
        res_qid = api_client.qualys_api_call("GET", "/api/2.0/fo/knowledge_base/vuln/", params, "qid")
        qweb_qid = self.get_qid_list_from_xml(res_qweb, "qweb")
        service_qid = self.get_qid_list_from_xml(res_qid, "service")
        value = self.compare_qweb_qids_and_service_qids(qweb_qid,service_qid)
        if value:
            print("No Difference in QID count missmatch in QWEB and QID-service")
        else:
            print("Difference in QID count QWEB and QID-Service")



