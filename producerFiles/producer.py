from kafka import KafkaProducer
import time
import psutil


kafkaProducer = KafkaProducer(bootstrap_servers='localhost:9092')

topicName = "myTopic"


counter = 0

while True:
    msg = kafkaProducer.send(topicName, key = str(counter).encode('utf-8'), value = str(psutil.cpu_percent()).encode('utf-8')).get()

    print("topic: ", msg.topic)
    print("partition: ", msg.partition)

    time.sleep(.5)
