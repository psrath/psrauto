import random
import string
from builtins import print

import pytest
from src.SearchList import SeachList


@pytest.mark.TestSearchList999
class TestSearchList999:
    """Test SearchList Resolve -"""
    def test_sl_01(self, api_client, common_functions, op_path, dbo):
        """TC 01 - Create Dynamic Search List with Discovery Methods - Authenticated"""
        params = {"discovery_methods": "Authenticated"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')

    def test_sl_02(self, api_client, common_functions, op_path, dbo):
        """TC 02 - Verify QID look up with Scope as Basic"""
        qids = "155292"
        uri = "/qid/1.0/"
        params = {"qid": qids, "scope": "Basic"}
        result = SeachList.verify_qid_service_API_call(api_client,common_functions,params,uri)
        print(result)
        if qids in result:
            flag = True
        else:
            print(result.text)
        assert flag, "Issue with service call"
    def test_sl_03(self, api_client, common_functions, op_path, dbo):
        """TC 03 - Verify QID look up with Scope as All"""
        qids = "155292"
        uri = "/qid/1.0/"
        params = {"qid": qids, "scope": "All"}
        result = SeachList.verify_qid_service_API_call(api_client,common_functions,params,uri)
        print(result)
        if qids in result:
            flag = True
        else:
            print(result.text)
        assert flag, "Issue with QID Look up service call"
    # def test_sl_04(self, api_client, common_functions, op_path, dbo):
    #     """TC 04 - Verify QID List with Scope as Basic"""
    #     #qids = "155292"
    #     uri = "/qid/1.0/v2/list"
    #     params_sl = {"details": "Basic", "show_disabled_flag": True, "show_pci_reasons": True, "show_qid_change_log": True, "show_supported_modules_info": True, "show_vuln_detection_info": True}
    #     result = SeachList.verify_qid_service_API_call(api_client,common_functions,params_sl,uri)
    #     print(result)
    #     if "vuln" in result:
    #         flag = True
    #     else:
    #         print(result.text)
    #     assert flag, "Issue with QID List service call"
    # def test_sl_05(self, api_client, common_functions, op_path, dbo):
    #     """TC 05 - Verify QID List with Scope as None"""
    #     qids = "155292"
    #     uri = "/qid/1.0/v2/list"
    #     params_sl = {"details": "None", "show_disabled_flag": True, "show_pci_reasons": True, "show_qid_change_log": True, "show_supported_modules_info": True, "show_vuln_detection_info": True}
    #     result = SeachList.verify_qid_service_API_call(api_client,common_functions,params_sl,uri)
    #     print(result)
    #     if "ID_SET" in result:
    #         flag = True
    #     else:
    #         print(result.text)
    #     assert flag, "Issue with QID List service call"

    def test_sl_06(self, api_client, common_functions, op_path, dbo):
        """TC 06 - Verify Dynamic SL resolve call"""
        params_sl = {"discovery_methods": "Authenticated"}
        uri = "/searchlist/1.0/resolve/"
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params_sl, 'qweb')
        params_service = {"searchListId": sl_id_qweb}
        result = SeachList.verify_qid_service_API_call(api_client, common_functions, params_service, uri)
        if "data" in result:
            flag = True
        else:
            print(result.text)
        assert flag, "Issue with QID Resolve service call"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')

    def test_sl_07(self, api_client, common_functions, op_path, dbo):
        """TC 07 - Verify SL page resolve call with dynamic SL"""
        params_sl = {"discovery_methods": "Authenticated"}
        uri = "/searchlist/1.0/resolve/paged/"
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params_sl, 'qweb')
        params_service = {"limit": "1000", "offset": "1003", "searchListId": sl_id_qweb}
        result = SeachList.verify_qid_service_API_call(api_client, common_functions, params_service, uri)
        if "data" in result:
            flag = True
        else:
            print(result.text)
        assert flag, "Issue with QID Resolve service call"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')









