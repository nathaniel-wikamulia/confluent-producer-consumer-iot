from confluent_kafka import KafkaException, KafkaError
from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONDeserializer

kafka_conf = {
    'bootstrap.servers': '<CLOUD CLUSTER BOOTSTRAP SERVER>',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': '<CLOUD CLUSTER API KEY>',
    'sasl.password': '<CLOUD CLUSTER API SECRET>',
    'group.id': 'my-consumer-group-2',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': True
}


sr_conf = {
    'url': '<SCHEMA REGISTRY PUBLIC ENDPOINT>',
    'basic.auth.user.info': '<SCHEMA REGISTRY API KEY>:<SCHEMA REGISTRY API SECRET>',
}
sr_client = SchemaRegistryClient(sr_conf)

value_schema = sr_client.get_latest_version('alert_topic-value').schema
value_deserializer = JSONDeserializer(value_schema.schema_str)

key_schema = sr_client.get_latest_version('alert_topic-key').schema
key_deserializer = JSONDeserializer(key_schema.schema_str)

consumer_conf = {
    **kafka_conf,
    'key.deserializer': key_deserializer,
    'value.deserializer': value_deserializer
}

consumer = DeserializingConsumer(consumer_conf)
consumer.subscribe(['alert_topic'])

print("Consumer started. Waiting for messages...\n")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f"End of partition: {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                continue
            raise KafkaException(msg.error())

        key_obj = msg.key()
        val_obj = msg.value()   

        print(f"Received from '{msg.topic()}' [p={msg.partition()} o={msg.offset()}]")
        print(f"Key:   {key_obj}")
        print(f"Value: {val_obj}")
        print("-" * 60)

except KeyboardInterrupt:
    print("\nConsumer interrupted by user")
finally:
    consumer.close()
    print("Consumer closed.")
