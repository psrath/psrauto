# -*- coding: utf-8 -*-
# import ET as ET
from lxml import etree
from io import StringIO, BytesIO


# from xml.etree import ElementTree as ET
# from Handlers import BaseHandler

class XmlParser:
    ''' XML Parser '''

    def __init__(self, xmlSource):
        self.xmlSource = xmlSource
        parser = etree.XMLParser(strip_cdata=False,remove_blank_text=True)
        self.root = etree.XML(bytes(bytearray(self.xmlSource, encoding='utf-8')), parser)

    def get_elements(self, xpath):
        return self.root.findall(xpath)

    def get_element_count(self, xpath):
        count = len(self.root.xpath(xpath))
        return count

    def get_element(self, xpath):
        return self.root.find(xpath)
        return self.root.find

    def get_element_text(self, xpath):
        # print xpath
        return self.root.xpath(xpath)[0].text

    def get_all_child_tags_tostring(self, xpath):
        el = self.get_element(xpath)
        if el is not None:
            return etree.tostring(el, method='xml', pretty_print=True).decode()
        return None

    def get_element_attribute(self, name, xpath='.', default=None):
        return self.root.find(xpath).get(name, default)

#  xml_data="""<?xml version="1.0"?>
# <HOST_DIFF>
#   <USER_HOST_ID>1135518</USER_HOST_ID>
#   <SUBSCRIPTION_ID>263788</SUBSCRIPTION_ID>
#   <EVENT_TYPE>HOST_UPDATED</EVENT_TYPE>
#   <IS_IP_IN_CV/>
#   <HOST ID="1135518">
#     <IP><![CDATA[10.91.77.234]]></IP>
#   </HOST>
#   <HOST_CHANGE_QUEUE_ID>3947720</HOST_CHANGE_QUEUE_ID>
# </HOST_DIFF>
# """
# xml_data = """<?xml version="1.0" encoding="UTF-8" ?>
# <!DOCTYPE SIMPLE_RETURN SYSTEM "https://qualysapi.p04.eng.sjc01.qualys.com/api/2.0/simple_return.dtd">
# <SIMPLE_RETURN>
#     <RESPONSE>
#         <DATETIME>2019-09-26T09:45:18Z</DATETIME>
#         <TEXT>New search list created successfully</TEXT>
#         <ITEM_LIST>
#             <ITEM>
#                 <KEY>ID</KEY>
#                 <VALUE>1784903</VALUE>
#             </ITEM>
#         </ITEM_LIST>
#     </RESPONSE>
# </SIMPLE_RETURN>"""
# x = XmlParser(xml_data)
# #print(x.get_elements('ITEM_LIST'.__getitem__(0)))
#print(x.get_element_text('//VALUE'))
# print(x.get_all_child_tags_tostring('RESPONSE'))
#print("Total count:", x.get_element_count(".//year"))
#xpath_vat = ".//KEY[text()='REFERENCE']/../VALUE"
#return_val = x.get_element_text(xpath_vat)
