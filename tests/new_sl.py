def test_sl_163(self, api_client, common_functions, op_path, dbo):
    """TC 180 - Create Dynamic Search List with provider iDefence  Compliance"""
    params = {"vuln_provider": "ITAM-VM Detections"}
    sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    print("Created: SL-QWEB", sl_id_qweb)
    sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    print("Created: SL-Service", sl_id_service)
    assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client,
                                              common_functions), "Invalid QIDs Found"
    SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

def test_sl_163(self, api_client, common_functions, op_path, dbo):
    """TC 181 - Create Dynamic Search List with provider iDefence  Compliance"""
    params = {"vuln_provider": "Qualys Debug"}
    sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    print("Created: SL-QWEB", sl_id_qweb)
    sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    print("Created: SL-Service", sl_id_service)
    assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client,
                                              common_functions), "Invalid QIDs Found"
    SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

def test_sl_163(self, api_client, common_functions, op_path, dbo):
    """TC 182 - Create Dynamic Search List with provider iDefence  Compliance"""
    params = {"vuln_provider": "Santander"}
    sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    print("Created: SL-QWEB", sl_id_qweb)
    sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    print("Created: SL-Service", sl_id_service)
    assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client,
                                              common_functions), "Invalid QIDs Found"
    SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')

def test_sl_163(self, api_client, common_functions, op_path, dbo):
    """TC 183 - Create Dynamic Search List with provider iDefence  Compliance"""
    params = {"vuln_provider": "ICS"}
    sl_id_qweb = SeachList.create_dynamic_search_list(api_client, params, 'qweb')
    print("Created: SL-QWEB", sl_id_qweb)
    sl_id_service = SeachList.create_dynamic_search_list(api_client, params, 'qid')
    print("Created: SL-Service", sl_id_service)
    assert SeachList.verify_qids_qweb_service(sl_id_qweb, sl_id_service, api_client,
                                              common_functions), "Invalid QIDs Found"
    SeachList.delete_dynamic_search_list(sl_id_qweb, api_client, 'qweb')
    SeachList.delete_dynamic_search_list(sl_id_service, api_client, 'qid')