#!/usr/bin/env python3
"""This will publish messages to pubsub once every few seconds."""
import json
import os
from pprint import pprint
import random
from time import sleep
import uuid

from kafka import KafkaProducer

TOPIC_NAME = os.getenv("TOPIC_NAME", "roman")


def publish():
    """This will connect to kafka and publish messages."""
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        batch_size=0,
        retries=3,
        acks=1,
        value_serializer=serialize,
    )

    while True:
        message = get_random_message()
        producer.send(topic=TOPIC_NAME, value=message)
        print(f"I sent this message!")
        pprint(message)
        sleep(2)


def get_random_message() -> dict:
    """Generate some fake dictionary of data."""
    return {
        "name": random.choice(
            [
                "Bugs Bunny",
                "Spongebob Squarepants",
                "Jimmy Neutron",
                "Simpsons",
                "Recess",
                "Tiger King",
            ]
        ),
        "season": random.randint(1, 100),
        "episode": random.randint(1, 22),
        "rating": round(random.random(), 2),
        "view_id": str(uuid.uuid4()),
    }


def serialize(message: dict) -> bytes:
    """Turns string to bytes"""
    return json.dumps(message).encode("utf-8")


if __name__ == "__main__":
    publish()
