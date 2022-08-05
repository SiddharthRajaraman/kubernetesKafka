from kafka import KafkaConsumer
from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN

kafkaConsumer = KafkaConsumer('myTopic', bootstrap_servers='localhost:9092', auto_offset_reset = 'earliest')



def convertToPandasDf(metricList):
    return pd.DataFrame(metricList, columns = ['metrics'])


metricList = [] #will hold metrics received from kafka topic
metricListDf = convertToPandasDf(metricList)

plt.ion()
for message in kafkaConsumer:
    metricList.append(float(message.value.decode('utf-8')))
    metricListDf = convertToPandasDf(metricList)


    if len(metricList) < 100:
        plt.scatter(len(metricList) - 1, metricList[-1], c = "black")
        plt.draw()
        plt.pause(.1)
    else:
        model = DBSCAN(eps = 1, min_samples = 2).fit(metricListDf)

        colors = model.labels_
        
        outliers = metricListDf[model.labels_ == -1]

        index = outliers.index

        plt.scatter(range(len(metricListDf)), metricListDf, c = colors)
        plt.scatter(index, outliers, color = 'blue')
        plt.draw()
        plt.pause(.1)