# Streaming Metric Anomaly Detection

## What is it?
This project serves to conduct various forms of outlier detection on streaming metrics, using Apache Kafka and Spark as the predominant methods of metric storage and analysis.

## Quick Start
### Dependencies 

```
pip3 install kafka-python
pip3 install pyspark
pip3 install matplotlib
pip3 install pandas
pip3 install scikit-learn
pip3 install numpy
pip3 install psutil
```
### Clone the repo
```
git clone https://github.com/SiddharthRajaraman/streamingMetricsAnomolyDetection.git
```

### Deploy Zookeeper and Kafka to Kubernetes Cluster
```
kubectl apply -f kafkaConfig/zookeeper.yaml
kubectl apply -f kafkaConfig/kafkaBroker.yaml
```

### Expose port for Kafka
```
kubectl port-forward <NAME OF KAFKA-BROKER POD> 9092
```

### Run producer
Kafka Producer, by default, sends local CPU metrics every .5 seconds
```
python3 producerFiles/producer.py
```

### Run Consumer
#### DBSCAN
```
python3 consumerFiles/consumerDBSCAN.py
```
#### Kmeans
```
python3 consumerFiles/consumerKmeans.py
```
#### Quartile
```
python3 consumerFiles/consumerQuartile.py
```

