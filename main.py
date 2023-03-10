from flask import Flask
from kafka_producer.producer import KafkaPurchaseProducer
from api.rest_controller import RestController
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')
bootstrap_servers = config['kafka']['bootstrap_servers']

app = Flask(__name__)

producer = KafkaPurchaseProducer(bootstrap_servers=bootstrap_servers)
rest_controller = RestController(app=app, producer=producer)

rest_controller.register_endpoints()
