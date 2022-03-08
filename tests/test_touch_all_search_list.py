import random
import string
import pytest
import sys
import datetime
from src.SearchList import SeachList


@pytest.mark.TestTouchAllSeachListResolve
class TestTouchAllSeachListResolve:
    """Test Touch all SearchList Resolve -"""

    def test_touch_all_sl(self, api_client, common_functions, op_path, dbo):
        """TC S01 - Test Touch all SearchList"""


        query_str = "select sl.ID, s.UUID from SEARCH_LIST sl inner join SUBSCRIPTION s on s.SUBSCRIPTION_ID = sl.SUBSCRIPTION_ID where " \
                    " sl.IS_SYSTEM = 0 and s.STATUS = 4 and s.EXPIRATION_DATE > sysdate  " \
                    " and sl.ID in (54760, 341960) " \
                    " and exists (select 1 from QG_ACCESS_DATA qad where s.SUBSCRIPTION_ID = qad.SUBSCRIPTION_ID and qad.ENABLED = 1 ) "
        print(query_str)

        sl_ids = dbo.execute_query(query_str, {})
        is_failed = False
        cnt_passed = 0
        cnt_failed = 0
        for sl_id in sl_ids:
            print("================================================================================")
            print("Verifying for Search List:", sl_id[0])

            params = {
                "customerUuid": sl_id[1],
                "lang": "en",
                "searchListId": sl_id[0],
                "noCache": "true"
            }
            startTs = datetime.datetime.now()
            res = api_client.qid_service_api_call("GET", "/resolve", params)
            endTs = datetime.datetime.now()
            deltaTs = endTs - startTs
            assert res.status_code == 200, "Invalid Status Code returned by QID Service API"

            sl_id_exist = dbo.fetch_value("select 1 from RAMA_QIDS_PERFORMANCE where ID = :id ", {'id': sl_id[0]});
            if sl_id_exist:
                dbo.execute("update RAMA_QIDS_PERFORMANCE set TIME_TAKEN = :time_taken, UPDATED_ON = sysdate where ID = :id",
                     {'time_taken': int(deltaTs.total_seconds() * 1000), 'id': sl_id[0]});
            else:
                dbo.insert_row("RAMA_QIDS_PERFORMANCE", {'ID': sl_id[0], 'TIME_TAKEN': int(deltaTs.total_seconds() * 1000)});

            print("PASSED: Search List Validation for ID:", sl_id[0])
            cnt_passed += 1

        print("************** Summary of all search list ************")
        print("Total Passed: " + str(cnt_passed))
        print("Total Failed: " + str(cnt_failed))
        print("******************************************************")
        if is_failed:
            return False
        return True