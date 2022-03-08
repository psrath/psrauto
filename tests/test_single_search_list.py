import random
import string
import pytest
import sys
from src.SearchList import SeachList


@pytest.mark.TestSingleSeachListResolve
class TestSingleSeachListResolve:
    """Test Single SearchList Resolve -"""

    def test_single_sl(self, api_client, common_functions, op_path, dbo):
        """TC S01 - Test Single SearchList"""
        sub_id = common_functions.get_subscription_id()
        query_str = "select ID from SEARCH_LIST where SUBSCRIPTION_ID = :sub_id and ID > 0 and " \
                    "IS_SYSTEM = 0"
        print(query_str)
        print(sub_id);
        local_log_file = "D:/git/qidservice/qid-service/src/test/qid-service-automation/reports/debug.log"
        debug = open(local_log_file, 'w', 2)
        sl_ids = dbo.execute_query(query_str, {'sub_id': sub_id})
        is_failed = False
        cnt_passed = 0
        cnt_failed = 0
        completed = 0
        debug.write("Total SearchLists : " + str(len(sl_ids)) + "\n");
        for sl_id in sl_ids:
            print("================================================================================")
            print("Verifying for Search List:", sl_id[0])
            completed += 1
            debug.write("================================================================================" + "\n");
            debug.write(str(completed) + ": verifying for Search List:" + str(sl_id[0]) + "\n")
            if not SeachList.verify_qids(sl_id[0], api_client, common_functions):
                print("FAILED: Search List Validation for ID:", sl_id[0])
                debug.write("FAILED: Search List Validation for ID:" + str(sl_id[0]) + "\n");
                is_failed = True
                cnt_failed += 1
            else:
                print("PASSED: Search List Validation for ID:", sl_id[0])
                debug.write("PASSED: Search List Validation for ID:" + str(sl_id[0]) + "\n");
                cnt_passed += 1

        debug.close()

        print("************** Summary of all search list ************")
        print("Total Passed: " + str(cnt_passed))
        print("Total Failed: " + str(cnt_failed))
        print("******************************************************")
        if is_failed:
            return False
        return True