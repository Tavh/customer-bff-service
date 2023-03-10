from flask import Flask, jsonify
from kafka_producer.producer import KafkaPurchaseProducer

class RestController:
    def __init__(self, app: Flask, producer: KafkaPurchaseProducer):
        """
        Initializes a new instance of the RestController class.

        Args:
            app (Flask): The Flask application instance.
            producer (KafkaPurchaseProducer): The KafkaPurchaseProducer instance to use for publishing purchase events.
        """
        self.app = app
        self.producer = producer

        self.register_endpoints()

    def register_endpoints(self):
        """
        Registers the API endpoints for the RestController class.
        """
        self.app.route('/customers/<int:customer_id>/purchase/<int:item_id>', methods=['POST'])(self.purchase_item)

    def purchase_item(self, customer_id, item_id):
        """
        Publishes a purchase event to Kafka.

        Args:
            customer_id (int): The ID of the customer making the purchase.
            item_id (int): The ID of the item being purchased.

        Returns:
            A JSON response indicating that the purchase event has been published to Kafka.
        """
        self.producer.publish_purchase(customer_id, item_id)
        return jsonify({"message": "Purchase event published to Kafka"})
