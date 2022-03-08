from builtins import print

import pytest
from src.SearchList import SeachList


@pytest.mark.Pod3Test
class Pod3Test:
    """Test Single Searchlist -"""
    def test_sl_01(self, api_client, common_functions, op_path, dbo):
        """TC 03 - Create Dynamic Search List with Discovery Methods - "Remote_Authenticated"""
        params = {"discovery_methods": "Remote,Authenticated"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qid')

    # def test_sl_02(self, api_client, common_functions, op_path, dbo):
    #     """TC 02 - Create Dynamic Search List with Discovery Methods - Remote"""
    #     params = {"discovery_methods": "Remote"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created: SL-QWEB", sl_id_qweb)
    #     sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    #     print("Created: SL-Service", sl_id_service)
    #     assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #     SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')
    #
    #
    # def test_sl_01(self, api_client, common_functions, op_path, dbo):
    #     """TC 01 - Create Dynamic Search List with Discovery Methods - Authenticated"""
    #     params = {"discovery_methods": "Authenticated"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created: SL-QWEB", sl_id_qweb)
    #     sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    #     print("Created: SL-Service", sl_id_service)
    #     assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #     SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')