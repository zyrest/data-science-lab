from pymongo import MongoClient

username = 'cying'
password = 'Hk8Thdtnct'
host = '39.106.55.9:27017'
mongo_url = 'mongodb://{}:{}@{}'.format(username, password, host)

mg = MongoClient(mongo_url)
db = mg['data_sci']
jobs = db['jobs']
job_detail = db['job_detail']
com_detail = db['com_detail']
