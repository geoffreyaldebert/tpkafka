from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('sio-topic', b'HELLO SIO')
producer.flush()
