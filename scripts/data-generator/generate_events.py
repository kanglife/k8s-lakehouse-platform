import json
import random
from datetime import datetime
import boto3

print("=== Sprint 2: data generator started ===")

BUCKET_NAME = "k8s-lakehouse-raw"
EVENT_COUNT = 1000

s3 = boto3.client("s3")

def generate_event():
    return {
        "user_id": random.randint(1, 100),
        "event_type": random.choice(["view", "click", "purchase"]),
        "page": f"/product/{random.randint(1, 50)}",
        "event_time": datetime.utcnow().isoformat()
    }

def main():
    events = [generate_event() for _ in range(EVENT_COUNT)]

    today = datetime.utcnow().strftime("%Y-%m-%d")
    key = f"events/date={today}/events.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(events),
        ContentType="application/json"
    )

    print(f"[SUCCESS] Uploaded {EVENT_COUNT} events")
    print(f"s3://{BUCKET_NAME}/{key}")

if __name__ == "__main__":
    main()
