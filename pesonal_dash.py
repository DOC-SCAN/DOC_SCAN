from pymongo import MongoClient

my_client = MongoClient()
my_client = MongoClient('mongodb://%s:%s@172.29.97.25:27017' % ('docscantest', 'mechanism_123'))

db = my_client["DOC_SCAN"]
collection = db['DOCUMENTS']

total_files = collection.distinct('mrno')
total_documents = collection.count_documents({})

if __name__ == '__main__':
    print(len(total_files))
    print(total_documents)