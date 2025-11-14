# Introduction to Producer and Consumer
In this repository, you will learn how to create a Python Kafka producer, send IoT data to Confluent Cloud, process the data using Flink, create a Python Kafka consumer, and consume the processed data with the consumer.
<br><br>
## Prerequisites
1. Download the code from this repository.
2. Install the Confluent Kafka Python client along with optional JSON Schema and performance dependencies:
```
pip install confluent-kafka
python3 -m pip install -U "confluent-kafka[jsonschema]" referencing
python3 -m pip install -U "confluent-kafka[jsonschema]" jsonschema referencing rpds-py
python3 -m pip install -U orjson
```
<br\>
## Step 1 - Login to Confluent Cloud
1. Log in to [Confluent Cloud](https://confluent.cloud) and enter your email and password. If you don't have an account you can sign up [here](https://www.confluent.io/confluent-cloud/tryfree/).
<br><br>
## Step 2 - Create a Confluent Cloud Environment
In this step, we will create a new Environment.

A Confluent Cloud environment is a logical grouping within your Confluent Cloud organization that serves as a container for your Kafka clusters and related components such as Connect, ksqlDB, Schema Registry, and Flink compute pools.

You can create multiple environments within a single organization at no additional cost. This setup allows different teams or departments to work in separate environments, ensuring isolation and preventing interference between workloads.

Steps to create an environment:
1. On the Confluent Cloud home screen, click "Environments" in the left-hand menu.
2. Click the "Add cloud environment" button on the right side of the page.
3. Enter a name for your environment. For this workshop, we’ll use "demo_environment".
4. For the Stream Governance package, select "Essentials".
5. Click "Create" to finish setting up your environment.
<br><br>
## Step 3 - Create a Confluent Cloud Cluster
Once you have created an environment, you can proceed to create a Confluent Cloud cluster.

A Confluent Cloud cluster is a fully managed Apache Kafka cluster that runs in the cloud and is hosted and maintained by Confluent. it's where your Kafka topics, producers, and consumers live and interact. The cluster handles all the data streaming activity, such as: producing, storing, and consuming messages in real time.

We'll create a Confluent Cloud cluster with the following specifications:
- Cluster type: Basic
- Cloud provider: Azure
- Cloud provider region: Singapore (southeastasia)
- Availability: Single zone
- Cluster name: azure_cluster

To create the cluster you can follow these steps below:
1. Click on your newly created environment to open it.
2. In the left-hand menu, select "Clusters".
3. Click the "Add cluster" button on the right side of the page.
4. Under the Basic cluster option, click the "Begin configuration" button.
5. Choose your preferred cloud provider. For this workshop, we'll use "Azure", and for the region, we'll choose Singapore (southeastasia).
6. Enter a name for your cluster. For this workshop, we’ll use "azure_cluster".
7. Click the "Launch cluster" button to create your cluster.
<br><br>
## Step 4 - Create an Apache Kafka topic
After creating a Confluent Cloud cluster, we'll create a new Apache Kafka topic called "iot".

Topics are the core abstraction for storing and processing data. Unlike traditional databases where data is stored in tables and updated with each new event, Kafka uses logs to record every event in sequence.

To create a topic, follow the steps below:
1. Click the previously provisioned Confluent Cloud cluster.
2. In the left-hand menu, select "Topics".
3. Click the "Add topic" button on the right side of the page.
4. Enter a name for your cluster. For this workshop, we’ll use "iot".
5. Click on the "Create with defaults" button.
<br><br>
## Step 5 - Create a Cluster API Key and API Secret
Now we need to generate a Kafka cluster API key and secret, which we’ll use later to authenticate our producer and consumer with our Kafka cluster.

A Kafka cluster API key is used to authenticate and authorize access to your Kafka clusters from external applications, scripts, or tools. In simple terms, it’s like a username and password for your application to connect securely to your Confluent Cloud Kafka cluster.

To generate a Kafka Cluster API key and secret, follow the steps below:
1. In the left-hand menu, select the "API keys" option.
2. Click the "Add key" button on the right side of the page.
3. Click on the "My account" button, then click the "Next" button.
4. Click the "Download and continue" button.

Now a download will begin. You’ll receive a ".txt" file containing your API key, API secret, cluster ID, and bootstrap server. Keep this file and your credentials private, they are equivalent to a username and password. If exposed, external actors could use them to access or misuse the data and resources in your Confluent Cloud account.

**Note: After you download your API key and secret and exit this menu, they will no longer be visible in the console. You can only access them from the ".txt" file you just downloaded, so make sure not to lose it.**
<br><br>
## Step 6 - Create a Schema Registry API Key and API Secret
Next, we need to generate a Schema Registry API key and secret, which will be used later to authenticate our producer and consumer with the Schema Registry.

The Schema Registry in Confluent Cloud stores and manages data schemas for Kafka producers and consumers. It ensures that the structure of messages flowing through Kafka topics remains consistent, compatible, and well-defined, preventing data format errors between applications.

Note that the Schema Registry requires its own API key and secret, separate from the Kafka cluster credentials. These are used specifically to authenticate your applications with the Schema Registry service.

To generate a Schema Registry API key and secret, follow the steps below:
1. Click the hamburger menu in the top-right corner of the page.
2. Select the "API keys" option.
3. Click the "Add API key" button on the right side of the page.
4. Click on the "My account" button, then click the "Next" button.
5. Click the “Schema Registry” button, select “demo_environment” from the dropdown menu, and then click “Next”.
6. Add a name and description to help identify this API key in the future. For this workshop, we’ll use “demo_environment_sr_api_key” for both the name and description, but feel free to provide a more descriptive label if you prefer.
7. After adding the name and the description, click the "Create API key" button.
8. Click on the "Download API key" button.

Just like the Kafka Cluster API key and secret, keep this file and your credentials private, they are equivalent to a username and password. If exposed, unauthorized users could access or misuse the data and resources in your Confluent Cloud account.

**Note: After you download your API key and secret and exit this menu, they will no longer be visible in the console. You can only access them from the ".txt" file you just downloaded, so make sure not to lose it.**
<br><br>
## Step 7 - Run the Apache Kafka producer
Once you have the API key and secret for the Cluster and Schema Registry, you can start creating the Kafka producer.

A Kafka producer is an application or client that sends (or “produces”) messages to Kafka topics. To create an Apache Kafka producer, you can follow the steps below:
1. Open the "kafka_producer.py" file.
2. Replace the "`<CLOUD CLUSTER BOOTSTRAP SERVER>`" string in the "kafka_producer.py" file using the "Bootstrap server" information from the ".txt" file you downloaded in Step 5.
3. Replace the "`<CLOUD CLUSTER API KEY>`" string in the "kafka_producer.py" file using the "API key" information from the ".txt" file you downloaded in Step 5.
4. Replace the "`<CLOUD CLUSTER API SECRET>`" string in the "kafka_producer.py" file using the "API secret" information from the ".txt" file you downloaded in Step 5.
5. Replace the "`<SCHEMA REGISTRY PUBLIC ENDPOINT>`" string in the "kafka_producer.py" file using the "Endpoint" information from the ".txt" file you downloaded in Step 6.
6. Replace the "`<SCHEMA REGISTRY API KEY>`" string in the "kafka_producer.py" file using the "API key" information from the ".txt" file you downloaded in Step 6.
7. Replace the "`<SCHEMA REGISTRY API SECRET>`" string in the "kafka_producer.py" file using the "API secret" information from the ".txt" file you downloaded in Step 6.
8. Open a terminal in the directory where your "kafka_producer.py" file is located.
9. Run the following command to execute the "kafka_producer.py" script:
```
python3 kafka_producer.py  
```
10. If you see a message similar to the one below, you have successfully sent data to the "iot" Kafka topic:
```
Message delivered to "iot" [partition 0] at offset 35
```
<br><br>
## Step 8 - Create a Flink Compute Pool
Now that the "iot" topic is filled with messages, we can start creating a Flink compute pool.

A Flink compute pool in Confluent Cloud for Apache Flink represents a set of compute resources bound to a region that is used to run your SQL statements. The resources provided by a compute pool are shared between all statements that use it. The capacity of a compute pool is measured in CFUs.
To create an Flink compute pool, you can follow the steps below:
1. In the left-hand menu, select "Flink".
2. Click the "Add compute pool" button on the right side of the page.
3. Choose your preferred cloud provider. For this workshop, we'll use "Azure", and for the region, we'll choose Singapore (southeastasia). Please note that the Flink compute pool must match the Kafka cluster's region.
4. Enter a name for your compute pool. For this workshop, we’ll use "azure_flink_compute_pool".
5. Set the "Max size" value to 10 CFU.
6. Click the "Create" button to create your compute pool.
<br><br>
## Step 9 - Run a Transformation Query using Flink
Once the Flink compute pool has been provisioned, you can begin writing Flink queries. Follow the steps below to get started:
1. Click the "Open SQL workspace" button on the right side of the page.
2. Open the "Catalog" dropdown in the top-right corner and select "demo_environment" to access your previously provisioned environment.
3. Open the "Database" dropdown in the top right corner and choose "azure_cluster" to access your previously provisioned Kafka cluster.
4. Paste the following Flink query into an empty cell:
```
CREATE TABLE alert_topic
DISTRIBUTED BY (device_id) INTO 6 BUCKETS
WITH (
  'key.format' = 'json-registry',
  'value.format' = 'json-registry'
)
AS
WITH expanded_metrics AS (
  SELECT
    device_id,
    sensor_timestamp,
    u.sensortype  AS metric_type,
    u.sensorvalue AS metric_value
  FROM iot
  CROSS JOIN UNNEST(metrics) AS u
)
SELECT 
  device_id,
  CONCAT(
    'Alert! the temperature of device_id ',
    device_id,
    ' is ',
    CAST(metric_value AS STRING),
    ' degrees Celsius'
  ) AS alert_msg
FROM expanded_metrics
WHERE metric_type = 'temperature' 
  AND metric_value > 100;
```
5. Click the "Run" button on the right side of the cell.
6. After you execute the Flink query, it will begin inserting the filtered data into a new Kafka topic called "alert_topic". If you see messages appearing in "alert_topic", it means your query ran successfully.
<br><br>
## Step 10 - Run the Apache Kafka consumer
In this step, we will start consuming data from the "alert_topic" using a Kafka consumer written in Python.

A Kafka consumer is an application or client that reads (or “consumes”) messages from Kafka topics. To create an Apache Kafka consumer, you can follow the steps below:
1. Open the "kafka_consumer.py" file.
2. Replace the "`<CLOUD CLUSTER BOOTSTRAP SERVER>`" string in the "kafka_consumer.py" file using the "Bootstrap server" information from the ".txt" file you downloaded in Step 5.
3. Replace the "`<CLOUD CLUSTER API KEY>`" string in the "kafka_consumer.py" file using the "API key" information from the ".txt" file you downloaded in Step 5.
4. Replace the "`<CLOUD CLUSTER API SECRET>`" string in the "kafka_consumer.py" file using the "API secret" information from the ".txt" file you downloaded in Step 5.
5. Replace the "`<SCHEMA REGISTRY PUBLIC ENDPOINT>`" string in the "kafka_consumer.py" file using the "Endpoint" information from the ".txt" file you downloaded in Step 6.
6. Replace the "`<SCHEMA REGISTRY API KEY>`" string in the "kafka_consumer.py" file using the "API key" information from the ".txt" file you downloaded in Step 6.
7. Replace the "`<SCHEMA REGISTRY API SECRET>`" string in the "kafka_consumer.py" file using the "API secret" information from the ".txt" file you downloaded in Step 6.
8. Open a terminal in the directory where your "kafka_consumer.py" file is located.
9. Run the following command to execute the "kafka_consumer.py" script:
```
python3 kafka_consumer.py  
```
10. If you see a message similar to the one below, you have successfully consumed data from the "alert_topic":
```
Received from 'alert_topic' [p=4 o=14]
Key:   {'device_id': '4'}
Value: {'alert_msg': 'Alert! the temperature of device_id 4 is 173.3 degrees Celsius'}
------------------------------------------------------------
```
<br><br>
## Step 11 - Clean Up Your Confluent Cloud Resources
To prevent your Confluent Cloud resources from incurring unnecessary costs, perform the following actions:
1. Stop any running Flink query.
2. Delete the Flink compute pool.
3. Delete the Schema Registry data contracts.
4. Delete the Kafka Cluster API key and secret.
5. Delete the Schema Registry API key and secret.
6. Delete the Kafka cluster.
<br><br>
## Additional Resources
For additional Confluent Cloud courses, you can find the next course [here](https://developer.confluent.io/courses/apache-kafka/get-started-hands-on/). 
