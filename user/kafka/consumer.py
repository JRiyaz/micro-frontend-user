from kafka import KafkaConsumer


class Consumer:
    def __init__(self, topic: str):
        # from ..config import config
        # servers = [config.KAFKA_BOOTSTRAP_SERVER]
        servers = ["localhost:9092"]
        self.topic = topic
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=servers,
            auto_offset_reset="earliest",
            enable_auto_commit=False,
        )

    def consume(self):
        for message in self.consumer:
            print(message)


if __name__ == "__main__":
    consumer = Consumer("user")
    consumer.consume()
