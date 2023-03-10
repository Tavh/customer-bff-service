from kafka import KafkaProducer
from json import dumps

class KafkaPurchaseProducer:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )
        self.topic = topic

    def publish_purchase(self, customer_id, item_id):
        print("publishing message")
        message = {
            'event_type': 'purchase',
            'customer_id': customer_id,
            'item_id': item_id
        }
        self.producer.send(self.topic, value=message)