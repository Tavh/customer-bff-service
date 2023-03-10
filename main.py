from flask import Flask
from kafka_producer.producer import KafkaPurchaseProducer
from api.rest_controller import RestController


app = Flask(__name__)

producer = KafkaPurchaseProducer("localhost:9092")
rest_controller = RestController(app=app, producer=producer)

rest_controller.register_endpoints()
