import json
import sys

from src.ConfigParser import ConfigParser
from kafka import KafkaProducer
from kafka import KafkaConsumer
from src.XmlParser import XmlParser


class KafkaClient(object):

    def __init__(self, config_file):
        self.kafka_host = ConfigParser(config_file).safe_get('KAFKA', 'KAFKA_HOST')
        self.message_unique_key = ConfigParser(config_file).safe_get('QA.UNIQUE_KEY', 'UNIQUE_KEY')

    def kafka_producer(self, topic, jsonData):
        print(self.kafka_host)
        self.kafka_topic_producer = topic
        print(self.kafka_topic_producer)
        producer = KafkaProducer(bootstrap_servers=self.kafka_host)
        self.message = jsonData
        print(self.message)
        future = producer.send(self.kafka_topic_producer, bytes(self.message, 'utf-8'))
        try:
            record_metadata = future.get(timeout=10)
        except KafkaError:
            pass

        print("Meesage sent on Topic : " + record_metadata.topic + " Partition: " + str(
            record_metadata.partition) + " Offset: " + str(record_metadata.offset))
        producer.flush()
        producer.close()

    def kafka_consumer(self, topic):
        self.kafka_topic_consumer = topic

        # consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_HOST, group_id='my-group',
        #                         consumer_timeout_ms=10000, auto_offset_reset='earliest', enable_auto_commit=True)
        try:
            consumer = KafkaConsumer(self.kafka_topic_consumer, bootstrap_servers=self.kafka_host, group_id='my-vmsp-1',
                                     consumer_timeout_ms=50000, auto_offset_reset='latest', enable_auto_commit=True)
        except KafkaError:
            consumer.close()
            pass
        return consumer

    def consume_unified_message(self, topic, id):
        consumed_unified_messages = self.kafka_consumer(topic)
        self.correlation_id = id
        print('Consumer started! for ID:' + self.correlation_id)
        self.consumed_message = None
        self.success_message = None
        for unified_message in consumed_unified_messages:
            self.consumed_message = None
            self.success_message = None
            decoded_data = unified_message.value.decode("utf-8")
            self.consumed_message = json.loads(decoded_data)
            producer_id = self.consumed_message[self.message_unique_key]
            source = self.consumed_message["source"]
            if (producer_id == self.correlation_id and source == "QWEB"):
                print(producer_id)
                self.success_message = self.consumed_message
                consumed_unified_messages.close()
                break
        print('Consumer stopped     !!! ')
        return self.success_message

    def consume_hds_message(self, topic, host_id):
        consumed_hds_messages = self.kafka_consumer(topic)
        self.correlation_id = host_id
        print('Consumer started! for ID:' + self.correlation_id)
        self.consumed_message = None
        self.success_message = None
        for hds_message in consumed_hds_messages:
            self.consumed_message = hds_message.value.decode("utf-8")
            self.success_message = None
            print(self.consumed_message)
            xml_host_id = XmlParser(self.consumed_message).get_element_text('//USER_HOST_ID')
            if xml_host_id == host_id:
                print("XML HostID:" + str(xml_host_id))
                self.success_message = self.consumed_message
                consumed_hds_messages.close()
                break
        print('Consumer stopped     !!! ')
        return self.success_message
