Assignment 3 Part 1 README - Real-Time Named Entity Recognition with Apache Kafka and Spark

This project demonstrates real-time data processing using Apache Kafka and PySpark. It reads text data from the NBA subreddit, analyzes text for named entities, and sends their counts to a Kafka topic, which is then visualized using Elasticsearch and Kibana.

Prerequisites

Ensure you have the following installed:
- Python 3.x
- Apache Kafka
- Apache Spark
- Elasticsearch and Kibana
- Logstash

Python Libraries:
- pyspark
- spacy
- pandas
- jupyter-notebook
- praw
- json

These can be installed using pip:
pip install pyspark spacy pandas jupyter-notebook praw json

Additionally, download the necessary Spacy language model:
python -m spacy download en_core_web_sm

Setup Instructions

1. Start Zookeeper Service

Zookeeper is required to run Kafka. Open a terminal and execute:
bin/zookeeper-server-start.sh config/zookeeper.properties

2. Start Kafka Server

Open another terminal and start the Kafka server:
bin/kafka-server-start.sh config/server.properties

3. Stream Data from Reddit to Kafka

The reddit_to_kafka.py script streams data from the NBA subreddit to Kafka topic1. Run this script in a new terminal:
python reddit_to_kafka.py

4. Process Data with PySpark

Open the writer_topic2.ipynb in Jupyter Notebook to process the incoming data and write the named entity counts to Kafka topic2.
jupyter-notebook writer_topic2.ipynb

5. Start Elasticsearch

Run Elasticsearch from its bin directory:
bin/elasticsearch

6. Start Kibana

After starting Elasticsearch, run Kibana:
bin/kibana

7. Start Logstash

Use Logstash to pull data from Kafka topic2 into Elasticsearch. Use the provided logstash.conf file:
bin/logstash -f logstash.conf

8. Visualize Data with Kibana

Once Elasticsearch and Kibana are running, use Kibana to create visualizations for the data as needed.

