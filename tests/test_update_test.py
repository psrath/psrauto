import random
from builtins import print
from src.XmlParser import XmlParser
from src.JsonParser import JsonParser
import pytest
from src.SearchList import SeachList

@pytest.mark.TestSeachListResolve333
class TestSeachListResolve333:
    """Test QID-Service Endpoints-"""
    CVE_ID = 'CVE-2021-36765'
    # def test_CVE_1(self, api_client, common_functions, op_path, dbo):
    #     """TC 1 - Verify CVE Centric API Call"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve":self.CVE_ID,"details":"All","qvsMin":0,"qvsMax":30}
    #     result = str(SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri))
    #     print("API Response\n"+result)
    #     if not result:
    #         test = False
    #     else:
    #         test = True
    #     assert test,"Failed To Get API Response"
    #
    # def test_CVE_2(self, api_client, common_functions, op_path, dbo):
    #     """TC 2 - Verify CVE Centric API Call for IdType"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve":self.CVE_ID,"details":"All","qvsMin":0,"qvsMax":30}
    #     result = str(SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri))
    #     print("API Response\n" + result)
    #     res = JsonParser(result).retrive_value_for_json_key("idType")
    #     dbQuery = "SELECT QVS_TYPE FROM VULN_QVS WHERE QVS_ID='"+self.CVE_ID+"'"
    #     #print(dbQuery)
    #     qvs_type = dbo.execute_query(dbQuery, {})
    #     #print(qvs_type)
    #     qvs_db = ''.join(qvs_type[0])
    #     qvs_api = ''.join(res[0])
    #     print('API-Value::' + qvs_api)
    #     print('DB-Value::' + qvs_db)
    #     assert (qvs_api == qvs_db), "Failed QVS Type Missmatch Between DB and API"
    #
    #
    # def test_CVE_3(self, api_client, common_functions, op_path, dbo):
    #     """TC 3 - Verify CVE Centric API Call With CVE-ID"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve":self.CVE_ID,"details":"All","qvsMin":0,"qvsMax":30}
    #     result = SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri)
    #     res = JsonParser(result).retrive_value_for_json_key("id")
    #     dbQuery = "SELECT QVS_ID FROM VULN_QVS WHERE QVS_ID='"+self.CVE_ID+"'"
    #     cve_id = dbo.execute_query(dbQuery, {})
    #     cve_db = ''.join(cve_id[0])
    #     cve_api = ''.join(res[0])
    #     print('API-Value'+cve_api)
    #     print('DB-Value'+cve_db)
    #     assert (cve_api == cve_db),"Failed CVE ID Missmatch Between DB and API"
    #
    # def test_CVE_4(self, api_client, common_functions, op_path, dbo):
    #     """TC 4 - Verify CVE Centric API Call With QVS_SCORE"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve":self.CVE_ID,"details":"All","qvsMin":0,"qvsMax":30}
    #     result = SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri)
    #     res = JsonParser(result).retrive_value_for_json_key("qvs")
    #     dbQuery = "SELECT QVS_SCORE FROM VULN_QVS WHERE QVS_ID='"+self.CVE_ID+"'"
    #     cve_id = dbo.execute_query(dbQuery, {})
    #     print(cve_id)
    #     cve_db = ''.join(map(str,(cve_id[0])))
    #     cve_api = ''.join(res[0])
    #     print('API-Value::'+cve_api)
    #     print('DB::Value'+cve_db)
    #     assert (cve_api == cve_db),"Failed QVS Score Missmatch Between DB and API"
    #
    # def test_CVE_5(self, api_client, common_functions, op_path, dbo):
    #     """TC 5 - Verify CVE Centric API Call With LAST_CHANGE_DATE"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve": self.CVE_ID, "details": "All", "qvsMin": 0, "qvsMax": 30}
    #     result = SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri)
    #     res = JsonParser(result).retrive_value_for_json_key("qvsLastChangedDate")
    #     strRes = ''.join([str(items) for items in res])
    #     dbQuery = "SELECT MODIFIED_ON FROM VULN_QVS WHERE QVS_ID='" + self.CVE_ID + "'"
    #     cve_id = dbo.execute_query(dbQuery, {})
    #     cve_db = ''.join(map(str, (cve_id[0])))
    #     print('API-Value::' + strRes)
    #     print('DB::Value' + cve_db)
    #     assert (strRes == cve_db), "Failed::Last ChangeDate Missmatch Between DB and API"
    #
    # def test_CVE_6(self, api_client, common_functions, op_path, dbo):
    #     """TC 6 - Verify CVE Centric API Call With PUBLISHED DATE"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve": self.CVE_ID, "details": "All", "qvsMin": 0, "qvsMax": 30}
    #     result = SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri)
    #     res = JsonParser(result).retrive_value_for_json_key("nvdPublishedDate")
    #     strRes = ''.join([str(items) for items in res])
    #     dbQuery = "SELECT PUBLISHED_ON FROM VULN_QVS WHERE QVS_ID='" + self.CVE_ID + "'"
    #     cve_id = dbo.execute_query(dbQuery, {})
    #     cve_db = ''.join(map(str, (cve_id[0])))
    #     print('API-Value::' + strRes)
    #     print('DB::Value' + cve_db)
    #     assert (strRes == cve_db), "Failed::Last Published Date Missmatch Between DB and API"
    #
    # def test_CVE_7(self, api_client, common_functions, op_path, dbo):
    #     """TC 7 - Verify CVE Centric API Call With Contributing Factor CVSS"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve": self.CVE_ID, "details": "All", "qvsMin": 0, "qvsMax": 30}
    #     result = SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri)
    #     res = JsonParser(result).key_exists_in_json("cvss")
    #     print("Result::{}".format(res))
    #     assert res, "Failed::Contributing Factor CVSS missing in API response"
    #
    # def test_CVE_8(self, api_client, common_functions, op_path, dbo):
    #     """TC 8 - Verify CVE Centric API Call With Contributing Factor cvssVersion"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve": self.CVE_ID, "details": "All", "qvsMin": 0, "qvsMax": 30}
    #     result = SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri)
    #     res = JsonParser(result).key_exists_in_json("cvssVersion")
    #     print("Result::{}".format(res))
    #     assert res, "Failed::Contributing Factor cvssVersion missing in API response"
    #
    # def test_CVE_9(self, api_client, common_functions, op_path, dbo):
    #     """TC 9 - Verify CVE Centric API Call With qvsMin value"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve": self.CVE_ID, "details": "All", "qvsMin": 0}
    #     result = SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri)
    #     res = JsonParser(result).key_exists_in_json("qvs")
    #     print("Result::{}".format(res))
    #     assert res, "Failed::qvsMin is missing in API response"
    #
    # def test_CVE_10(self, api_client, common_functions, op_path, dbo):
    #     """TC 10 - Verify CVE Centric API Call With qvsMax value"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve": self.CVE_ID, "details": "All", "qvsMax": 100}
    #     result = SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri)
    #     res = JsonParser(result).key_exists_in_json("qvs")
    #     print("Result::{}".format(res))
    #     assert res, "Failed::qvsMax is missing in API response"
    #
    # def test_CVE_11(self, api_client, common_functions, op_path, dbo):
    #     """TC 11 - Verify CVE Centric API Call validation qvsMin>qvsMax value"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve": self.CVE_ID, "details": "All","qvsMin": 100, "qvsMax": 0}
    #     result = str(SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri))
    #     res = JsonParser(result).retrive_value_for_json_key("error")
    #     print("Error-Message::{}".format(res))
    #     strRes = ''.join([str(items) for items in res])
    #     if "qvsMin cannot be greater than qvsMax" in strRes:
    #         res = True
    #     else:
    #         res = False
    #     assert res ,"Validation failed for qvsMin>qvsMax"
    #
    # def test_CVE_12(self, api_client, common_functions, op_path, dbo):
    #     """TC 12 - Verify CVE Centric API Call mandatory param validation Details value"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve": self.CVE_ID, "details": "","qvsMin": 0, "qvsMax": 100}
    #     result = str(SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri))
    #     res = JsonParser(result).retrive_value_for_json_key("error")
    #     print("Error-Message::{}".format(res))
    #     strRes = ''.join([str(items) for items in res])
    #     if "Invalid Details parameter in the request. Allowed Values are Basic|All" in strRes:
    #         res = True
    #     else:
    #         res = False
    #     assert res ,"Validation failed for param Details"
    #
    # def test_CVE_13(self, api_client, common_functions, op_path, dbo):
    #     """TC 13 - Verify CVE Centric API Call mandatory param validation Details-CVE-ID"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve": "", "details": "All","qvsMin": 0, "qvsMax": 100}
    #     result = str(SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri))
    #     res = JsonParser(result).retrive_value_for_json_key("message")
    #     print("Error-Message::{}".format(res))
    #     strRes = ''.join([str(items) for items in res])
    #     if "Validation failed for object='cveCentricRequest'" in strRes:
    #         res = True
    #     else:
    #         res = False
    #     assert res ,"Validation failed for CVE-ID"
    # def test_CVE_13(self, api_client, common_functions, op_path, dbo):
    #     """TC 13 - Verify CVE Centric API Call param validation between qvsMin and qvsMax value"""
    #     uri = "/qvs/1.0/search"
    #     params = {"cve": self.CVE_ID, "details": "All","qvsMin": 0, "qvsMax": 10}
    #     result = str(SeachList.verify_qid_service_CVE_call(api_client, common_functions, params, uri))
    #     print(f'API-response{result}')
    #     if self.CVE_ID not in result:
    #         res = True
    #     else:
    #         res = False
    #     assert res ,"Validation failed with wrong cvsMin and cvsMax value"

    def test_sl_14(self, api_client, common_functions, op_path, dbo):
        """TC 14 - Verify QID-Service look up with Scope as Basic"""
        qids = "119088"
        uri = "/qid/1.0/"
        params = {"qid": qids, "scope": "Basic"}
        result = SeachList.verify_qid_service_API_call(api_client,common_functions,params,uri)
        print(result)
        res1 = JsonParser(result).retrive_value_for_json_key("id")
        res2 = JsonParser(result).retrive_value_for_json_key("source")
        #print(f'{res}')
        api_qid = ''.join([str(items) for items in res1])
        source = ''.join([str(items) for items in res2])
        print("QID::",api_qid," Source::",source)
        #print(source)
        if (qids == api_qid) and (source == 'QUALYS'):
             flag = True
             print("Validation Pass for QID-LookUP")
        else:
             flag = False
        assert flag, "Issue with service call"



    # def test_sl_04(self, api_client, common_functions, op_path, dbo):
    #     """TC 04 - Create Dynamic Search List with Discovery Methods - All"""
    #     params = {"discovery_methods": "ALL"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created: SL-QWEB", sl_id_qweb)
    #     sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    #     print("Created: SL-Service", sl_id_service)
    #     assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client,common_functions), "Invalid QIDs Found"
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #     SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')
    #
    # def test_sl_03(self, api_client, common_functions, op_path, dbo):
    #     """TC 03 - Create Dynamic Search List with Discovery Methods - "Remote_Authenticated"""
    #     params = {"discovery_methods": "Remote,Authenticated"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created: SL-QWEB", sl_id_qweb)
    #     sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    #     print("Created: SL-Service", sl_id_service)
    #     assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qid')
    #
    # def test_sl_02(self, api_client, common_functions, op_path, dbo):
    #     """TC 02 - Create Dynamic Search List with Discovery Methods - Remote"""
    #     params = {"discovery_methods": "Remote"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created: SL-QWEB", sl_id_qweb)
    #     sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    #     print("Created: SL-Service", sl_id_service)
    #     assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
    #     #SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #     #SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')
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
    #
    # def test_sl_15(self, api_client, common_functions, op_path, dbo):
    #     """TC 01 - Create Dynamic Search List with All Supported Modules"""
    #     params = {"supported_modules": "VM, CA-Windows Agent, CA-Linux Agent, CA-Mac Agent, CA-AIX Agent, CA-BSD Agent, CA-Solaris Agent, WAS, WAF, MD, SEM-Android, API Security, SEM-IOS,ICS"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created: SL-QWEB", sl_id_qweb)
    #     sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    #     print("Created: SL-Service", sl_id_service)
    #     assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #     SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')
    #
    # def test_sl_255(self, api_client, common_functions, op_path, dbo):
    #     """TC 01 - Create Dynamic Search List with Supported Modules"""
    #     params = {"supported_modules": "ICS"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created: SL-QWEB", sl_id_qweb)
    #     sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    #     print("Created: SL-Service", sl_id_service)
    #     assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #     SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')
    #
    # def test_sl_04(self, api_client, common_functions, op_path, dbo):
    #     """TC 03 - Dynamic Search List Create/Update/Delete WIth QID Update/Reset for Service Disable Subscription"""
    #     params = {"confirmed_severities": "5"}
    #     qid_update_params = {"threat_comment": "Updated Threat Comment", "impact_comment": "Updated Impact Comment",
    #                          "solution_comment": "Updated solution comment"}
    #     sl_id = SeachList.create_dynamic_search_list(api_client, params, "qweb")
    #     print("Created: QWEB-SL", sl_id)
    #     pre_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qweb"), "qweb")
    #     qid_to_change = random.choice(pre_update_res)
    #     print("QID picked up for updation ::::::", qid_to_change)
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "list")
    #     print("\nPre-Updation sevirity level is ::::::" + SeachList.get_qid_sevirity(kb_list))
    #     SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "edit", "1", qid_update_params)
    #     kb_list = SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "list")
    #     print("\nPost-Updation sevirity levle is ::::::" + SeachList.get_qid_sevirity(kb_list))
    #     pst_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qweb"), "qweb")
    #     flag = True
    #     if qid_to_change in pst_update_res:
    #         flag = False
    #     assert flag, "Failed..Failed to Update QID"
    #     if flag:
    #         print("Post upgrade Reverting sevirity::::")
    #         SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "reset")
    #         print("\nReset sevirity levle is ::::" + SeachList.get_qid_sevirity(kb_list))
    #     assert flag, "Failed..Updated QID is present in the SearchList"
    #     print("Deleting SL" + sl_id)
    #     SeachList.delete_dynamic_search_list(sl_id, api_client, 'qweb')
    #
    # def test_sl_152(self, api_client, common_functions, op_path, dbo):
    #     """TC 160 - Create Dynamic Search List with Supported Modules VM-Scanner"""
    #     params = {"supported_modules": "VM-Scanner"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created: SL-QWEB", sl_id_qweb)
    #     sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    #     print("Created: SL-Service", sl_id_service)
    #     assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #     SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')
    #
    # def test_sl_01(self, api_client, common_functions, op_path, dbo):
    #     """TC 01 - Create QWEB-Dynamic Search List with Discovery Methods - Authenticated"""
    #     params = {"discovery_methods": "Authenticated"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created Successfully: SL-QWEB ", sl_id_qweb)
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #
    # def test_sl_02(self, api_client, common_functions, op_path, dbo):
    #     """TC 02 - Create QWEB-Dynamic Search List with Discovery Methods - Remote"""
    #     params = {"discovery_methods": "Remote"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created Successfully: SL-QWEB", sl_id_qweb)
    #     print("Deleting create dynamic SL")
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #
    # def test_sl_03(self, api_client, common_functions, op_path, dbo):
    #     """TC 03 - Create QWEB-Dynamic Search List with Discovery Methods - "Remote_Authenticated"""
    #     params = {"discovery_methods": "Remote,Authenticated"}
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    #     print("Created Successfully: SL-QWEB", sl_id_qweb)
    #     print("Deleting the created Searchlist")
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #
    #
    # def test_sl_04(self, api_client, common_functions, op_path, dbo):
    #     """TC 04 - Dynamic Search List Create/Update/Delete WIth QID Update/Reset for Service Disable Subscription"""
    #     params = {"confirmed_severities": "5"}
    #     qid_update_params = {"threat_comment": "Updated Threat Comment", "impact_comment": "Updated Impact Comment", "solution_comment": "Updated solution comment"}
    #     sl_id = SeachList.create_dynamic_search_list(api_client, params, "qweb")
    #     print("Created Successfully: SL-QWEB", sl_id)
    #     pre_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qweb"))
    #     qid_to_change = random.choice(pre_update_res)
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
    #         SeachList.qid_update_or_list_reset(api_client, qid_to_change, "qweb", "edit", "5")
    #     assert flag, "Failed..Updated QID is present in the SearchList"
    #     print("Deleting SL" +sl_id)
    #     SeachList.delete_dynamic_search_list(sl_id, api_client, 'qweb')
    #
    # def test_sl_05(self, api_client, common_functions, op_path, dbo):
    #     """TC 05 - Dynamic Search List Create/Update/Delete WIth QID Update/Reset for Service Enable Subscription"""
    #     params = {"confirmed_severities": "5"}
    #     qid_update_params  = {"threat_comment": "Updated Threat Comment","impact_comment": "Updated Impact Comment", "solution_comment": "Updated solution comment"}
    #     sl_id = SeachList.create_dynamic_search_list(api_client, params, "qid")
    #     print("Created Successfully: SL-QID-service", sl_id)
    #     pre_update_res = SeachList.get_qid_list_from_xml(SeachList.get_qweb_search_list(api_client, sl_id, "qid"))
    #     qid_to_change = random.choice(pre_update_res)
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
    #     print("Deleting SL" + sl_id)
    #     SeachList.delete_dynamic_search_list(sl_id, api_client, 'qid')
    #
    # def test_sl_06(self, api_client, common_functions, op_path, dbo):
    #     """TC 06 - Create Dynamic Search List Create/Update/Delete And Update-Reset QID for QID Enable Subscription"""
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
    #     print("Deleting SL" + sl_id)
    #     SeachList.delete_dynamic_search_list(sl_id, api_client, 'qid')
    #
    # def test_sl_07(self, api_client, common_functions, op_path, dbo):
    #     """TC 07 - Create Dynamic Search List Create/Update/Delete And Update-Reset QID for QID Disable Subscription"""
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
    #     print("Deleting SL" + sl_id)
    #     SeachList.delete_dynamic_search_list(sl_id, api_client, 'qweb')
    #     print("Deleting SL" + sl_id)
    #     SeachList.delete_dynamic_search_list(sl_id, api_client, 'qweb')


    # def test_sl_08(self, api_client, common_functions, op_path, dbo):
    #     """TC 08 - Create QWEB Static Search List with Single QID"""
    #     no_of_QID = []
    #     params = {"qids": "105741"}
    #     no_of_QID = (params.get("qids")).split(',')
    #     sl_id = SeachList.create_static_search_list(api_client, params,"qweb")
    #     print("Created: SL", sl_id)
    #     count = SeachList.list_static_search_list(api_client,sl_id,"qweb")
    #     #print("Count of QID " +str(count))
    #
    #     if count == len(no_of_QID):
    #         flag = True
    #     else:
    #         flag = False
    #         print("Count of QID " + str(count))
    #     assert flag, "Invlid QID found"
    #     SeachList.delete_static_search_list(api_client,sl_id,"qweb")
    #
    # def test_sl_09(self, api_client, common_functions, op_path, dbo):
    #     """"TC 09 - Create QWEB Static Search List with Single QID"""
    #     no_of_QID = []
    #     params = {"qids": "87437"}
    #     no_of_QID = (params.get("qids")).split(',')
    #     sl_id = SeachList.create_static_search_list(api_client, params, "qweb")
    #     print("Created: SL", sl_id)
    #     count = SeachList.list_static_search_list(api_client, sl_id, "qweb")
    #     # print("Count of QID " +str(count))
    #     if count == len(no_of_QID):
    #         flag = True
    #     else:
    #         flag = False
    #         print("Count of QID " + str(count))
    #     assert flag, "Invlid QID found"
    #
    # def test_sl_10(self, api_client, common_functions, op_path, dbo):
    #     """TC 10 - Update QWEB Static Search List with Add QIDS"""
    #     no_of_QID_Before_Update = []
    #     no_of_QID_After_Update = []
    #     params = {"qids": "10688"}
    #     no_of_QID_Before_Update = (params.get("qids")).split(',')
    #     sl_id = SeachList.create_static_search_list(api_client, params, "qweb")
    #     update_params = {"add_qids": "38103,166684,236884"}
    #     no_of_QID_After_Update = no_of_QID_Before_Update.append((update_params.get("add_qids")).split(','))
    #     SeachList.update_static_search_list(api_client,update_params,sl_id,"qweb")
    #     print("Created: SL", sl_id)
    #     count = SeachList.list_static_search_list(api_client,sl_id,"qweb")
    #     print("Count of QID " +str(count))
    #
    #     if count == len(no_of_QID_After_Update):
    #         flag = True
    #     else:
    #         flag = False
    #         print("Count of QID " + str(count))
    #     assert flag, "Invlid QID found"
    #
    # def test_sl_11(self, api_client, common_functions, op_path, dbo):
    #     """"TC 11 - Create QWEB Static Search List with multiple QIDs"""
    #     no_of_QID = []
    #     params = {"qids": "10688,12525,11771,198350,177131,105648"}
    #     no_of_QID = (params.get("qids")).split(',')
    #     sl_id = SeachList.create_static_search_list(api_client, params, "qweb")
    #     print("Created: SL", sl_id)
    #     count = SeachList.list_static_search_list(api_client, sl_id, "qweb")
    #     # print("Count of QID " +str(count))
    #     if count == len(no_of_QID):
    #         flag = True
    #     else:
    #         flag = False
    #         print("Count of QID " + str(count))
    #     assert flag, "Invlid QID found"
    #     SeachList.delete_static_search_list(api_client,sl_id,"qweb")
    #
    # def test_sl_12(self, api_client, common_functions, op_path, dbo):
    #     """"TC 12 - Create QWEB Static Search List with multiple + range QIDs"""
    #     no_of_QID = []
    #     params = {"qids": "10688,12525,11771,1027-1033,1167-1170"}
    #     #no_of_QID = (params.get("qids")).split(',')
    #     sl_id = SeachList.create_static_search_list(api_client, params, "qweb")
    #     print("Created: SL", sl_id)
    #     #count = SeachList.list_static_search_list(api_client, sl_id, "qweb")
    #     # print("Count of QID " +str(count))
    #     if sl_id != "null":
    #         flag = True
    #     else:
    #         flag = False
    #     assert flag, "Static serachlist creation error"
    #     SeachList.delete_static_search_list(api_client,sl_id,"qweb")
    # def test_sl_13(self, api_client, common_functions, op_path, dbo):
    #     """TC 13 - Verify QID look up with Scope as Basic"""
    #     qids = "119088"
    #     uri = "/qid/1.0/"
    #     params = {"qid": qids, "scope": "Basic"}
    #     result = SeachList.verify_qid_service_API_call(api_client,common_functions,params,uri)
    #     print(result)
    #     if qids in result:
    #         flag = True
    #     else:
    #         print(result.text)
    #     assert flag, "Issue with service call"
    # def test_sl_14(self, api_client, common_functions, op_path, dbo):
    #     """TC 14 - Verify QID look up with Scope as All"""
    #     qids = "119088"
    #     uri = "/qid/1.0/"
    #     params = {"qid": qids, "scope": "All"}
    #     result = SeachList.verify_qid_service_API_call(api_client,common_functions,params,uri)
    #     print(result)
    #     if qids in result:
    #         flag = True
    #     else:
    #         print(result.text)
    #     assert flag, "Issue with QID Look up service call"

    # def test_sl_15(self, api_client, common_functions, op_path, dbo):
    #     """TC 15 - Verify Dynamic SL-Resolved call"""
    #     params_sl = {"discovery_methods": "Authenticated"}
    #     uri = "/searchlist/1.0/resolve/"
    #     sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params_sl, 'qid')
    #     params_service = {"searchListId": sl_id_qweb}
    #     result = SeachList.verify_qid_service_API_call(api_client, common_functions, params_service, uri)
    #     if "data" in result:
    #         flag = True
    #     else:
    #         print(result.text)
    #     assert flag, "Issue with QID Resolve service call"
    #     SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    #
    # def test_sl_16(self, api_client, common_functions, op_path, dbo):
    #     """TC 16 - Verify Dynamic SL-pageResolved call with dynamic SL"""
    #     flag = False
    #     params_sl = {"discovery_methods": "Authenticated"}
    #     uri = "/searchlist/1.0/resolve/paged/"
    #     sl_id_qid = SeachList.create_dynamic_search_list(api_client, params_sl, 'qid')
    #     print("Create Searchlist::"+sl_id_qid)
    #     params_service = {"limit": "1000", "offset": "1003", "searchListId": sl_id_qid}
    #     result = SeachList.verify_qid_service_API_call(api_client, common_functions, params_service, uri)
    #     if "data" in result:
    #         flag = True
    #     else:
    #         print(result.text)
    #
    #     assert flag, "Issue with QID Resolve service call"
    #     SeachList.delete_dynamic_search_list(sl_id_qid, api_client, 'qid')
