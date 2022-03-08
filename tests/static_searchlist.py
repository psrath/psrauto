import random
import string
from builtins import print

import pytest
from src.SearchList import SeachList


@pytest.mark.TestSeachListResolve333
class TestSeachListResolve333:
    """Test SearchList Resolve -"""

    # def test_sl_168(self, api_client, common_functions, op_path, dbo):
    #     """TC 176 - Create Dynamic Search List And Update QID with sevirity from 5-1 QID Enable Subscription"""
    #     params = {"confirmed_severities": "5"}
    #     qid_update_params = {"threat_comment": "Updated Threat Comment", "impact_comment": "Updated Impact Comment", "solution_comment": "Updated solution comment"}
    #     sl_id = SeachList.create_dynamic_search_list(api_client, params, "qweb")
    #     print("Created: SL", sl_id)
    #     pre_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qweb"))
    #     qid_to_change = pre_update_res[0]
    #     print("QID picked up for updation :",  qid_to_change)
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "list")
    #     print("\nPre-Updation sevirity level is " + SeachList.get_qid_sevirity(kb_list))
    #     SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "edit", "1", qid_update_params)
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "list")
    #     print("\nPost-Updation sevirity levle is "+SeachList.get_qid_sevirity(kb_list))
    #     pst_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qweb"))
    #     flag = True
    #     if qid_to_change in pst_update_res:
    #         flag = False
    #     assert flag, "Failed..Failed to Update QID"
    #     if flag:
    #         print("Post upgrade Reverting sevirity")
    #         SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qid", "edit", "5")
    #     assert flag, "Failed..Updated QID is present in the SearchList"
    #
    # def test_sl_169(self, api_client, common_functions, op_path, dbo):
    #     """TC 177 - Create Dynamic Search List And Update QID with sevirity from 5-1 QID Disable Subscription"""
    #     params = {"confirmed_severities": "5"}
    #     qid_update_params  = {"threat_comment": "Updated Threat Comment","impact_comment": "Updated Impact Comment", "solution_comment": "Updated solution comment"}
    #     sl_id = SeachList.create_dynamic_search_list(api_client, params, "qid")
    #     print("Created: SL", sl_id)
    #     pre_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qid"))
    #     qid_to_change = pre_update_res[0]
    #     print("QID picked up for updation :",  qid_to_change)
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qid", "list")
    #     print("\nPre-Updation sevirity level is " + SeachList.get_qid_sevirity(kb_list))
    #     SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qid", "edit", "1", qid_update_params)
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qid", "list")
    #     print("\nPost-Updation sevirity levle is "+SeachList.get_qid_sevirity(kb_list))
    #     pst_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qid"))
    #     flag = True
    #     if qid_to_change in pst_update_res:
    #         flag = False
    #     assert flag, "Failed..Failed to Update QID"
    #     if flag:
    #         print("Post upgrade Reverting sevirity")
    #         SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qid", "edit", "5", qid_update_params)
    #     assert flag, "Failed..Updated QID is present in the SearchList"
    #
    # def test_sl_170(self, api_client, common_functions, op_path, dbo):
    #     """TC 178 - Create Dynamic Search List And Update-Reset QID with sevirity from 5-1-5 QID Enable Subscription"""
    #     params = {"confirmed_severities": "5"}
    #     qid_update_params = {"threat_comment": "Updated Threat Comment", "impact_comment": "Updated Impact Comment", "solution_comment": "Updated solution comment"}
    #     sl_id = SeachList.create_dynamic_search_list(api_client, params, "qid")
    #     print("Created: SL", sl_id)
    #     pre_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qid"))
    #     qid_to_change = random.choice(pre_update_res)
    #     print("QID picked up for updation :",  qid_to_change)
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qid", "list")
    #     pre_update_sevirity = SeachList.get_qid_sevirity(kb_list)
    #     print("\n###Pre-Updation sevirity level is### " + pre_update_sevirity)
    #     SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qid", "edit", "1", qid_update_params)
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qid", "list")
    #     post_update_sevirity = SeachList.get_qid_sevirity(kb_list)
    #     print("\n###Post-Updation sevirity levle is### "+post_update_sevirity)
    #     pst_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qid"))
    #     flag = True
    #     if qid_to_change in pst_update_res:
    #         flag = False
    #         assert flag, "Failed..Failed to Update QID"
    #     print("Reseting sevirity level of the Updated QID " +qid_to_change)
    #     SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qid", "reset")
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qid", "list")
    #     post_reset_sevirity = SeachList.get_qid_sevirity(kb_list)
    #     print("\n###Post-Reset sevirity level is### " +post_reset_sevirity)
    #     flag = False
    #     if pre_update_sevirity == post_reset_sevirity:
    #         flag = True
    #     assert flag, "Failed..Failed to Update QID"
    #
    # def test_sl_171(self, api_client, common_functions, op_path, dbo):
    #     """TC 179 - Create Dynamic Search List And Update-Reset QID with sevirity from 5-1-5 QID Disable Subscription"""
    #     params = {"confirmed_severities": "5"}
    #     qid_update_params = {"threat_comment": "Updated Threat Comment", "impact_comment": "Updated Impact Comment", "solution_comment": "Updated solution comment"}
    #     sl_id = SeachList.create_dynamic_search_list(api_client, params, "qweb")
    #     print("Created: SL", sl_id)
    #     pre_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qweb"))
    #     qid_to_change = random.choice(pre_update_res)
    #     print("QID picked up for updation :",  qid_to_change)
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "list")
    #     pre_update_sevirity = SeachList.get_qid_sevirity(kb_list)
    #     print("\n###Pre-Updation sevirity level is### " + pre_update_sevirity)
    #     SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "edit", "1",qid_update_params)
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "list")
    #     post_update_sevirity = SeachList.get_qid_sevirity(kb_list)
    #     print("\n###Post-Updation sevirity levle is### "+post_update_sevirity)
    #     pst_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qweb"))
    #     flag = True
    #     if qid_to_change in pst_update_res:
    #         flag = False
    #         assert flag, "Failed..Failed to Update QID"
    #     print("Reseting sevirity level of the Updated QID " +qid_to_change)
    #     SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "reset")
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "list")
    #     post_reset_sevirity = SeachList.get_qid_sevirity(kb_list)
    #     print("\n###Post-Reset sevirity level is### " +post_reset_sevirity)
    #     flag = False
    #     if pre_update_sevirity == post_reset_sevirity:
    #         flag = True
    #     assert flag, "Failed..Failed to Update QID"




    def test_sl_02(self, api_client, common_functions, op_path, dbo):
        """TC 02 - Create Static Search List with Single QID"""
        params = {"qids": "10688"}
        sl_id = SeachList.create_static_search_list(api_client, params,"qweb")
        print("Created: SL", sl_id)
        assert SeachList.verify_qids_static(sl_id, api_client, common_functions,"qweb"), "Invalid QIDs Found"
        SeachList.delete_static_search_list(sl_id, api_client)

    def test_sl_03(self, api_client, common_functions, op_path, dbo):
        """TC 03 - Create Static Search List with Multiple QID"""
        params = {"qids": "10688,12525,11771"}
        sl_id = SeachList.create_static_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids_static(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_static_search_list(sl_id, api_client)

    def test_sl_04(self, api_client, common_functions, op_path, dbo):
        """TC 04 - Create Static Search List with Multiple QID"""
        params = {"qids": "10688,12525,11771,1027-1033,1167-1170"}
        sl_id = SeachList.create_static_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids_static(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_static_search_list(sl_id, api_client)


