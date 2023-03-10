from kafka import KafkaProducer
from json import dumps

class KafkaPurchaseProducer:
    def __init__(self, kafka_bootstrap_servers):
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_bootstrap_servers,
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )

    def publish_purchase(self, customer_id, item_id):
        message = {
            'event_type': 'purchase',
            'customer_id': customer_id,
            'item_id': item_id
        }
        self.producer.send('purchases', value=message)