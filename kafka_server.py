from confluent_kafka.admin import AdminClient
from confluent_kafka.cimpl import NewTopic

import producer_server
from kafka.client import KafkaClient
import logging


BROKER_URL = "localhost:9092"
TOPIC = "com.sfo.crimes.calls"
CLIENT_ID = "sfo-crime-data-produce"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def run_kafka_server():
	# TODO get the json file path
    input_file = "data/police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic=TOPIC,
        bootstrap_servers=BROKER_URL,
        client_id=CLIENT_ID
    )

    return producer

def create_topic_if_not_existing():
    client = KafkaClient(bootstrap_servers='localhost:9092')
    future = client.cluster.request_update()
    client.poll(future=future)

    metadata = client.cluster
    if TOPIC in metadata.topics():
        logger.info("Topic already existing %s", TOPIC)
    else:
        create_topic()

def create_topic():
    """Creates the producer topic if it does not already exist"""
    # Creates the topic
    logger.info("Creating topic %s", TOPIC)
    try:
        client = AdminClient({'bootstrap.servers': BROKER_URL})
        topic = NewTopic(TOPIC, num_partitions=1, replication_factor=1)
        client.create_topics([topic])
        logger.info("Topic created successfully")
    except Exception as e:
        logger.error("failed to create topic %s, error : %s", TOPIC, e)
        raise

def feed():
    create_topic_if_not_existing()
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
