# Kafka Local

This is a local development version of kafka running on docker compose.

## Running this code

### Launcing Kafka

Launch with

- `./up.sh`

Bring down with

- `./down.sh`

### Executing Python Clients

After installing the `requirements.txt` then, create topic with

- `./create_topic.py`

Publish data using to topic

- `./publisher/publish.py`

Subscribe to topic data using

- `./subscriber/subscribe.py`
