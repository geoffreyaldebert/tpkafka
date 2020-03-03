from kafka import KafkaConsumer

consumer = KafkaConsumer("sio-topic", bootstrap_servers='localhost:9092', group_id='python')

for message in consumer:
   val  = message.value
   print(val)

