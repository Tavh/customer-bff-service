from kafka import KafkaProducer
from json import dumps
from util.logger import get_logger


class KafkaPurchaseProducer:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.logger = get_logger(__name__)
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )
        self.topic = topic

    def publish_purchase(self, customer_id, item_id):
        message = {
            'event_type': 'purchase',
            'customer_id': customer_id,
            'item_id': item_id
        }
        self.logger.info(f"producing message: {message}\n to topic: {self.topic}")
        self.producer.send(self.topic, value=message)
        self.producer.flush()