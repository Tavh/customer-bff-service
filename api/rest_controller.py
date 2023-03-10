from flask import Flask, jsonify
from kafka_producer.producer import KafkaPurchaseProducer



class RestController:
    def __init__(self, app: Flask, producer: KafkaPurchaseProducer):
        self.app = app
        self.producer = producer

        self.register_endpoints()

    def register_endpoints(self):
        self.app.route('/customers/<int:customer_id>/purchase/<int:item_id>', methods=['POST'])(self.purchase_item)

    def purchase_item(self, customer_id, item_id):
        self.producer.publish_purchase(customer_id, item_id)
        return jsonify({"message": "Purchase event published to Kafka"})