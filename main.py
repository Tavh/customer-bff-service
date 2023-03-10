import os

from flask import Flask
from kafka_producer.producer import KafkaPurchaseProducer
from api.rest_controller import RestController


# Get configuration from environment variables
bootstrap_servers = os.environ['BOOTSTRAP_SERVERS']
topic = os.environ['TOPIC']

print(f"bootstrap_servers: {bootstrap_servers}, topic: {topic}")

app = Flask(__name__)

producer = KafkaPurchaseProducer(bootstrap_servers=bootstrap_servers, topic=topic)
rest_controller = RestController(app=app, producer=producer)

rest_controller.register_endpoints()

if __name__ == "__main__":
    app.run(debug=True)