import praw
from kafka import KafkaProducer
import json

# Reddit API credentials
reddit = praw.Reddit(client_id='6bD3OJevsYkamnfMSpgtMg',
                     client_secret='hy9_StzGddo8ZomO8_e327sO4WZtPw',
                     user_agent='windows:RedditStreamer:1.0')

# Kafka configuration
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Subreddit to stream comments from
subreddit = reddit.subreddit('nba')

for comment in subreddit.stream.comments():
    try:
        # Prepare the message
        message = {'author': str(comment.author), 'body': comment.body}
        
        # Send the message to Kafka topic
        producer.send('topic1', value=message)
        print(f"Sent: {message}")
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"An error occurred: {e}")
