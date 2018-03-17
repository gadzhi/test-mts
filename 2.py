from hdfs import InsecureClient
from hdfs import Config
client = InsecureClient('http://localhost:1080', user='admin')
client = Config().get_client('dev')


with client.read('features') as reader:
  features = reader.read()