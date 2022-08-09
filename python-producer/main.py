from faker import Faker
from kafka import KafkaProducer
import json
import time

fake = Faker()

def get_registered_data():
    
    data = {
        'first name': fake.first_name(),
        'last name': fake.last_name(),
        'age': fake.random_int(0, 60),
        'address': fake.address(),
        'register year': fake.year(),
        'register month': fake.month(),
        'register day': fake.day_of_month(),
        'monthly income ($NT)': fake.random_int(28000, 100000)
    }

    return data

def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=['192.168.1.5:9092'], value_serializer=json_serializer)

if __name__ == '__main__':
    
    while 1 == 1:
        registered_data = get_registered_data()
        print(registered_data)
        producer.send('registered-user', value=registered_data)
        time.sleep(10)