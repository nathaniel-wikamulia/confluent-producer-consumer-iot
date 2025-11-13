# Introduction to Producer and Consumer
In this repository, you will learn how to create a Python Kafka producer, send IoT data to Confluent Cloud, process the data using Flink, create a Python Kafka consumer, and consume the processed data with the consumer.

## Prerequisites
1. Download the code from this repository.
2. Install the Confluent Kafka Python client along with optional JSON Schema and performance dependencies:
```
pip install confluent-kafka
python3 -m pip install -U "confluent-kafka[jsonschema]" referencing
python3 -m pip install -U "confluent-kafka[jsonschema]" jsonschema referencing rpds-py
python3 -m pip install -U orjson
```

## Step 1 - Login to Confluent Cloud
1. Log in to [Confluent Cloud](https://confluent.cloud) and enter your email and password. If you don't have an account you can sign up [here](https://www.confluent.io/confluent-cloud/tryfree/).

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

## Step 4 - Create an Apache Kafka topic
After creating a Confluent Cloud cluster, we'll create a new Apache Kafka topic called "iot".

Topics are the core abstraction for storing and processing data. Unlike traditional databases where data is stored in tables and updated with each new event, Kafka uses logs to record every event in sequence.

To create a topic, follow the steps below:
1. Click the previously provisioned Confluent Cloud cluster.
2. In the left-hand menu, select "Topics".
3. Click the "Add topic" button on the right side of the page.
4. Enter a name for your cluster. For this workshop, we’ll use "iot".
5. Click on the "Create with defaults" button.

## Step 5 - Run the Apache Kafka producer

## Step 6 - Run the Apache Kafka producer

## Step 7 - Run the Apache Kafka producer


## Step 8 - Create a Flink Compute Pool

## Step 9 - Run a Transformation Query using Flink

## Step 10 - Run the Apache Kafka consumer
