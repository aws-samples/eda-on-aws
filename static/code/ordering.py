import hashlib
from datetime import datetime, timedelta

from pprint import pprint as pp


class Consumer:
    def __init__(self) -> None:
        self.__events: [dict] = []

    def __iter__(self):
        return iter(self.__events)

    def receive_event(self, event: dict) -> None:
        self.__events.append(event)

    @property
    def ordered_events(self) -> list:
        data = [item["data"] for item in self.__events]
        return sorted(data, key=lambda x: x["timestamp"])


class MessageBroker:
    def __init__(self) -> None:
        self.__subscribers: [Consumer] = []

    def subscribe(self, consumer: Consumer) -> None:
        self.__subscribers.append(consumer)

    def publish(self, message: dict) -> None:
        for subscriber in self.__subscribers:
            subscriber.receive_event(message)


class Producer:
    def __init__(self, broker: MessageBroker = None) -> None:
        self.__broker = broker or MessageBroker()

    @staticmethod
    def _generate_idempotency_key(data: dict) -> str:
        return hashlib.md5(str(data).encode("utf-8")).hexdigest()

    @staticmethod
    def _generate_payload(data) -> dict:
        idempotency_key = Producer._generate_idempotency_key(data)
        return {"data": data, "metadata": {"idempotency_key": idempotency_key}}

    def publish(self, message) -> None:
        payload = self._generate_payload(message)
        self.__broker.publish(payload)


if __name__ == "__main__":
    now = datetime.utcnow()
    events = [
        {
            "airline": "AWS Airlines",
            "flight_number": "AA-123-f",
            "segment": "departure",
            "event_type": "boarding_completed",
            "timestamp": now - timedelta(seconds=1000),
            "utc_timestamp": (now - timedelta(seconds=1000)).isoformat(),
        },
        {
            "airline": "AWS Airlines",
            "flight_number": "AA-123-f",
            "segment": "departure",
            "event_type": "taxi_started",
            "timestamp": now - timedelta(seconds=100),
            "utc_timestamp": (now - timedelta(seconds=100)).isoformat(),
        },
        {
            "airline": "AWS Airlines",
            "flight_number": "AA-123-f",
            "segment": "departure",
            "event_type": "takeoff",
            "timestamp": now,
            "utc_timestamp": now.isoformat(),
        },
        {
            "airline": "AWS Airlines",
            "flight_number": "AA-123-f",
            "segment": "landing",
            "event_type": "approach_started",
            "timestamp": now + timedelta(seconds=9000),
            "utc_timestamp": (now + timedelta(seconds=9000)).isoformat(),
        },
        {
            "airline": "AWS Airlines",
            "flight_number": "AA-123-f",
            "segment": "landing",
            "event_type": "landed",
            "timestamp": now + timedelta(seconds=9200),
            "utc_timestamp": (now + timedelta(seconds=9200)).isoformat(),
        },
        {
            "airline": "AWS Airlines",
            "flight_number": "AA-123-f",
            "segment": "landing",
            "event_type": "taxi_to_gate",
            "timestamp": now + timedelta(seconds=9239),
            "utc_timestamp": (now + timedelta(seconds=9239)).isoformat(),
        },
    ]

    # swap two events to simulate out of order delivery
    _tmp = events[2]
    events[2] = events[0]
    events[0] = _tmp

    consumer = Consumer()

    broker = MessageBroker()

    client = Producer(broker=broker)
    broker.subscribe(consumer)

    for event in events:
        client.publish(event)

    for event in consumer:
        pp(event)

    pp("----------------------")

    for event in consumer.ordered_events:
        pp(event)
