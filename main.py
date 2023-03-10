from flask import Flask, jsonify
from kafka_producer.producer import KafkaPurchaseProducer

from json import dumps


app = Flask(__name__)

producer = KafkaPurchaseProducer("localhost:9092")

@app.route('/customers/<int:customer_id>/purchase/<int:item_id>', methods=['POST'])
def publish_purchase(customer_id, item_id):
    producer.publish_purchase(customer_id, item_id)
    return jsonify({"message": "Purchase event published to Kafka"})

print("hi")