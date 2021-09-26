#!/usr/bin/env python3
"""This will consume messages and print them to the terminal."""
import json
import os
from pprint import pprint

from kafka import KafkaConsumer

TOPIC_NAME = os.getenv("TOPIC_NAME", "roman")


def consume():
    """This is the method that grabs the messages."""
    consumer = KafkaConsumer(
        TOPIC_NAME, bootstrap_servers=["localhost:9092"], value_deserializer=deserialize
    )

    for message in consumer:
        print("Pulled this message:")
        pprint(message.value)
        print(f"Offset: {message.offset}")


def deserialize(message: bytes) -> dict:
    """Deserializes the data to a python object."""
    return json.loads(message.decode("utf-8"))


if __name__ == "__main__":
    consume()
