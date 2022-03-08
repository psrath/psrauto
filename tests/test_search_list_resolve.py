import random
import string
import pytest
from src.SearchList import SeachList


@pytest.mark.TestSeachListResolve
class TestSeachListResolve:
    """Test SearchList Resolve -"""
    def test_sl_01(self, api_client, common_functions, op_path, dbo):
        """TC 01 - Create Dynamic Search List with Discovery Methods - Remote"""
        params = {"discovery_methods": "Remote"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_02(self, api_client, common_functions, op_path, dbo):
        """TC 02 - Create Dynamic Search List with Discovery Methods - Authenticated"""
        params = {"discovery_methods": "Authenticated"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_03(self, api_client, common_functions, op_path, dbo):
        """TC 03 - Create Dynamic Search List with Discovery Methods - "Remote_Authenticated"""
        params = {"discovery_methods": "Remote,Authenticated"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_04(self, api_client, common_functions, op_path, dbo):
        """TC 04 - Create Dynamic Search List with Discovery Methods - All"""
        params = {"discovery_methods": "ALL"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_05(self, api_client, common_functions, op_path, dbo):
        """TC 05 - Create Dynamic Search List with Authentication Type DB2"""
        params = {"auth_types": "DB2"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_06(self, api_client, common_functions, op_path, dbo):
        """TC 06 - Create Dynamic Search List with Authentication Type HTTP"""
        params = {"auth_types": "HTTP"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_07(self, api_client, common_functions, op_path, dbo):
        """TC 07 - Create Dynamic Search List with Authentication Type mysql"""
        params = {"auth_types": "MySQL"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_08(self, api_client, common_functions, op_path, dbo):
        """TC 08 - Create Dynamic Search List with Authentication Type ORACLE"""
        params = {"auth_types": "Oracle"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_09(self, api_client, common_functions, op_path, dbo):
        """TC 09 - Create Dynamic Search List with Authentication Type SNMP"""
        params = {"auth_types": "SNMP"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_10(self, api_client, common_functions, op_path, dbo):
        """TC 10 - Create Dynamic Search List with Authentication Type UNIX"""
        params = {"auth_types": "Unix"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_11(self, api_client, common_functions, op_path, dbo):
        """TC 11 - Create Dynamic Search List with Authentication Type VMWare"""
        params = {"auth_types": "VMware"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_12(self, api_client, common_functions, op_path, dbo):
        """TC 12 - Create Dynamic Search List with Authentication Type Windows"""
        params = {"auth_types": "Windows"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_13(self, api_client, common_functions, op_path, dbo):
        """TC 14 - Create Dynamic Search List with Categories Type AmaZOn Linux"""
        params = {"categories": "Amazon Linux"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_14(self, api_client, common_functions, op_path, dbo):
        """TC 15 - Create Dynamic Search List with Categories Type backdrops_and_trojan_horses"""
        params = {"categories": "Backdoors and trojan horses"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_15(self, api_client, common_functions, op_path, dbo):
        """TC 16 - Create Dynamic Search List with Categories Type Brute Force Attack"""
        params = {"categories": "Brute Force Attack"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_16(self, api_client, common_functions, op_path, dbo):
        """TC 17 - Create Dynamic Search List with Categories Type CGI"""
        params = {"categories": "CGI"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_17(self, api_client, common_functions, op_path, dbo):
        """TC 18 - Create Dynamic Search List with Categories Type CentOS"""
        params = {"categories": "CentOS"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_18(self, api_client, common_functions, op_path, dbo):
        """TC 19 - Create Dynamic Search List with Categories Type cisco"""
        params = {"categories": "Cisco"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_19(self, api_client, common_functions, op_path, dbo):
        """TC 20 - Create Dynamic Search List with Categories Type dns and bind"""
        params = {"categories": "DNS and BIND"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_20(self, api_client, common_functions, op_path, dbo):
        """TC 21 - Create Dynamic Search List with Categories Type Database"""
        params = {"categories": "Database"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_21(self, api_client, common_functions, op_path, dbo):
        """TC 22 - Create Dynamic Search List with Categories Type E-Commerce"""
        params = {"categories": "E-Commerce"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_22(self, api_client, common_functions, op_path, dbo):
        """TC 23 - Create Dynamic Search List with Categories Type Fedora"""
        params = {"categories": "Fedora"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_23(self, api_client, common_functions, op_path, dbo):
        """TC 24 - Create Dynamic Search List with Categories Type file transfer protocol"""
        params = {"categories": "File Transfer Protocol"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_24(self, api_client, common_functions, op_path, dbo):
        """TC 25 - Create Dynamic Search List with Categories Type Finger"""
        params = {"categories": "Finger"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_25(self, api_client, common_functions, op_path, dbo):
        """TC 26 - Create Dynamic Search List with Categories Type Firewall"""
        params = {"categories": "Firewall"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_26(self, api_client, common_functions, op_path, dbo):
        """TC 27 - Create Dynamic Search List with Categories Type Forensics"""
        params = {"categories": "Forensics"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_27(self, api_client, common_functions, op_path, dbo):
        """TC 28 - Create Dynamic Search List with Categories Type General remote Services"""
        params = {"categories": "General remote services"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_28(self, api_client, common_functions, op_path, dbo):
        """TC 29 - Create Dynamic Search List with Categories Type HP-UX"""
        params = {"categories": "HP-UX"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_29(self, api_client, common_functions, op_path, dbo):
        """TC 30 - Create Dynamic Search List with Categories Type Hardware"""
        params = {"categories": "Hardware"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_30(self, api_client, common_functions, op_path, dbo):
        """TC 31 - Create Dynamic Search List with Categories Type Information Gathering"""
        params = {"categories": "Information gathering"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_31(self, api_client, common_functions, op_path, dbo):
        """TC 32 - Create Dynamic Search List with Categories Type Internet Explorer"""
        params = {"categories": "Internet Explorer"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_32(self, api_client, common_functions, op_path, dbo):
        """TC 33 - Create Dynamic Search List with Categories Type Local"""
        params = {"categories": "Local"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_33(self, api_client, common_functions, op_path, dbo):
        """TC 34 - Create Dynamic Search List with Categories Type Mail Services"""
        params = {"categories": "Mail services"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_34(self, api_client, common_functions, op_path, dbo):
        """TC 35 - Create Dynamic Search List with Categories Type NFS"""
        params = {"categories": "NFS"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_35(self, api_client, common_functions, op_path, dbo):
        """TC 36 - Create Dynamic Search List with Categories Type News Server"""
        params = {"categories": "News Server"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_36(self, api_client, common_functions, op_path, dbo):
        """TC 37 - Create Dynamic Search List with Categories Type OEL"""
        params = {"categories": "OEL"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_37(self, api_client, common_functions, op_path, dbo):
        """TC 38 - Create Dynamic Search List with Categories Type OVAL"""
        params = {"categories": "OVAL"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_38(self, api_client, common_functions, op_path, dbo):
        """TC 39 - Create Dynamic Search List with Categories Type Oracle VM Server"""
        params = {"categories": "Oracle VM Server"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_39(self, api_client, common_functions, op_path, dbo):
        """TC 40 - Create Dynamic Search List with Categories Type Proxy"""
        params = {"categories": "Proxy"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_40(self, api_client, common_functions, op_path, dbo):
        """TC 41 - Create Dynamic Search List with Categories Type QRDI"""
        params = {"categories": "QRDI"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_41(self, api_client, common_functions, op_path, dbo):
        """TC 42 - Create Dynamic Search List with Categories Type RPC"""
        params = {"categories": "RPC"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_42(self, api_client, common_functions, op_path, dbo):
        """TC 44 - Create Dynamic Search List with Categories Type SMB/NETBIOS"""
        params = {"categories": "SMB / NETBIOS"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_43(self, api_client, common_functions, op_path, dbo):
        """TC 45 - Create Dynamic Search List with Categories Type SNMP"""
        params = {"categories": "SNMP"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_44(self, api_client, common_functions, op_path, dbo):
        """TC 46 - Create Dynamic Search List with Categories Type SUSE"""
        params = {"categories": "SUSE"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_45(self, api_client, common_functions, op_path, dbo):
        """TC 47 - Create Dynamic Search List with Categories Type Security Policy"""
        params = {"categories": "Security Policy"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_46(self, api_client, common_functions, op_path, dbo):
        """TC 48 - Create Dynamic Search List with Categories Type Solaris"""
        params = {"categories": "Solaris"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_47(self, api_client, common_functions, op_path, dbo):
        """TC 49 - Create Dynamic Search List with Categories Type TCP/IP"""
        params = {"categories": "TCP/IP"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_48(self, api_client, common_functions, op_path, dbo):
        """TC 50 - Create Dynamic Search List with Categories Type Ubuntu"""
        params = {"categories": "Ubuntu"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_49(self, api_client, common_functions, op_path, dbo):
        """TC 51 - Create Dynamic Search List with Categories Type Vmware"""
        params = {"categories": "VMware"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_50(self, api_client, common_functions, op_path, dbo):
        """TC 52 - Create Dynamic Search List with Categories Type Web Application"""
        params = {"categories": "Web Application"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_51(self, api_client, common_functions, op_path, dbo):
        """TC 53 - Create Dynamic Search List with Categories Type Information Web Application FireWall"""
        params = {"categories": "Web Application Firewall"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_52(self, api_client, common_functions, op_path, dbo):
        """TC 54 - Create Dynamic Search List with Categories Type Webserver"""
        params = {"categories": "Web server"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_53(self, api_client, common_functions, op_path, dbo):
        """TC 55 - Create Dynamic Search List with Categories Type Window"""
        params = {"categories": "Windows"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_54(self, api_client, common_functions, op_path, dbo):
        """TC 56 - Create Dynamic Search List with Categories Type X-Windows"""
        params = {"categories": "X-Window"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_55(self, api_client, common_functions, op_path, dbo):
        """TC 57 - Create Dynamic Search List with Patch Available Option Enabled"""
        params = {"patch_available": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_56(self, api_client, common_functions, op_path, dbo):
        """TC 58 - Create Dynamic Search List with patch trend micro"""
        params = {"patch_available": "1", "virtual_patch_available": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_57(self, api_client, common_functions, op_path, dbo):
        """TC 59 - Create Dynamic Search List without virtual patch"""
        params = {"patch_available": "1", "virtual_patch_available": "1" }
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_58(self, api_client, common_functions, op_path, dbo):
        """TC 60 - Create Dynamic Search List with CVEID"""
        params = {"cve_ids": "CVE-2018-0477,CVE-2015-3183,CVE-2016-3110,CVE-2016-4459,CVE-2018-10194"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_59(self, api_client, common_functions, op_path, dbo):
        """TC 61 - Create Dynamic Search List with Categories Type CVE ID not in"""
        params = {"cve_ids": "CVE-2016-4459,CVE-2018-10194", "not_cve_ids": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_60(self, api_client, common_functions, op_path, dbo):
        """TC 62 - Create Dynamic Search List with CPE_ALL"""
        params = {"cpe": "ALL"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_61(self, api_client, common_functions, op_path, dbo):
        """TC 63 - Create Dynamic Search List with CPE Application"""
        params = {"cpe": "Application"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_62(self, api_client, common_functions, op_path, dbo):
        """TC 64 - Create Dynamic Search List with CPE Hardware"""
        params = {"cpe": "Hardware"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_63(self, api_client, common_functions, op_path, dbo):
        """TC 65 - Create Dynamic Search List with CPE None"""
        params = {"cpe": "None"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_64(self, api_client, common_functions, op_path, dbo):
        """TC 66 - Create Dynamic Search List with CPE Operating system"""
        params = {"cpe": "Operating System"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_65(self, api_client, common_functions, op_path, dbo):
        """TC 67 - Create Dynamic Search List with Exploitability Core Security"""
        params = {"exploitability": "Core Security"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_66(self, api_client, common_functions, op_path, dbo):
        """TC 68 - Create Dynamic Search List with Wxploitability exploitkits"""
        params = {"exploitability": "ExploitKits"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_67(self, api_client, common_functions, op_path, dbo):
        """TC 69 - Create Dynamic Search List with Exploitability Immunity"""
        params = {"exploitability": "Core Security"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_68(self, api_client, common_functions, op_path, dbo):
        """TC 70 - Create Dynamic Search List with Exploitability Immunity-Agora"""
        params = {"exploitability": "Immunity - Agora"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_69(self, api_client, common_functions, op_path, dbo):
        """TC 71 - Create Dynamic Search List with Immunity Dsquare"""
        params = {"exploitability": "Core Security"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_70(self, api_client, common_functions, op_path, dbo):
        """TC 72 - Create Dynamic Search List with Immunity Enable Security"""
        params = {"exploitability": "Immunity - Enable Security"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_71(self, api_client, common_functions, op_path, dbo):
        """TC 73 - Create Dynamic Search List with Wxploitability immunity_white_phosphourus"""
        params = {"exploitability": "Immunity - White Phosphorus"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_72(self, api_client, common_functions, op_path, dbo):
        """TC 74 - Create Dynamic Search List with Wxploitability Metasploit"""
        params = {"exploitability": "Metasploit"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_73(self, api_client, common_functions, op_path, dbo):
        """TC 75 - Create Dynamic Search List with Wxploitability Qualys"""
        params = {"exploitability": "Qualys"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_74(self, api_client, common_functions, op_path, dbo):
        """TC 76 - Create Dynamic Search List with Wxploitability the_exploit_db"""
        params = {"exploitability": "The Exploit-DB"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_75(self, api_client, common_functions, op_path, dbo):
        """TC 77 - Create Dynamic Search List with Associated Malware"""
        params = {"malware_associated": "Trend Micro"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_76(self, api_client, common_functions, op_path, dbo):
        """TC 78 - Create Dynamic Search List with Associated Malware trendmicro"""
        params = {"malware_associated": "Trend Micro"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_77(self, api_client, common_functions, op_path, dbo):
        """TC 79 - Create Dynamic Search List with Vendor Reference Redhat"""
        params = {"vendor_refs": "RHSA-2018:2772"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_78(self, api_client, common_functions, op_path, dbo):
        """TC 80 - Create Dynamic Search List with Vendor Reference CISCO"""
        params = {"vendor_refs": "cisco-sa-20180926-ptp"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_79(self, api_client, common_functions, op_path, dbo):
        """TC 81 - Create Dynamic Search List with Not Vendor Reference CISCO"""
        params = {"not_vendor_refs": "1", "vendor_refs": "cisco-sa-20180926-ptp"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_80(self, api_client, common_functions, op_path, dbo):
        """TC 82 - Create Dynamic Search List with Not Vendor Reference CISCO"""
        params = {"not_vendor_refs": "1", "vendor_refs": "cisco-sa-20180926-ptp"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_81(self, api_client, common_functions, op_path, dbo):
        """TC 83 - Create Dynamic Search List with Not Vendor Reference CISCO"""
        params = {"not_vendor_refs": "1", "vendor_refs": "cisco-sa-20180926-ptp"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_82(self, api_client, common_functions, op_path, dbo):
        """TC 84 - Create Dynamic Search List with Vendor Reference CVSS Base Score"""
        params = {"cvss_base_operand": "1", "cvss_base": "6"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_83(self, api_client, common_functions, op_path, dbo):
        """TC 85 - Create Dynamic Search List with Vendor Reference CVSS Base Score"""
        params = {"cvss_base_operand": "2", "cvss_base": "6"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_84(self, api_client, common_functions, op_path, dbo):
        """TC 86 - Create Dynamic Search List with Vendor Reference CVSS Base Score  Temporal less than"""
        params = {"cvss_temp_operand": "1", "cvss_temp": "5"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_85(self, api_client, common_functions, op_path, dbo):
        """TC 87 - Create Dynamic Search List with Vendor Reference CVSS Base Score Temporal Greater equal"""
        params = {"cvss_temp_operand": "1", "cvss_temp": "6"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_86(self, api_client, common_functions, op_path, dbo):
        """TC 88 - Create Dynamic Search List with Vendor Reference CVSS Base3 Score Temporal"""
        params = {"cvss3_base_operand": "1", "cvss3_base": "5"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_87(self, api_client, common_functions, op_path, dbo):
        """TC 89 - Create Dynamic Search List with Vendor Reference CVSS Base Score Temporal"""
        params = {"cvss3_temp_operand": "2", "cvss3_temp": "8"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_88(self, api_client, common_functions, op_path, dbo):
        """TC 90 - Create Dynamic Search List with Vendor Reference CVSS access vector Local Access"""
        params = {"cvss_access_vector": "Local Access"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_89(self, api_client, common_functions, op_path, dbo):
        """TC 91 - Create Dynamic Search List with Vendor Reference CVSS access vector adjuscent network"""
        params = {"cvss_access_vector": "Adjacent Network"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_90(self, api_client, common_functions, op_path, dbo):
        """TC 92 - Create Dynamic Search List with Vendor Reference CVSS access vector Network"""
        params = {"cvss_access_vector": "Network"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_91(self, api_client, common_functions, op_path, dbo):
        """TC 93 - Create Dynamic Search List with BugTrack ID"""
        params = {"bugtraq_id": "75963"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_92(self, api_client, common_functions, op_path, dbo):
        """TC 94 - Create Dynamic Search List with Not BugTrack ID"""
        params = {"bugtraq_id": "105108", "not_bugtraq_id": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_93(self, api_client, common_functions, op_path, dbo):
        """TC 95 - Create Dynamic Search List with Service Modified Today"""
        params = {"service_modified_date_today": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_94(self, api_client, common_functions, op_path, dbo):
        """TC 96 - Create Dynamic Search List with Service Modified in previous year"""
        params = {"service_modified_date_in_previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_95(self, api_client, common_functions, op_path, dbo):
        """TC 97 - Create Dynamic Search List with Service Modified in previous month"""
        params = {"service_modified_date_in_previous": "Month"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_96(self, api_client, common_functions, op_path, dbo):
        """TC 98 - Create Dynamic Search List with Service Modified Week"""
        params = {"service_modified_date_in_previous": "Week"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_97(self, api_client, common_functions, op_path, dbo):
        """TC 99 - Create Dynamic Search List with Service Modified previous quarter"""
        params = {"service_modified_date_in_previous": "Quarter"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_98(self, api_client, common_functions, op_path, dbo):
        """TC 100 - Create Dynamic Search List with Service Modified Today"""
        params = {"service_modified_date_today": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_99(self, api_client, common_functions, op_path, dbo):
        """TC 101 - Create Dynamic Search List with Service Modified date within last days"""
        params = {"service_modified_date_within_last_days": "60"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_100(self, api_client, common_functions, op_path, dbo):
        """TC 102 - Create Dynamic Search List with Service Modified date between"""
        params = {"service_modified_date_between": "01/01/2018-01/15/2019"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_101(self, api_client, common_functions, op_path, dbo):
        """TC 103 - Create Dynamic Search List with Service Modified not Today"""
        params = {"not_service_modified_flag": "1", "service_modified_date_today": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_102(self, api_client, common_functions, op_path, dbo):
        """TC 104 - Create Dynamic Search List with Service Modified in not previous year"""
        params = {"not_service_modified_flag": "1", "service_modified_date_in_previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_103(self, api_client, common_functions, op_path, dbo):
        """TC 105 - Create Dynamic Search List with Service Modified in not previous month"""
        params = {"not_service_modified_flag": "1", "service_modified_date_in_previous": "Month"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_104(self, api_client, common_functions, op_path, dbo):
        """TC 106 - Create Dynamic Search List with Service Modified not in previous Week"""
        params = {"not_service_modified_flag": "1", "service_modified_date_in_previous": "Week"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_105(self, api_client, common_functions, op_path, dbo):
        """TC 107 - Create Dynamic Search List with User Modified Today"""
        params = {"user_modified_date_today": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_106(self, api_client, common_functions, op_path, dbo):
        """TC 108 - Create Dynamic Search List with User Modified in previous year"""
        params = {"user_modified_date_in previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_107(self, api_client, common_functions, op_path, dbo):
        """TC 109 - Create Dynamic Search List with User Modified in previous month"""
        params = {"user_modified_date_in previous": "Month"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_108(self, api_client, common_functions, op_path, dbo):
        """TC 110 - Create Dynamic Search List with User Modified Week"""
        params = {"user_modified_date_in previous": "Week"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_109(self, api_client, common_functions, op_path, dbo):
        """TC 111 - Create Dynamic Search List with User Modified previous quarter"""
        params = {"service_modified_date_in_previous": "Quarter"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_110(self, api_client, common_functions, op_path, dbo):
        """TC 112 - Create Dynamic Search List with User Modified date in previous year"""
        params = {"user_modified_date_in_previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_111(self, api_client, common_functions, op_path, dbo):
        """TC 113 - Create Dynamic Search List with User Modified date within last days"""
        params = {"user_modified_date_within_last_days": "60"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_112(self, api_client, common_functions, op_path, dbo):
        """TC 114 - Create Dynamic Search List with User Modified date between"""
        params = {"user_modified_date_between": "01/01/2018-01/15/2019"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_113(self, api_client, common_functions, op_path, dbo):
        """TC 115 - Create Dynamic Search List with QID Modified not Today"""
        params = {"not_published_flag": "1", "published_date_today": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_114(self, api_client, common_functions, op_path, dbo):
        """TC 116 - Create Dynamic Search List with QID Modified in not previous year"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_115(self, api_client, common_functions, op_path, dbo):
        """TC 117 - Create Dynamic Search List with QID Modified in not previous month"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Month"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_116(self, api_client, common_functions, op_path, dbo):
        """TC 118 - Create Dynamic Search List with QID Modified not in previous Week"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Week"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_117(self, api_client, common_functions, op_path, dbo):
        """TC 119 - Create Dynamic Search List with QID Modified Not in previous quarter"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Quarter"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_118(self, api_client, common_functions, op_path, dbo):
        """TC 120 - Create Dynamic Search List with QID Modified Not in previous year"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_119(self, api_client, common_functions, op_path, dbo):
        """TC 130 - Create Dynamic Search List with QID Modified NOT date within last 60 days"""
        params = {"not_published_flag": "1", "published_date_within_last_days": "60"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_120(self, api_client, common_functions, op_path, dbo):
        """TC 131 - Create Dynamic Search List with QID Modified  NOt date between"""
        params = {"not_published_flag": "1", "published_date_between": "01/01/2018-01/15/2019"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_121(self, api_client, common_functions, op_path, dbo):
        """TC 132 - Create Dynamic Search List with Published Today"""
        params = {"published_date_today": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_122(self, api_client, common_functions, op_path, dbo):
        """TC 133 - Create Dynamic Search List with QID published in previous year"""
        params = {"published_date_in_previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_123(self, api_client, common_functions, op_path, dbo):
        """TC 134 - Create Dynamic Search List with QID Published Modified in previous month"""
        params = {"published_date_in_previous": "Month"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_124(self, api_client, common_functions, op_path, dbo):
        """TC 135 - Create Dynamic Search List with QID published in Week"""
        params = {"published_date_in_previous": "Week"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_125(self, api_client, common_functions, op_path, dbo):
        """TC 136 - Create Dynamic Search List with QID published previous quarter"""
        params = {"published_date_in_previous": "Quarter"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_126(self, api_client, common_functions, op_path, dbo):
        """TC 137 - Create Dynamic Search List with qid published date in previous year"""
        params = {"published_date_in_previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_127(self, api_client, common_functions, op_path, dbo):
        """TC 138 - Create Dynamic Search List with QID published  date within last 60 days"""
        params = {"published_date_within_last_days": "9999"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_128(self, api_client, common_functions, op_path, dbo):
        """TC 139 - Create Dynamic Search List with QID published date between"""
        params = {"published_date_between": "01/01/2018-01/15/2019"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_129(self, api_client, common_functions, op_path, dbo):
        """TC 140 - Create Dynamic Search List with QID Modified not Today"""
        params = {"not_published_flag": "1", "published_date_today": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_130(self, api_client, common_functions, op_path, dbo):
        """TC 141 - Create Dynamic Search List with QID Modified in not previous year"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_131(self, api_client, common_functions, op_path, dbo):
        """TC 142 - Create Dynamic Search List with QID Modified in not previous month"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Month"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_132(self, api_client, common_functions, op_path, dbo):
        """TC 143 - Create Dynamic Search List with QID Modified not in previous Week"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Week"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_133(self, api_client, common_functions, op_path, dbo):
        """TC 144 - Create Dynamic Search List with QID Modified not Today"""
        params = {"not_published_flag": "1", "published_date_today": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_134(self, api_client, common_functions, op_path, dbo):
        """TC 145 - Create Dynamic Search List with QID Modified in not previous year"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_135(self, api_client, common_functions, op_path, dbo):
        """TC 146 - Create Dynamic Search List with User Modified in not previous month"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Month"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_136(self, api_client, common_functions, op_path, dbo):
        """TC 148 - Create Dynamic Search List with QID Modified Not in previous quarter"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Quarter"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_137(self, api_client, common_functions, op_path, dbo):
        """TC 149 - Create Dynamic Search List with qid Modified Not in previous year"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Year"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_138(self, api_client, common_functions, op_path, dbo):
        """TC 150 - Create Dynamic Search List with QID Modified NOT date within last 60 days"""
        params = {"not_published_flag": "1", "published_date_within_last_days": "60"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_139(self, api_client, common_functions, op_path, dbo):
        """TC 151 - Create Dynamic Search List with QID Modified  NOt date between"""
        params = {"not_published_flag": "1", "published_date_between": "01/01/2018-01/15/2019"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)


    def test_sl_140(self, api_client, common_functions, op_path, dbo):
        """TC 152 - Create Dynamic Search List with confirmed sevirity"""
        params = {"confirmed_severities": "1,2,3,4,5"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_145(self, api_client, common_functions, op_path, dbo):
        """TC 153 - Create Dynamic Search List with confirmed sevirity"""
        params = {"confirmed_severities": "1,2,3"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_146(self, api_client, common_functions, op_path, dbo):
        """TC 154 - Create Dynamic Search List with vendor"""
        params = {"vendor_ids": "3"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_147(self, api_client, common_functions, op_path, dbo):
        """TC 155 - Create Dynamic Search List with Not vendor"""
        params = {"not_vendor_ids": "1"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_148(self, api_client, common_functions, op_path, dbo):
        """TC 156 - Create Dynamic Search List with Not vendor"""
        params = {"products": "acrobat,adobe_air,chrome,dbus,enterprise_linux,.net_framework"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_149(self, api_client, common_functions, op_path, dbo):
        """TC 157 - Create Dynamic Search List with Not 2 Products"""
        params = {"not_products": "1", "products": "4500_switch_50-port,.net_framework,.net_framework_developer_pack,.net_core_sdk"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_150(self, api_client, common_functions, op_path, dbo):
        """TC 158 - Create Dynamic Search List with Not Products"""
        params = {"not_products": "1", "products": "4500_switch_50-port"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_151(self, api_client, common_functions, op_path, dbo):
        """TC 159 - Create Dynamic Search List with Vuln Details"""
        params = {"vuln_details": "Security Fixes: Mozilla"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_152(self, api_client, common_functions, op_path, dbo):
        """TC 160 - Create Dynamic Search List with Supported Modules"""
        params = {"supported_modules": "VM,CA-Windows Agent,CA-Linux Agent,WAS,WAF,MD,CA-Mac Agent,CA-AIX Agent"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_153(self, api_client, common_functions, op_path, dbo):
        """TC 161 - Create Dynamic Search List with PCI Compliance"""
        params = {"compliance_types": "PCI"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_154(self, api_client, common_functions, op_path, dbo):
        """TC 162 - Create Dynamic Search List with CobiT Compliance"""
        params = {"compliance_types": "CobIT"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_155(self, api_client, common_functions, op_path, dbo):
        """TC 163 - Create Dynamic Search List with HIPPA Compliance"""
        params = {"compliance_types": "HIPAA"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_156(self, api_client, common_functions, op_path, dbo):
        """TC 164 - Create Dynamic Search List with GLBA  Compliance"""
        params = {"compliance_types": "GLBA"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_157(self, api_client, common_functions, op_path, dbo):
        """TC 165 - Create Dynamic Search List with SOX  Compliance"""
        params = {"compliance_types": "SOX"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_158(self, api_client, common_functions, op_path, dbo):
        """TC 166 - Create Dynamic Search List with Qualys Top Internal 20  Compliance"""
        params = {"qualys_top_lists": "Internal_10"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_159(self, api_client, common_functions, op_path, dbo):
        """TC 167 - Create Dynamic Search List with Qualys Top External 10  Compliance"""
        params = {"qualys_top_lists": "External_10"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_160(self, api_client, common_functions, op_path, dbo):
        """TC 168 - Create Dynamic Search List with Qualys Top Internal and External 10  Compliance"""
        params = {"qualys_top_lists": "Internal_10,External_10"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_161(self, api_client, common_functions, op_path, dbo):
        """TC 169 - Create Dynamic Search List with provider Amazon  Compliance"""
        params = {"vuln_provider": "Amazon"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_162(self, api_client, common_functions, op_path, dbo):
        """TC 170 - Create Dynamic Search List with provider Apple  Compliance"""
        params = {"vuln_provider": "Apple"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_163(self, api_client, common_functions, op_path, dbo):
        """TC 171 - Create Dynamic Search List with provider iDefence  Compliance"""
        params = {"vuln_provider": "iDefense"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_164(self, api_client, common_functions, op_path, dbo):
        """TC 172 - Create Dynamic Search List with provider win2k3  Compliance"""
        params = {"vuln_provider": "Windows 2003 Extended Support"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)
    def test_sl_165(self, api_client, common_functions, op_path, dbo):
        """TC 173 - Create Dynamic Search List with Categories Type AIX"""
        params = {"categories": "AIX"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_166(self, api_client, common_functions, op_path, dbo):
        """TC 174 - Create Dynamic Search List with Categories Type RedHat"""
        params = {"categories": "RedHat"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_167(self, api_client, common_functions, op_path, dbo):
        """TC 175 - Create Dynamic Search List with QID Modified not in previous Week"""
        params = {"not_published_flag": "1", "published_date_in_previous": "Week"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params)
        print("Created: SL", sl_id)
        assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
        SeachList.delete_dynamic_search_list(sl_id, api_client)

    def test_sl_168(self, api_client, common_functions, op_path, dbo):
        """TC 176 - Create Dynamic Search List And Update QID with sevirity from 5-1"""
        params1 = {"confirmed_severities": "5"}
        sl_id = SeachList.create_dynamic_search_list(api_client, params1)
        print("Created: SL", sl_id)
        res = SeachList.get_qid_list_from_json(SeachList.get_qid_service_search_list(api_client, common_functions,sl_id))
        qid_to_change=res[0]
        print("QID picked up for updation :",  qid_to_change)
        #params_qid_update = {"sevirity": "1"}
        #SeachList.update_qid(api_client, params_qid_update, qid_to_change)
        qid_update = {
            "action": "edit",
            "qid": qid_to_change,
            "severity": "1"
        }
        res=api_client.qualys_api_call("POST", "/api/2.0/fo/knowledge_base/vuln/", qid_update)
        assert res.status_code == 200, "Invalid Status Code returned by QWEB API"
        print(res.text)
        res = SeachList.get_qid_list_from_json(SeachList.get_qid_service_search_list(api_client, common_functions,sl_id))
        print(res[0])
        for id in res:
            if id == qid_to_change:
                print(id)
                flag = False
                break
            else:
                assert SeachList.verify_qids(sl_id, api_client, common_functions), "Invalid QIDs Found"
                flag = True

        print(flag)
        SeachList.delete_dynamic_search_list(sl_id, api_client)
        assert flag, "Updated QID is present in the SearchList"



    # def test_verify_all_sl(self, api_client, common_functions, op_path, dbo):
    #     """TC 02 - Verify All Dynamic Search List"""
    #     assert SeachList.verify_all_dynamic_sl_in_subscription(api_client, common_functions, dbo), "Invalid QIDs Found"
