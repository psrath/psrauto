import random
import string
from builtins import print

import pytest
from src.SearchList import SeachList


@pytest.mark.TestSeachListResolve345
class TestSeachListResolve345:
    """Test SearchList Resolve -"""
    def test_sl_03(self, api_client, common_functions, op_path, dbo):
        """TC 03 - Create Dynamic Search List with Discovery Methods - "Remote_Authenticated"""
        params = {"discovery_methods": "Remote,Authenticated"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qid')

    def test_sl_37(self, api_client, common_functions, op_path, dbo):
        """TC 38 - Create Dynamic Search List with Categories Type OVAL"""
        params = {"categories": "OVAL"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_40(self, api_client, common_functions, op_path, dbo):
        """TC 41 - Create Dynamic Search List with Categories Type QRDI"""
        params = {"categories": "QRDI"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_59(self, api_client, common_functions, op_path, dbo):
        """TC 61 - Create Dynamic Search List with Categories Type CVE ID not in"""
        params = {"cve_ids": "CVE-2016-4459,CVE-2018-10194", "not_cve_ids": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')


    def test_sl_79(self, api_client, common_functions, op_path, dbo):
        """TC 81 - Create Dynamic Search List with Not Vendor Reference CISCO"""
        params = {"not_vendor_refs": "1", "vendor_refs": "cisco-sa-20180926-ptp"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_80(self, api_client, common_functions, op_path, dbo):
        """TC 82 - Create Dynamic Search List with Not Vendor Reference CISCO"""
        params = {"not_vendor_refs": "1", "vendor_refs": "cisco-sa-20180926-ptp"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_81(self, api_client, common_functions, op_path, dbo):
        """TC 83 - Create Dynamic Search List with Not Vendor Reference CISCO"""
        params = {"not_vendor_refs": "1", "vendor_refs": "cisco-sa-20180926-ptp"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_82(self, api_client, common_functions, op_path, dbo):
        """TC 84 - Create Dynamic Search List with Vendor Reference CVSS Base Score"""
        params = {"cvss_base_operand": "1", "cvss_base": "6"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_83(self, api_client, common_functions, op_path, dbo):
        """TC 85 - Create Dynamic Search List with Vendor Reference CVSS Base Score"""
        params = {"cvss_base_operand": "2", "cvss_base": "6"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_87(self, api_client, common_functions, op_path, dbo):
        """TC 89 - Create Dynamic Search List with Vendor Reference CVSS Base Score Temporal"""
        params = {"cvss3_temp_operand": "2", "cvss3_temp": "8"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_92(self, api_client, common_functions, op_path, dbo):
        """TC 94 - Create Dynamic Search List with Not BugTrack ID"""
        params = {"bugtraq_id": "105108", "not_bugtraq_id": "1"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_95(self, api_client, common_functions, op_path, dbo):
        """TC 97 - Create Dynamic Search List with Service Modified in previous month"""
        params = {"service_modified_date_in_previous": "Month"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_99(self, api_client, common_functions, op_path, dbo):
        """TC 101 - Create Dynamic Search List with Service Modified date within last days"""
        params = {"service_modified_date_within_last_days": "60"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_100(self, api_client, common_functions, op_path, dbo):
        """TC 102 - Create Dynamic Search List with Service Modified date between"""
        params = {"service_modified_date_between": "01/01/2018-10/15/2019"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_101(self, api_client, common_functions, op_path, dbo):
        """TC 103 - Create Dynamic Search List with Service Modified not Today"""
        params = {"not_service_modified_flag": "1", "service_modified_date_today": "1"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_102(self, api_client, common_functions, op_path, dbo):
        """TC 104 - Create Dynamic Search List with Service Modified in not previous year"""
        params = {"not_service_modified_flag": "1", "service_modified_date_in_previous": "Year"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_103(self, api_client, common_functions, op_path, dbo):
        """TC 105 - Create Dynamic Search List with Service Modified in not previous month"""
        params = {"not_service_modified_flag": "1", "service_modified_date_in_previous": "Month"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_104(self, api_client, common_functions, op_path, dbo):
        """TC 106 - Create Dynamic Search List with Service Modified not in previous Week"""
        params = {"not_service_modified_flag": "1", "service_modified_date_in_previous": "Week"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_107(self, api_client, common_functions, op_path, dbo):
        """TC 109 - Create Dynamic Search List with User Modified in previous month"""
        params = {"user_modified_date_in previous": "Month"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_108(self, api_client, common_functions, op_path, dbo):
        """TC 110 - Create Dynamic Search List with User Modified Week"""
        params = {"user_modified_date_in previous": "Week"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')


    def test_sl_111(self, api_client, common_functions, op_path, dbo):
        """TC 113 - Create Dynamic Search List with User Modified date within last days"""
        params = {"user_modified_date_within_last_days": "60"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_113(self, api_client, common_functions, op_path, dbo):
        """TC 115 - Create Dynamic Search List with QID Modified not Today"""
        params = {"not_published_flag": "1", "published_date_today": "1"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_114(self, api_client, common_functions, op_path, dbo):
        """TC 116 - Create Dynamic Search List with QID Modified in not previous year"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Year"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')


    def test_sl_115(self, api_client, common_functions, op_path, dbo):
        """TC 117 - Create Dynamic Search List with QID Modified in not previous month"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Month"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_116(self, api_client, common_functions, op_path, dbo):
        """TC 118 - Create Dynamic Search List with QID Modified not in previous Week"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Week"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_117(self, api_client, common_functions, op_path, dbo):
        """TC 119 - Create Dynamic Search List with QID Modified Not in previous quarter"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Quarter"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_118(self, api_client, common_functions, op_path, dbo):
        """TC 120 - Create Dynamic Search List with QID Modified Not in previous year"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Year"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_119(self, api_client, common_functions, op_path, dbo):
        """TC 130 - Create Dynamic Search List with QID Modified NOT date within last 60 days"""
        params = {"not_published_flag": "1", "published_date_within_last_days": "60"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_120(self, api_client, common_functions, op_path, dbo):
        """TC 131 - Create Dynamic Search List with QID Modified  NOt date between"""
        params = {"not_published_flag": "1", "published_date_between": "01/01/2018-01/15/2019"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_123(self, api_client, common_functions, op_path, dbo):
        """TC 134 - Create Dynamic Search List with QID Published Modified in previous month"""
        params = {"published_date_in_previous": "Month"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')


    def test_sl_127(self, api_client, common_functions, op_path, dbo):
        """TC 138 - Create Dynamic Search List with QID published  date within last 60 days"""
        params = {"published_date_within_last_days": "9999"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_129(self, api_client, common_functions, op_path, dbo):
        """TC 140 - Create Dynamic Search List with QID Modified not Today"""
        params = {"not_published_flag": "1", "published_date_today": "1"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')


    def test_sl_130(self, api_client, common_functions, op_path, dbo):
        """TC 141 - Create Dynamic Search List with QID Modified in not previous year"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Year"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')


    def test_sl_131(self, api_client, common_functions, op_path, dbo):
        """TC 142 - Create Dynamic Search List with QID Modified in not previous month"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Month"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_132(self, api_client, common_functions, op_path, dbo):
        """TC 143 - Create Dynamic Search List with QID Modified not in previous Week"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Week"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_133(self, api_client, common_functions, op_path, dbo):
        """TC 144 - Create Dynamic Search List with QID Modified not Today"""
        params = {"not_published_flag": "1", "published_date_today": "1"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')


    def test_sl_134(self, api_client, common_functions, op_path, dbo):
        """TC 145 - Create Dynamic Search List with QID Modified in not previous year"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Year"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_135(self, api_client, common_functions, op_path, dbo):
        """TC 146 - Create Dynamic Search List with User Modified in not previous month"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Month"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_136(self, api_client, common_functions, op_path, dbo):
        """TC 148 - Create Dynamic Search List with QID Modified Not in previous quarter"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Quarter"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_137(self, api_client, common_functions, op_path, dbo):
        """TC 149 - Create Dynamic Search List with qid Modified Not in previous year"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Year"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_138(self, api_client, common_functions, op_path, dbo):
        """TC 150 - Create Dynamic Search List with QID Modified NOT date within last 60 days"""
        params = {"not_published_flag": "1", "published_date_within_last_days": "60"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_139(self, api_client, common_functions, op_path, dbo):
        """TC 151 - Create Dynamic Search List with QID Modified  NOt date between"""
        params = {"not_published_flag": "1", "published_date_between": "01/01/2018-01/15/2019"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_140(self, api_client, common_functions, op_path, dbo):
        """TC 152 - Create Dynamic Search List with confirmed sevirity"""
        params = {"confirmed_severities": "1,2,3,4,5"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_145(self, api_client, common_functions, op_path, dbo):
        """TC 153 - Create Dynamic Search List with confirmed sevirity"""
        params = {"confirmed_severities": "1,2,3"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_146(self, api_client, common_functions, op_path, dbo):
        """TC 154 - Create Dynamic Search List with vendor"""
        params = {"vendor_ids": "3"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_147(self, api_client, common_functions, op_path, dbo):
        """TC 155 - Create Dynamic Search List with Not vendor"""
        params = {"not_vendor_ids": "1"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_148(self, api_client, common_functions, op_path, dbo):
        """TC 156 - Create Dynamic Search List with Products actobat,adobe,chrome,dbus"""
        params = {"products": "acrobat,adobe_air,chrome,dbus,enterprise_linux,.net_framework"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_149(self, api_client, common_functions, op_path, dbo):
        """TC 157 - Create Dynamic Search List with Not 2 Products"""
        params = {"not_products": "1", "products": "4500_switch_50-port,.net_framework"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_150(self, api_client, common_functions, op_path, dbo):
        """TC 158 - Create Dynamic Search List with Not Products"""
        params = {"not_products": "1", "products": "4500_switch_50-port"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_151(self, api_client, common_functions, op_path, dbo):
        """TC 159 - Create Dynamic Search List with Vuln Details"""
        params = {"vuln_details": "Security Fixes: Mozilla"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_152(self, api_client, common_functions, op_path, dbo):
        """TC 160 - Create Dynamic Search List with Supported Modules"""
        params = {"supported_modules": "VM,CA-Windows Agent,CA-Linux Agent,WAS,WAF,MD,CA-Mac Agent,CA-AIX Agent"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_153(self, api_client, common_functions, op_path, dbo):
        """TC 161 - Create Dynamic Search List with PCI Compliance"""
        params = {"compliance_types": "PCI"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_154(self, api_client, common_functions, op_path, dbo):
        """TC 162 - Create Dynamic Search List with CobiT Compliance"""
        params = {"compliance_types": "CobIT"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_155(self, api_client, common_functions, op_path, dbo):
        """TC 163 - Create Dynamic Search List with HIPPA Compliance"""
        params = {"compliance_types": "HIPAA"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_156(self, api_client, common_functions, op_path, dbo):
        """TC 164 - Create Dynamic Search List with GLBA  Compliance"""
        params = {"compliance_types": "GLBA"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_157(self, api_client, common_functions, op_path, dbo):
        """TC 165 - Create Dynamic Search List with SOX  Compliance"""
        params = {"compliance_types": "SOX"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client,  common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_158(self, api_client, common_functions, op_path, dbo):
        """TC 166 - Create Dynamic Search List with Qualys Top Internal 20  Compliance"""
        params = {"qualys_top_lists": "Internal_10"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_159(self, api_client, common_functions, op_path, dbo):
        """TC 167 - Create Dynamic Search List with Qualys Top External 10  Compliance"""
        params = {"qualys_top_lists": "External_10"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_160(self, api_client, common_functions, op_path, dbo):
        """TC 168 - Create Dynamic Search List with Qualys Top Internal and External 10  Compliance"""
        params = {"qualys_top_lists": "Internal_10,External_10"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_161(self, api_client, common_functions, op_path, dbo):
        """TC 169 - Create Dynamic Search List with provider Amazon  Compliance"""
        params = {"vuln_provider": "Amazon"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_162(self, api_client, common_functions, op_path, dbo):
        """TC 170 - Create Dynamic Search List with provider Apple  Compliance"""
        params = {"vuln_provider": "Apple"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_163(self, api_client, common_functions, op_path, dbo):
        """TC 171 - Create Dynamic Search List with provider iDefence  Compliance"""
        params = {"vuln_provider": "iDefense"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_164(self, api_client, common_functions, op_path, dbo):
        """TC 172 - Create Dynamic Search List with provider win2k3  Compliance"""
        params = {"vuln_provider": "Windows 2003 Extended Support"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_165(self, api_client, common_functions, op_path, dbo):
        """TC 173 - Create Dynamic Search List with Categories Type AIX"""
        params = {"categories": "AIX"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_166(self, api_client, common_functions, op_path, dbo):
        """TC 174 - Create Dynamic Search List with Categories Type RedHat"""
        params = {"categories": "RedHat"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

    def test_sl_167(self, api_client, common_functions, op_path, dbo):
        """TC 175 - Create Dynamic Search List with QID Modified not in previous Week"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Week"}
        sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
        print("Created: SL-QWEB", sl_id_qweb)
        sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
        print("Created: SL-Service", sl_id_service)
        assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
        SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')


