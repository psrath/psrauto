import json

class JsonParser:
    ''' Json Parser '''


    def __init__(self, jsonSource):
        self.jsonSource = jsonSource
        #inputFile = open(self.jsonSource, 'r')
        self.jsonObj = json.loads(self.jsonSource)
        self.lst = []


    def extract_values(self, key):
        """Pull all values of specified key from nested JSON."""
        arr = []
        obj = self.jsonObj

        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        results = extract(obj, arr, key)
        return results

    def key_exists_in_json(self, key):
        #lst.clear()
        res = self.extract_values(key)
        if len(res) > 0:
            return True
        else:
            return False
    def retrive_value_for_json_key(self, key):
        self.lst.clear()
        lst = self.extract_values(key)
        if len(lst) > 0:
            #for l in lst:
            return lst
        else:
            return "No Data Found"
    def retrive_key_count_from_json(self, key):
        self.lst.clear()
        lst = self.extract_values(key)
        if len(lst) > 0:
            return len(lst)
        else:
            return False

# json_Data = """{
#     "success": 1,
#     "message": null,
#     "status": 0,
#     "error": null,
#     "data": {
#         "CVE-2021-36765": {
#             "base": {
#                 "id": "CVE-2021-36765",
#                 "idType": "CVE",
#                 "qvs": "28",
#                 "qvsLastChangedDate": 1640649600,
#                 "nvdPublishedDate": 1628086500
#             },
#             "contributingFactors": {
#                 "cvss": "5",
#                 "cvssVersion": "v2"
#             }
#         }
#     },
#     "timeStamp": "2022-01-17T00:15:12.486+0000 UTC",
#     "info": null
# }"""
#
# j = JsonParser(json_Data)
# res = j.key_exists_in_json("cvss")
# print(res)
# #strRes = ''.join([str(items) for items in res])
# #print(j.retrive_key_count_from_json("id"))
# #print(strRes)
