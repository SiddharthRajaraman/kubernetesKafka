from kafka import KafkaConsumer, KafkaAdminClient


kafkaConsumer = KafkaConsumer(bootstrap_servers = 'localhost:9092')
adminClient = KafkaAdminClient(bootstrap_servers = 'localhost:9092')

def createTopic(topicName, numPartitions, replicationFactor):
    if topicName in kafkaConsumer.topics():
        print('Topic: {} already exists'.format(topicName))
    else:
        adminClient.create_topics(new_topics=[NewTopic(name=topicName, num_partitions=numPartitions, replication_factor=replicationFactor)])
        print('Topic: {} successfully created'.format(topicName))

def deleteTopic(topicName):
    if topicName in kafkaConsumer.topics():
        adminClient.delete_topics(topics=[topicName])
        print('Topic: {} successfully deleted'.format(topicName))        
    else:
        print('Topic: {} does not exists'.format(topicName))

def getPartitions(topicName):
    partitions = kafkaConsumer.partitions_for_topic(topicName)
    return len(partitions)


print(kafkaConsumer.topics())
deleteTopic('test')
print(kafkaConsumer.topics())

