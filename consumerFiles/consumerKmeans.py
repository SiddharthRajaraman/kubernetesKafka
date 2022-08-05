from kafka import KafkaConsumer
from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from numpy import sqrt, random, array, argsort



kafkaConsumer = KafkaConsumer('myTopic', bootstrap_servers='127.0.0.1:9092', auto_offset_reset = 'earliest')

def convertToPandasDf(metricList):
    return pd.DataFrame(metricList, columns = ['metrics'])


metricList = [] #will hold metrics received from kafka topic
metricListDf = convertToPandasDf(metricList)

plt.ion()
for message in kafkaConsumer:
    metricList.append(float(message.value.decode('utf-8')))
    metricListDf = convertToPandasDf(metricList)
    metricListDf = metricListDf.to_numpy()
    temp = metricListDf


    if len(metricList) > 100:
        metricListDf = scale(metricListDf)

        kmeans = KMeans(n_clusters = 1).fit(metricListDf)
        center = kmeans.cluster_centers_


        distance = sqrt((metricListDf - center)**2)

        order_index = argsort(distance, axis = 0)
        indexes = order_index[-20:]

        values = temp[indexes]


        if indexes[len(indexes) - 1] == len(temp) - 1:
            plt.scatter(len(temp) - 1, temp[len(temp) - 1], color = 'red')
        else:
            plt.scatter(len(temp) - 1, temp[len(temp) - 1], color = 'black')
        plt.show()
        plt.pause(.1)
    else:
        plt.scatter(len(temp) - 1, temp[len(temp) - 1], color = 'black')
        plt.show()
        plt.pause(.1)        




