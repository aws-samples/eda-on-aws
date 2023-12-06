import hashlib

from typing import Optional, Dict

from dataclasses import dataclass

NOTSTARTED = "NOTSTARTED"
INPROGRESS = "INPROGRESS"
COMPLETED = "COMPLETED"


@dataclass
class EventState:
    status: str
    idempotency_key: str
    results: Optional[dict] = None

    def is_inprogress(self):
        return self.status == INPROGRESS

    def is_completed(self):
        return self.status == COMPLETED


IN_MEMORY_DATASTORE: Dict[str, EventState] = {}


def _generate_idempotency_key(data):
    return hashlib.md5(str(data).encode("utf-8")).hexdigest()


def generate_user_payload(data):
    # Step 1. The client generates the idempotency key and adds it to the event payload.
    idempotency_key = _generate_idempotency_key(data)
    return {"data": data, "metadata": {"idempotency_key": idempotency_key}}


def process_user_payload(payload: dict):
    data = payload["data"]
    # Step 3. The consumer extracts the idempotency_key
    idempotency_key: str = payload["metadata"]["idempotency_key"]

    # Step 3. Fetch event state from data store
    event_state = _fetch_event_state(idempotency_key)

    # Step 4. If the key exists in the data store, stop
    if event_state.is_inprogress():
        raise Exception("Event in progress")
    elif event_state.is_completed():
        print("Event already completed. Returning results.")
        return event_state.results

    # Step 5. When the key doesn't exist, mark the event state as in progress in the data store
    _persist_event_state(event_state, INPROGRESS)

    # Step 6. Run the application code/business logic
    results = run_business_logic(data)

    # Step 7. Save the results and mark this event state as completed and persist
    _persist_function_results(event_state, results)

    return event_state.results


def _fetch_event_state(idempotency_key: str) -> EventState:
    return IN_MEMORY_DATASTORE.get(idempotency_key) or EventState(
        NOTSTARTED, idempotency_key
    )


def _persist_event_state(event_state: EventState, status: str) -> None:
    event_state.status = status
    IN_MEMORY_DATASTORE[event_state.idempotency_key] = event_state


def _persist_function_results(event_state: EventState, results: dict) -> None:
    event_state.results = results
    _persist_event_state(event_state, COMPLETED)


def run_business_logic(data: dict) -> dict:
    # This would run your application logic. In this example, just return the data.
    return data


if __name__ == "__main__":
    data_items = [
        {
            "name": "John Smith",
            "age": 45,
            "city": "New York",
            "country": "USA",
            "job": "Software Engineer",
        },
        {
            "name": "Jane Doe",
            "age": 30,
            "city": "Seattle",
            "country": "USA",
            "job": "Engineering Manager",
        },
    ]

    for data in data_items:
        # Step 1. Prepare the payload
        payload = generate_user_payload(data)
        # Step 2. Note there is no step 2 since this example code doesn't need to publish.
        # If there was an event broker the publish step would be here.

        # Steps 3-7. This function makes up what happens within the data consumer. In a real
        # distributed system, this would be a different process.
        process_user_payload(payload)
        process_user_payload(payload)
