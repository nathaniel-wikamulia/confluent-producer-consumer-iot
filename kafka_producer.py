from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer

kafka_conf = {
    'bootstrap.servers': '<CLOUD CLUSTER BOOTSTRAP SERVER>',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': '<CLOUD CLUSTER API KEY>',
    'sasl.password': '<CLOUD CLUSTER API SECRET>',
}

schema_registry_conf = {
    'url': '<SCHEMA REGISTRY PUBLIC ENDPOINT>',
    'basic.auth.user.info': '<SCHEMA REGISTRY API KEY>:<SCHEMA REGISTRY API SECRET>',
}

key_schema = """
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "DeviceKey",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "device_id": { "type": "string" }
  },
  "required": ["device_id"]
}
"""

# JSON Schema describing your payload
value_schema = """
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "IoTReading",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "device_id": { "type": "string" },
    "sensor_timestamp": { "type": "string" },
    "metrics": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "sensortype": { "type": "string" },
          "sensorvalue": { "type": "number" }
        },
        "required": ["sensortype", "sensorvalue"]
      }
    }
  },
  "required": ["device_id", "sensor_timestamp", "metrics"]
}
"""

iot_data = [
    {
        "device_id": "1",
        "sensor_timestamp": "2025-11-12T09:00:00Z",
        "metrics": [
            {"sensortype": "temperature", "sensorvalue": 36.5},
            {"sensortype": "humidity", "sensorvalue": 55.2}
        ]
    },
    {
        "device_id": "2",
        "sensor_timestamp": "2025-11-12T09:00:10Z",
        "metrics": [
            {"sensortype": "temperature", "sensorvalue": 34.0},
            {"sensortype": "humidity", "sensorvalue": 50.5}
        ]
    },
    {
        "device_id": "4",
        "sensor_timestamp": "2025-11-12T09:00:20Z",
        "metrics": [
            {"sensortype": "temperature", "sensorvalue": 173.3},
            {"sensortype": "humidity", "sensorvalue": 52.1}
        ]
    }
]

sr_client = SchemaRegistryClient(schema_registry_conf)

def key_to_dict(key, ctx):
    if isinstance(key, dict):
        return key
    return {"device_id": str(key)}

key_serializer = JSONSerializer(
    schema_str=key_schema,
    schema_registry_client=sr_client,
    to_dict=key_to_dict
)

def value_to_dict(record, ctx):
    return record

value_serializer = JSONSerializer(
    schema_str=value_schema,
    schema_registry_client=sr_client,
    to_dict=value_to_dict
)

# Create SerializingProducer with key/value serializers
producer_conf = {
    **kafka_conf,
    "key.serializer": key_serializer,
    "value.serializer": value_serializer
}
producer = SerializingProducer(producer_conf)


topic_name = "iot"
# topic_value = iot_data

producer = SerializingProducer(producer_conf)

topic_name = "iot"

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f'Message delivered to "{msg.topic()}" [partition {msg.partition()}] at offset {msg.offset()}')

for record in iot_data:
    producer.produce(
        topic=topic_name,
        key={"device_id": record["device_id"]},
        value=record,
        on_delivery=delivery_report
    )
    producer.poll(0)

producer.flush()




