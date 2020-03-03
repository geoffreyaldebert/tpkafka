from kafka import KafkaProducer
import random
import json
import time

producer = KafkaProducer(bootstrap_servers="localhost:9092")

cpt = 0

while True :
    cpt = cpt + 1
    rd = random.randint(0,100)
    record = "{'id':"+str(cpt)+",'value':"+str(rd)+"}"
    producer.send("sio-topic", json.dumps(record).encode())
    time.sleep(1)

