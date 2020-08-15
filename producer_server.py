from kafka import KafkaProducer
import json
import time
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        # with open(self.input_file) as f:
        #     for line in f:
        #         message = self.dict_to_binary(line)
        #         print(message)
        #         # TODO send the correct data
        #         # self.send(self.topic,value=message)
        #         time.sleep(1)
        with open(self.input_file) as json_file:
            records = json.load(json_file)
            count = 0
            for record in records:
                message = self.dict_to_binary(record)
                self.send(self.topic, value=message)
                count += 1
                logger.info("Sending message ==> %s", count)
                print("Sending message ==> %s", count)
                time.sleep(1)


    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')
        