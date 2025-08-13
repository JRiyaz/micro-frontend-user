from kafka import KafkaProducer


class EventProducer:
    def __init__(self, topic: str | None = None):
        # from ..config import config
        # servers = [config.KAFKA_BOOTSTRAP_SERVER]
        servers = ["localhost:9092"]
        self.producer = KafkaProducer(bootstrap_servers=servers)
        self.topic = topic

    def publish(self, topic: str | None, key: str, value: str):
        if not topic:
            topic = self.topic
        self.producer.send(topic, key=key.encode("utf-8"), value=value.encode("utf-8"))

    def close(self):
        if not self.producer:
            return
        self.producer.close()
        self.producer = None


if __name__ == "__main__":
    import time

    event = EventProducer("user")
    for i in range(50):
        data = dict(topic=None, key=f"key-{i + 1}", value="value-{}".format(i + 1))
        print(data)
        event.publish(**data)
        time.sleep(5)
