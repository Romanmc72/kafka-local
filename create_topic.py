#!/usr/bin/env python3
"""This creates the topic if it does not yet exist."""
import os

from kafka.admin import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

TOPIC_NAME = os.getenv("TOPIC_NAME", "roman")


def create_topic(topic_name: str = TOPIC_NAME):
    """Creating a topic"""
    admin_client = KafkaAdminClient(bootstrap_servers=["localhost:9092"])

    topic_list = []
    topic_list.append(NewTopic(name=topic_name, num_partitions=1, replication_factor=1))
    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
    except TopicAlreadyExistsError:
        print("Topic already exists.")
        return None
    print("Created topic.")


if __name__ == "__main__":
    create_topic()
