from kafka import KafkaConsumer
from hdfs import InsecureClient
from json import dump, dumps
import json

client = InsecureClient('http://sandbox-hdp.hortonworks.com:50070')

consumer = KafkaConsumer("sio-topic", bootstrap_servers='localhost:9092', group_id='python')

records = json.loads('[{}]') 

cpt = 0
cpt2 = 0

for message in consumer:
   records.append(message.value.decode())
   val = message.value
   print(val)
   cpt = cpt + 1
   cpt2 = cpt2 + 1
   if cpt == 10:
      client.write('/user/root/data/records'+str(cpt2)+'.json', data=dumps(records), encoding='utf-8')
      cpt = 0

